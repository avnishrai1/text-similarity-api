
"""
model.py
---------
Part A: Semantic similarity using Sentence-Transformers.

We use a lightweight, high-quality model: "all-MiniLM-L6-v2".
Cosine similarity is in [-1, 1]. We map it to [0, 1] by (sim + 1) / 2
to strictly meet the assignment requirement.

Functions:
- normalize_text: basic cleanup (kept minimal since transformers are robust)
- get_similarity: returns a float in [0, 1] rounded to 4 decimals
-Avnish Mahan Hai 
"""

from typing import Optional
import re
from sentence_transformers import SentenceTransformer, util
import torch

# Load model once on module import (fast in API, avoids reloading per request)
_MODEL_NAME = "all-MiniLM-L6-v2"
_model = SentenceTransformer(_MODEL_NAME)

_whitespace_re = re.compile(r"\s+")

def normalize_text(s: Optional[str]) -> str:
    if s is None:
        return ""
    s = s.strip()
    s = _whitespace_re.sub(" ", s)
    return s

def _cosine_to_unit_interval(x: float) -> float:
    # Cosine similarity is in [-1, 1]. Convert to [0, 1].
    return max(0.0, min(1.0, (x + 1.0) / 2.0))

def get_similarity(text1: str, text2: str) -> float:
    """
    Compute semantic similarity between two texts.
    Returns a float between 0 and 1.
    """
    t1 = normalize_text(text1)
    t2 = normalize_text(text2)

    # Edge cases
    if not t1 and not t2:
        return 1.0  # both empty -> identical
    if not t1 or not t2:
        return 0.0  # one empty -> dissimilar

    emb1 = _model.encode(t1, convert_to_tensor=True, normalize_embeddings=True)
    emb2 = _model.encode(t2, convert_to_tensor=True, normalize_embeddings=True)
    sim = util.pytorch_cos_sim(emb1, emb2).item()  # in [-1, 1]
    score = _cosine_to_unit_interval(sim)
    return round(float(score), 4)
