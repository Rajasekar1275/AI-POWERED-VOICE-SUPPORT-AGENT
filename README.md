# 📊 AI-Powered Chat Support Agent (Gemini + Streamlit)

This project is an **AI customer support assistant** powered by **Google Gemini API** and deployed using **Streamlit Cloud**.  
It allows users to ask questions (via text) based on a provided **FAQ PDF**, and receive instant intelligent answers.

> 🎯 This version focuses on **text + chart output only**, as Streamlit Cloud currently doesn't support microphone or audio playback.

---

## 🚀 Live App

[![Open in Streamlit](https://ai-powered-voice-support-agent-jcs4fqmx62rm3cyvojqom4.streamlit.app/)

👉 Click the badge above to try the live chat agent.

---

## 📁 Features

✅ Upload and parse PDF FAQs  
✅ Ask questions via text input  
✅ AI finds relevant answers using vector search (FAISS)  
✅ Gemini API powers natural language understanding  
✅ Clean Streamlit UI with minimal dependencies  
✅ Deployment-ready with `.env` security

---

## 🧠 Tech Stack

| Component       | Tool / Library                     |
|----------------|------------------------------------|
| LLM             | [Google Gemini API](https://ai.google.dev/) |
| Framework       | [Streamlit](https://streamlit.io) |
| Vector DB       | FAISS                             |
| NLP Embeddings  | HuggingFace Transformers          |
| Document Loader | LangChain PDF Loader              |
| Environment     | Python + `.env` + `requirements.txt` |

---

