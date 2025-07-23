from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, VideoUnavailable
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Gemini model
genai.configure(api_key=os.getenv("AIzaSyB6S8O-9l0SH_HiGkjbh47J6_a3Y4xQdj0"))
model_gemini = genai.GenerativeModel("gemini-1.5-flash-latest")

# FastAPI app setup
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# In-memory storage for each video's chunks and index
video_chunks = {}
video_indices = {}

# Request schema for /extract
class ExtractRequest(BaseModel):
    video_id: str

# Request schema for /ask
class AskRequest(BaseModel):
    video_id: str
    question: str

# Endpoint to extract and embed transcript
@app.post("/extract")
async def extract_transcript(data: ExtractRequest):
    video_id = data.video_id

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
    except VideoUnavailable:
        raise HTTPException(status_code=404, detail="Video is unavailable.")
    except TranscriptsDisabled:
        raise HTTPException(status_code=403, detail="Transcripts are disabled for this video.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    full_text = " ".join([entry['text'] for entry in transcript])
    chunks = [full_text[i:i+512] for i in range(0, len(full_text), 512)]
    embeddings = model.encode(chunks)

    # Build FAISS index
    index = faiss.IndexFlatL2(384)
    index.add(np.array(embeddings))

    # Save index and chunks
    video_chunks[video_id] = chunks
    video_indices[video_id] = index

    return {"status": "Transcript processed", "chunks": len(chunks)}

# Endpoint to ask a question
@app.post("/ask")
async def ask_question(data: AskRequest):
    video_id = data.video_id
    question = data.question

    index = video_indices.get(video_id)
    chunks = video_chunks.get(video_id)
    
    if index is None or chunks is None:
        raise HTTPException(status_code=404, detail="Video ID not found. Please extract transcript first.")

    q_embed = model.encode([question])
    D, I = index.search(np.array(q_embed), k=3)

    context = " ".join([chunks[i] for i in I[0]])
    prompt = f"""Answer the following question based on the context:\n\nContext:\n{context}\n\nQuestion: {question}"""

    try:
        response = model_gemini.generate_content(prompt)
        return {"answer": response.text.strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Gemini API error: {str(e)}")
