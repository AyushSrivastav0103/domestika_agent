# Domestika Creative Assistant (AI Product Manager Assignment)

This is a functional prototype of the **Domestika Creative Assistant**, built as part of the Product Manager – AI take-home assignment.

The assistant supports two key user flows:
- 🎯 **Onboarding**: Recommends a 5-step micro-project path tailored to the learner's skill
- 🎨 **Feedback**: Gives actionable design tips to improve a creative draft

Built with Streamlit and Groq’s blazing-fast LLaMA-3 models.

---

## 🧠 Tech Stack

- `streamlit` – for interactive UI
- `openai` – Python SDK (used to call Groq’s OpenAI-compatible LLM endpoint)
- `dotenv` – local environment variable management
- Groq API – for high-speed LLaMA-3 (8B) inference

---

## 🚀 Running the App Locally

### 1. Clone this repo
```bash
git clone https://github.com/AyushSrivastav0103/domestika_agent.git
