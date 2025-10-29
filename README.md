
# TextSimilarityProject

Semantic Textual Similarity (0–1) using Sentence-Transformers, with a FastAPI endpoint.

## Endpoints
- `POST /similarity`  
  Request: `{"text1": "...", "text2": "..."}`  
  Response: `{"similarity score": 0.1234}`  

- `GET /health` → `{"status":"ok"}`

## Local Setup

```bash
# 1) Create & activate virtual env (recommended)
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# 2) Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 3) (Optional) Score your dataset
python batch_infer.py --input DataNeuron_Text_Similarity.csv --output DataNeuron_Text_Similarity_scored.csv

# 4) Run API
uvicorn api:app --host 0.0.0.0 --port 8000

# 5) Test
curl -X POST "http://127.0.0.1:8000/similarity" \
  -H "Content-Type: application/json" \
  -d '{"text1":"I love NLP","text2":"I enjoy AI"}'
```

Open interactive docs at: http://127.0.0.1:8000/docs

## Deployment (Render.com - free)

1. Push this folder to a **new GitHub repo**.
2. Create a **new Web Service** on Render → **Connect Repo**.
3. Runtime: Python.  
   - Build Command: `pip install -r requirements.txt`  
   - Start Command: `uvicorn api:app --host 0.0.0.0 --port $PORT`
4. Wait for deploy → copy your **Live URL**.  
5. Test with:
```bash
curl -X POST "https://YOUR-SERVICE.onrender.com/similarity" \
  -H "Content-Type: application/json" \
  -d '{"text1":"nuclear body seeks new tech","text2":"terror suspects face arrest"}'
```

## Notes
- We map cosine similarity from [-1, 1] to [0, 1] as required by the assignment.
- The model is loaded once and kept in memory for fast inference.
- Code is fully commented and concise.


xyz