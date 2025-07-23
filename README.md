# 🧠 YouTube RAG Chatbot Chrome Extension

A Chrome Extension that allows users to ask questions about any YouTube video and get AI-powered answers — using **Retrieval-Augmented Generation (RAG)**, **YouTube transcripts**, **HuggingFace embeddings**, **FAISS**, and **Gemini Pro (Google Generative AI)** via a **FastAPI backend**.

---

## 📌 Features

- ✅ Chrome extension to interact with any YouTube video
- 🎙️ Fetches video transcript via **YouTube Transcript API**
- ✂️ Splits and embeds content using **HuggingFace Transformers**
- 💾 Stores vector data using **FAISS**
- 🧠 Sends context-aware queries to **Gemini Pro**
- ⚡ Uses a **FastAPI** backend for serving responses
- 📥 Provides real-time answers in the extension popup

---

## 🛠 Tech Stack

| Component         | Tool/Library                            |
|------------------|------------------------------------------|
| Language Model    | Gemini Pro via `langchain_google_genai` |
| Embeddings        | `sentence-transformers/all-MiniLM-L6-v2`|
| Vector DB         | FAISS (`langchain_community.vectorstores`) |
| Transcripts       | `youtube_transcript_api`                |
| Backend           | FastAPI                                 |
| Frontend          | HTML, JS, CSS (Chrome Extension)        |

---

## 📁 Project Structure


---

## 🚀 Getting Started

### 🔧 1. Backend Setup (FastAPI + LangChain + Gemini)

```bash
# Clone the repo
git clone https://github.com/your-username/youtube-rag-chatbot.git
cd youtube-rag-chatbot/backend

# Setup Python 3.10 virtual environment
python3.10 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
GOOGLE_API_KEY=your_google_gemini_api_key
uvicorn main:app --reload

🌐 2. Chrome Extension Setup
Go to chrome://extensions/ in Chrome

Enable Developer Mode

Click Load Unpacked

Select the /extension folder from the project directory

Open a YouTube video and launch the extension

💡 How It Works
Extract video ID from YouTube URL

Use youtube_transcript_api to fetch the transcript

Split the transcript into chunks using RecursiveCharacterTextSplitter

Embed each chunk with HuggingFaceEmbeddings

Store in FAISS vector index

On user question → retrieve top relevant chunks

Format context → query Gemini with langchain_google_genai

Return answer → display in popup

🤝 Credits
LangChain

HuggingFace

Gemini Pro

FAISS by Facebook

YouTube Transcript API

📄 License
This project is licensed under the MIT License.
