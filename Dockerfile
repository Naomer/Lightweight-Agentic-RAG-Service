FROM python:3.11-slim

# 1. Install system dependencies for FAISS
RUN apt-get update && apt-get install -y \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# 2. Copy requirements
COPY requirements.txt .

# 3. Force the CPU-only index and upgrade pip
RUN pip install --upgrade pip && \
    pip install --no-cache-dir \
    --extra-index-url https://download.pytorch.org/whl/cpu \
    -r requirements.txt

# 4. Copy project
COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
