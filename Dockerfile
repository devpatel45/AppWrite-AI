# syntax=docker/dockerfile:1.4

# Stage 1 — Builder
FROM python:3.12.11-slim AS builder

WORKDIR /app

# Enable BuildKit cache for pip
RUN apt-get update && apt-get install -y \
    build-essential cmake gcc g++ git python3-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN --mount=type=cache,target=/root/.cache \
    pip install --upgrade pip && \
    pip install --no-cache-dir --prefer-binary -r requirements.txt

# Copy only source code last (after deps, for better layer caching)
COPY . .

# Stage 2 — Final image
FROM python:3.12.11-slim
WORKDIR /app

# Copy deps from builder
COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy your code
COPY . .

EXPOSE 1414

CMD ["python3", "-m", "streamlit", "run", "UI/Interface.py", "--server.port=1414", "--server.address=0.0.0.0"]
