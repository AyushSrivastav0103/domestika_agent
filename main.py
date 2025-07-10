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
        "needs a micro-project path. List them clearly."
    )
    text = chat_completion(prompt)
    if not text:
        return "1. Basic strokes practice\n2. Letterforms drill\n3. Phrase composition\n4. Creative poster\n5. Peer feedback session"
    return text

def analyze_design():
    prompt = (
        "You’re a design mentor reviewing a creative draft. "
        "Suggest 3 concise, actionable tips to improve color, layout, or typography."
    )
    text = chat_completion(prompt)
    if not text:
        return (
            "1. Increase heading font size for emphasis\n"
            "2. Try a complementary color palette\n"
            "3. Align elements to a consistent grid"
        )
    return text

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
        st.success("Here’s your micro‑project path:")
        st.markdown(projects)

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
            st.markdown(tips)
