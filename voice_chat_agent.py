import streamlit as st
import os
from gtts import gTTS
import tempfile
from dotenv import load_dotenv
import google.generativeai as genai
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

# Load environment variables from .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# App Setup
st.set_page_config(page_title="AI Voice + Chat Agent")
st.title("📞 Voice & Chat Support Agent")

# Check API Key
if not api_key:
    st.error("🔐 GEMINI_API_KEY not found. Please add it to your .env file.")
    st.stop()

# Configure Gemini
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Your prompt here")


# Load faqs.pdf from folder
pdf_path = "faqs.pdf"
if not os.path.exists(pdf_path):
    st.error("❌ 'faqs.pdf' not found in the project folder.")
    st.stop()

@st.cache_resource
def load_faq_to_db(path):
    loader = PyPDFLoader(path)
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    split_docs = splitter.split_documents(docs)
    embeddings = HuggingFaceEmbeddings()
    db = FAISS.from_documents(split_docs, embeddings)
    return db

db = load_faq_to_db(pdf_path)

# Chat + Retrieval
def query_gemini_with_faq(query, db):
    docs = db.similarity_search(query, k=3)
    context = "\n".join(doc.page_content for doc in docs)
    prompt = f"""Answer the user's question using only the context below.

Context:
{context}

Question: {query}

If the answer is not in the context, say: I do not have an answer to that question. Let me transfer your call to the live agent.
"""
    response = model.generate_content(prompt)
    return response.text.strip()

# Text-to-speech
def speak_text(text):
    tts = gTTS(text)
    tts.save("output.mp3")
    st.audio("output.mp3", format="audio/mp3")
    os.remove("output.mp3")

# Chat UI
query = st.text_input("💬 Ask your question here:")
if st.button("Ask"):
    if query:
        answer = query_gemini_with_faq(query, db)
        st.success(answer)
        speak_text(answer)
    else:
        st.warning("Please enter a question.")
