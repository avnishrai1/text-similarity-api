
"""
api.py
------
Part B: FastAPI server exposing the algorithm as a Server API Endpoint.

Endpoint (POST): /similarity
Request body: {"text1": "...", "text2": "..."}
Response body: {"similarity score": 0.1234}
"""

from fastapi import FastAPI
from pydantic import BaseModel
from model import get_similarity

app = FastAPI(
    title="Text Similarity API",
    description=(
        "Semantic Textual Similarity using Sentence-Transformers.\n\n"
        "POST /similarity with JSON: {\"text1\": \"...\", \"text2\": \"...\"}\n"
        "Response: {\"similarity score\": 0.1234}"
    ),
    version="1.0.0",
)

class TextPair(BaseModel):
    text1: str
    text2: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/similarity")
def similarity_endpoint(pair: TextPair):
    score = get_similarity(pair.text1, pair.text2)
    # IMPORTANT: Key must be exactly "similarity score" per assignment.
    return {"similarity score": score}

# For local dev: `python api.py` then visit http://127.0.0.1:8000/docs
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)
