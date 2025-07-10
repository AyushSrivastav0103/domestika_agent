# 📝 README — Creative Assistant Prototype  
**Author:** Ayush Srivastava  
**Submission for:** PM – Creative Assistant Assignment  
**Prototype Link:** [https://ayushsrivastav0103-domestika-agent-main-vrtvyc.streamlit.app/](https://ayushsrivastav0103-domestika-agent-main-vrtvyc.streamlit.app/)

---

> **Note:**  
> This app is hosted on Streamlit Community Cloud (free tier).  
> If the app has been idle, it may take up to a minute to start.  
> Please refresh the page if you see a loading spinner for a long time.
> or give a call at 8588054237
##  Setup Steps

1. **Open : https://ayushsrivastav0103-domestika-agent-main-vrtvyc.streamlit.app/ **  
   Deployed via [Streamlit Cloud](https://streamlit.io/cloud); no local setup needed.

2. **Flows implemented:**
   - `Onboarding`: Select a skill → get a 5-step creative project path from the AI.
   - `Feedback`: Upload a draft image → get AI-generated improvement tips.

3. **Backend:**
   - Powered by **Groq API (LLaMA 3)** for ultra-fast LLM inference.
   - Stateless prompt design with minimal context requirements.

---

##  Known Gaps (MVP Constraints)

| Limitation                     | Notes |
|-------------------------------|-------|
|  No real image analysis      | Draft image upload is symbolic; feedback is based on static prompt. |
|  Stateless interaction       | No memory or session history across steps. |
|  No user authentication      | Open use; not personalized or rate-limited. |
|  Limited safety/guardrails  | No toxic output detection or moderation pipeline yet. |

---

##  Next Experiments

| Opportunity                         | Rationale |
|-------------------------------------|-----------|
|  **Add memory + user state**       | Personalize journeys based on past progress. |
|  **Multimodal model for real image feedback** | Enable actual visual feedback on design drafts. |
|  **Peer navigator recommendations** | Suggest learners or mentors for collaboration, based on goals. |
|  **Live feedback scoring UI**     | Let users rate feedback to improve prompt tuning. |
|  **Moderation & hallucination guardrails** | Ensure safe, high-trust responses from LLMs. |

---

##  Submission Links

- **Prototype**: [Streamlit App](https://ayushsrivastav0103-domestika-agent-main-vrtvyc.streamlit.app/)
- **Slides Deck**: [Strategy & Roadmap](https://docs.google.com/presentation/d/1on31JdiqKoT3l3jNuIRgNokjd_yz5cQM-f9T8xK9_xQ/edit?usp=sharing)
- **Metrics Sheet**: [Metrics & Ops](https://docs.google.com/spreadsheets/d/1L5ck572twRAirezBGJ3tbo7GwVfqHs17utG19Mr0l4g/edit?usp=sharing)
- **Github Repo**: (https://github.com/AyushSrivastav0103/domestika_agent)
- **Demo Video**: https://www.loom.com/share/cc4adcc0d2794ce3bf97d7b9fe4fa9e8?sid=205e9a45-dad7-41e1-93a8-9f5309e73c6c