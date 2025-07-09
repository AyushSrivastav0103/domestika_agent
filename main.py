# main.py

import os
from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st

# ─── Load API Key ───────────────────────────────────────────────────────────────

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    st.error("GROQ_API_KEY not found in environment variables.")
    st.stop()

# ─── OpenAI-Compatible Client Setup for Groq ────────────────────────────────────

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=GROQ_API_KEY
)

MODEL = "llama3-8b-8192"  # Fast & good quality

# ─── Chat Completion Wrapper ────────────────────────────────────────────────────

def chat_completion(prompt: str) -> str | None:
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=7000
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        st.error(f"Groq API error: {e}")
        print(f"Groq API error: {e}")
        return None

# ─── Creative Assistant Logic ───────────────────────────────────────────────────

def recommend_next_project(skill: str):
    prompt = (
        f"You’re an expert creative coach. A learner who knows '{skill}' "
        "needs a 5-step micro-project path. List them clearly."
    )
    text = chat_completion(prompt)
    if not text:
        return [
            "Basic strokes practice",
            "Letterforms drill",
            "Phrase composition",
            "Creative poster",
            "Peer feedback session"
        ]

    projects = []
    for line in text.splitlines():
        cleaned = line.strip().lstrip("0123456789.- ").strip()
        if cleaned:
            projects.append(cleaned)
    return projects[:5]

def analyze_design():
    prompt = (
        "You’re a design mentor reviewing a creative draft. "
        "Suggest 3 concise, actionable tips to improve color, layout, or typography."
    )
    text = chat_completion(prompt)
    if not text:
        return [
            "Increase heading font size for emphasis",
            "Try a complementary color palette",
            "Align elements to a consistent grid"
        ]
    tips = []
    for line in text.splitlines():
        cleaned = line.strip().lstrip("-0123456789. ").strip()
        if cleaned:
            tips.append(cleaned)
    return tips[:3]

# ─── Streamlit UI ───────────────────────────────────────────────────────────────

st.set_page_config(page_title="Domestika Creative Assistant", layout="wide")
st.sidebar.title("Creative Assistant")

flow = st.sidebar.selectbox("Choose flow", ["Onboarding", "Feedback"])

if flow == "Onboarding":
    st.title("Creative Assistant: Onboarding")

    skill = st.selectbox(
        "Pick a skill to level up",
        ["Hand‑Lettering", "Illustration", "UX Design"]
    )

    if st.button("Start"):
        with st.spinner("Generating your personalized path..."):
            projects = recommend_next_project(skill)
        st.success("Here’s your 5‑step micro‑project path:")
        for i, p in enumerate(projects, 1):
            st.write(f"{i}. {p}")

else:
    st.title("Creative Assistant: Feedback")
    draft = st.file_uploader("Upload your draft image", type=["png", "jpg", "jpeg"])

    if st.button("Get Feedback"):
        if not draft:
            st.warning("Please upload an image first.")
        else:
            with st.spinner("Analyzing your design..."):
                tips = analyze_design()
            st.success("Here are some actionable tips:")
            for tip in tips:
                st.write(f"• {tip}")
