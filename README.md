🚀 YouTube RAG Chatbot Chrome Extension
A powerful Chrome extension that enables users to interact with YouTube videos using a context-aware Q&A chatbot — powered by Retrieval-Augmented Generation (RAG) and Gemini Pro (Google Generative AI).


🧠 What It Does
✅ Works as a Chrome Extension
✅ Extracts transcripts from any YouTube video
✅ Splits and embeds the content using HuggingFace Transformers
✅ Stores embeddings using FAISS vector store
✅ Answers questions using Gemini Pro
✅ FastAPI backend for handling RAG responses in real time

📦 Tech Stack
Frontend: HTML/CSS/JS (Chrome Extension)

Backend: FastAPI

LLM: Gemini Pro (Google Generative AI)

Embeddings: Hugging Face Transformers

Vector Store: FAISS

Transcripts: YouTube Transcript API

🛠️ How It Works
Injects content script to access the current YouTube video URL.

Extracts the video transcript using the YouTube Transcript API.

Splits and embeds the transcript into vector representations.

Stores these embeddings in a FAISS vector store.

Sends the user’s question to the backend (FastAPI).

Performs similarity search, constructs context, and queries Gemini Pro.

Displays real-time answers in a floating chat window on the video.

📁 Project Structure
css
Copy
Edit
📦youtube-rag-chatbot
 ┣ 📂backend
 ┃ ┣ 📜main.py
 ┃ ┣ 📜utils.py
 ┃ ┣ 📜requirements.txt
 ┣ 📂extension
 ┃ ┣ 📜manifest.json
 ┃ ┣ 📜popup.html
 ┃ ┣ 📜popup.js
 ┃ ┣ 📜content.js
 ┣ 📜README.md

🚀 Getting Started
Backend Setup
bash
Copy
Edit
cd backend
python3.10 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
Chrome Extension Setup
Open Chrome and go to chrome://extensions/

Enable Developer Mode

Click Load Unpacked and select the extension/ folder

Open a YouTube video and interact with the bot

🙌 Acknowledgements
LangChain

HuggingFace Transformers

Gemini Pro

FAISS
