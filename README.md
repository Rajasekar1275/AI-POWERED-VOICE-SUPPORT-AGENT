# 🤖 AI-Powered Chat Support Agent (Gemini + Streamlit)

This is an AI-based **FAQ support agent** built using **Streamlit** and **Google's Gemini API**. It allows users to ask questions from a PDF-based FAQ document and receive accurate, real-time answers.

> ✨ Current version supports **chat-based interaction only**.  
> 🔊 Voice & audio features will be added in future releases (see below).

---

## 🎥 Demo Video

👉 [Click here to watch the demo video on Google Drive](https://drive.google.com/file/d/1z7EG2Ad4rCaHEOCZG0k3Y6xq474aTN8c/view?usp=sharing)

This video demonstrates:
- Asking questions via chat
- Getting Gemini-powered answers


## 🚀 Live Demo

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ai-powered-voice-support-agent-jcs4fqmx62rm3cyvojqom4.streamlit.app/)

👉 Click the badge above to try the app live.

---

## 📁 Features

✅ Ask questions via chat (text input)  
✅ AI understands context and responds intelligently  
✅ Gemini API powers natural language reasoning  
✅ Streamlit-based interactive frontend  
✅ Secure key handling using `.env` or Streamlit secrets

---

## 🔒 Limitations & Future Enhancements

| Feature             | Status   | Notes |
|---------------------|----------|-------|
| 💬 Text/Chat input   | ✅ Active | Chat input works fully |
| 🎤 Microphone input  | 🚫 Coming soon | Will be added with Render or Railway support |
| 🔊 Text-to-speech    | 🚫 Planned | Will work once deployed to a platform with audio support |
| 📱 Multi-device UX   | 🧪 Improving | UI will be optimized for mobile/tablets |

> 🔧 Currently hosted on **Streamlit Cloud**, which does not support real-time microphone/audio.  
> 🔜 Voice features will be enabled in future versions via **Render** or **Fly.io**.

---

## 🧠 Tech Stack

| Component       | Tool / Library                     |
|----------------|------------------------------------|
| LLM             | [Google Gemini API](https://ai.google.dev/) |
| Frontend        | [Streamlit](https://streamlit.io) |
| Vector Search   | FAISS                             |
| Embeddings      | HuggingFace Transformers          |
| PDF Loader      | LangChain                         |
| Deployment      | Streamlit Cloud                   |

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Rajasekar1275/AI-POWERED-VOICE-SUPPORT-AGENT.git
cd AI-POWERED-VOICE-SUPPORT-AGENT
