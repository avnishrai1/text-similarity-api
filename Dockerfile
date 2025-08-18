# Slim image to reduce memory/size
FROM python:3.10-slim

# Avoid interactive prompts / speed up installs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Workdir
WORKDIR /app

# Install system packages only if needed (most likely not required)
# RUN apt-get update && apt-get install -y --no-install-recommends build-essential && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better Docker layer caching
COPY requirements.txt /app/requirements.txt

# Install Python deps
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r /app/requirements.txt

# Copy the rest of the app
COPY . /app

# Cloud Run provides PORT; default to 8080 if missing
ENV PORT=8080

# Expose for clarity (Cloud Run routes automatically)
EXPOSE 8080

# Start FastAPI (listen on $PORT)
CMD ["sh", "-c", "uvicorn api:app --host 0.0.0.0 --port ${PORT}"]
