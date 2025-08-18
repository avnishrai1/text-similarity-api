
import requests

url = "http://127.0.0.1:8000/similarity"
payload = {"text1": "I love machine learning", "text2": "I enjoy studying AI"}

resp = requests.post(url, json=payload, timeout=30)
print(resp.status_code, resp.json())
