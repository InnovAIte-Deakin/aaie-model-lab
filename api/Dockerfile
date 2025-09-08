# Dockerfile for Hugging Face Model Deployment
# Multi-stage build for optimized production image

# Stage 1: Base image with Python and system dependencies
FROM python:3.9-slim as base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# Stage 2: Development image with ML dependencies
FROM base as development

# Install PyTorch and ML dependencies
RUN pip install --no-cache-dir \
    torch==2.0.1 \
    torchvision==0.15.2 \
    torchaudio==2.0.2 \
    --index-url https://download.pytorch.org/whl/cpu

# Install Hugging Face and other ML libraries
RUN pip install --no-cache-dir \
    transformers==4.35.0 \
    datasets==2.14.0 \
    accelerate==0.24.0 \
    sentencepiece==0.1.99 \
    protobuf==3.20.3

# Stage 3: Production image
FROM development as production

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install additional ML dependencies
RUN pip install --no-cache-dir \
    transformers==4.35.0 \
    torch==2.0.1 \
    accelerate==0.24.0

# Copy application code
COPY . .

# Create non-root user for security
RUN useradd --create-home --shell /bin/bash app \
    && chown -R app:app /app
USER app

# Expose port
EXPOSE 5001

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:5001/health || exit 1

# Set environment variables
ENV PORT=5001
ENV MODEL_TYPE=simple
ENV MODEL_NAME=distilbert-base-uncased

# Run the application
CMD ["python", "app.py"]

# Stage 4: GPU-enabled image (optional)
FROM nvidia/cuda:11.8-runtime-ubuntu20.04 as gpu

# Install Python
RUN apt-get update && apt-get install -y \
    python3.9 \
    python3.9-pip \
    python3.9-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip3.9 install --no-cache-dir -r requirements.txt

# Install GPU-enabled PyTorch and transformers
RUN pip3.9 install --no-cache-dir \
    torch==2.0.1+cu118 \
    torchvision==0.15.2+cu118 \
    torchaudio==2.0.2+cu118 \
    --index-url https://download.pytorch.org/whl/cu118

RUN pip3.9 install --no-cache-dir \
    transformers==4.35.0 \
    accelerate==0.24.0

# Copy application code
COPY . .

# Create non-root user
RUN useradd --create-home --shell /bin/bash app \
    && chown -R app:app /app
USER app

# Expose port
EXPOSE 5001

# Set environment variables for GPU
ENV PORT=5001
ENV MODEL_TYPE=simple
ENV MODEL_NAME=distilbert-base-uncased
ENV CUDA_VISIBLE_DEVICES=0

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:5001/health || exit 1

# Run the application
CMD ["python3.9", "app.py"]
