# Dockerfile for Google Gemini Model Deployment
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

# Stage 2: Development image
FROM base as development

# Install Python dependencies
RUN pip install --no-cache-dir \
    google-generativeai==0.3.2 \
    google-auth==2.23.4 \
    google-auth-oauthlib==1.1.0 \
    google-auth-httplib2==0.1.1

# Stage 3: Production image
FROM development as production

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

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
ENV GOOGLE_AI_API_KEY=""

# Run the application
CMD ["python", "app.py"]

# Stage 4: Development image with debugging tools
FROM production as dev

# Switch back to root for development tools
USER root

# Install development dependencies
RUN pip install --no-cache-dir \
    ipython \
    jupyter \
    pytest \
    pytest-cov \
    black \
    flake8

# Copy development scripts
COPY --chown=app:app . .

# Switch back to app user
USER app

# Expose Jupyter port
EXPOSE 8888

# Development command
CMD ["python", "app.py"]
