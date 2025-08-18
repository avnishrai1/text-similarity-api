
# DataNeuron STS Task – Short Report (1–2 pages)

**Candidate:** <Your Name>  
**Contact:** <Phone/Email>  
**Date:** <Date>

## Problem
Estimate **semantic similarity** between two texts and return a score in **[0, 1]**. Provide a **live API**.

## Approach (Part A)
- **Model:** Sentence-Transformers `"all-MiniLM-L6-v2"` (pre-trained on NLI/MSMARCO; good general STS).
- **Preprocessing:** Minimal (trim/normalize whitespace). Transformers are robust to casing/punctuation.
- **Scoring:** Cosine similarity of embeddings → mapped from **[-1,1] to [0,1]** via `(sim+1)/2`.
- **Edge cases:** Both empty → 1.0, one empty → 0.0.
- **Batch script:** `batch_infer.py` scores the provided CSV and outputs `similarity score` column.

### Why this model?
- Strong performance vs size; very fast on CPU; zero-shot, no labels required.

## Deployment (Part B)
- **Framework:** FastAPI.
- **Endpoint:** `POST /similarity`
  - Request: `{"text1":"...","text2":"..."}`
  - Response: `{"similarity score": 0.1234}`
- **Hosting:** Render.com (free tier).
  - Build: `pip install -r requirements.txt`
  - Start: `uvicorn api:app --host 0.0.0.0 --port $PORT`

## Validation
- Manual spot checks on identical/near-duplicate/dissimilar pairs.
- Sanity examples included in `test_api.py`.

## Limitations & Future Work
- Domain-specific nuance could benefit from fine-tuning on in-domain pairs (if labels available).
- Add language detection & multilingual model for cross-lingual cases.
- Add caching + batching for high QPS; Dockerize for portability.
- Optional UI (Gradio) for demo alongside the API.
