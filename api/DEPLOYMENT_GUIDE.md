# Hugging Face Model Deployment Guide

## Overview
This guide provides comprehensive instructions for deploying Hugging Face models locally using our AAIE Rubric Scoring API. The deployment supports both local development and production environments with Docker containerization.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Local Deployment](#local-deployment)
3. [Docker Deployment](#docker-deployment)
4. [Google Colab Deployment](#google-colab-deployment)
5. [Testing and Validation](#testing-and-validation)
6. [Performance Monitoring](#performance-monitoring)
7. [Troubleshooting](#troubleshooting)

## Prerequisites

### System Requirements
- Python 3.8+
- 8GB+ RAM (16GB recommended for larger models)
- 5GB+ free disk space
- CUDA-compatible GPU (optional, for faster inference)

### Software Dependencies
```bash
# Core dependencies
pip install torch torchvision torchaudio
pip install transformers datasets accelerate
pip install flask flask-cors requests
pip install sentencepiece protobuf

# Optional for GPU support
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

## Local Deployment

### 1. Quick Start
```bash
# Clone the repository
git clone <repository-url>
cd aaie-model-lab/api

# Install dependencies
pip install -r requirements.txt

# Run the API with HF model integration
python app.py
```

### 2. Environment Configuration
Create a `.env` file:
```bash
# API Configuration
PORT=5001
MODEL_TYPE=simple
MODEL_NAME=distilbert-base-uncased

# Optional: GPU Configuration
CUDA_VISIBLE_DEVICES=0
```

### 3. Model Selection
The API supports different Hugging Face models:

| Model Type | Model Name | Use Case | Memory Usage |
|------------|------------|----------|--------------|
| Simple | `distilbert-base-uncased` | Quick testing | ~500MB |
| Advanced | `microsoft/DialoGPT-medium` | Better accuracy | ~1.5GB |
| Custom | `your-model-name` | Domain-specific | Varies |

## Docker Deployment

### 1. Build Docker Image
```bash
# CPU-only image
docker build -t hf-rubric-api .

# GPU-enabled image
docker build --target gpu -t hf-rubric-api-gpu .
```

### 2. Run Container
```bash
# CPU deployment
docker run -p 5001:5001 \
  -e MODEL_TYPE=simple \
  -e MODEL_NAME=distilbert-base-uncased \
  hf-rubric-api

# GPU deployment
docker run --gpus all -p 5001:5001 \
  -e MODEL_TYPE=simple \
  -e MODEL_NAME=distilbert-base-uncased \
  hf-rubric-api-gpu
```

### 3. Docker Compose (Recommended)
Create `docker-compose.yml`:
```yaml
version: '3.8'
services:
  hf-rubric-api:
    build: .
    ports:
      - "5001:5001"
    environment:
      - PORT=5001
      - MODEL_TYPE=simple
      - MODEL_NAME=distilbert-base-uncased
    volumes:
      - ./models:/app/models
    restart: unless-stopped
    
  # Optional: GPU-enabled service
  hf-rubric-api-gpu:
    build:
      context: .
      target: gpu
    ports:
      - "5002:5001"
    environment:
      - PORT=5001
      - MODEL_TYPE=simple
      - MODEL_NAME=distilbert-base-uncased
      - CUDA_VISIBLE_DEVICES=0
    volumes:
      - ./models:/app/models
    restart: unless-stopped
    deploy:
      resources:
        reservations:
          devices:
            - driver: nvidia
              count: 1
              capabilities: [gpu]
```

Run with Docker Compose:
```bash
docker-compose up -d
```

## Google Colab Deployment

### 1. Open Colab Notebook
- Upload `hf_deployment_colab.ipynb` to Google Colab
- Ensure GPU runtime is enabled (Runtime → Change runtime type → GPU)

### 2. Run Deployment
```python
# Install dependencies
!pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
!pip install transformers datasets accelerate flask flask-cors

# Run the notebook cells
# Follow the step-by-step instructions in the notebook
```

### 3. Colab-Specific Features
- Automatic GPU detection
- Performance visualization
- Model comparison tools
- Export results to CSV/JSON

## Testing and Validation

### 1. Health Check
```bash
curl http://localhost:5001/health
```

Expected response:
```json
{
  "status": "healthy",
  "service": "LLM Rubric Scoring API",
  "version": "1.0.0"
}
```

### 2. Model Evaluation Test
```bash
curl -X POST http://localhost:5001/llm/rubric-score \
  -H "Content-Type: application/json" \
  -d '{"student_submission": "This is a test essay about climate change."}'
```

Expected response:
```json
{
  "Structure": "Good",
  "Clarity": "Good",
  "Relevance": "Good",
  "Academic_Writing": "Good"
}
```

### 3. Comprehensive Testing
```bash
# Run unit tests
python test_and_demo.py

# Run integration tests
python app.py &
python test_and_demo.py --integration
```

### 4. Load Testing
```python
import requests
import time
import concurrent.futures

def test_api_performance():
    url = "http://localhost:5001/llm/rubric-score"
    data = {"student_submission": "Test submission for performance testing."}
    
    def make_request():
        start_time = time.time()
        response = requests.post(url, json=data)
        end_time = time.time()
        return response.status_code, end_time - start_time
    
    # Test with 10 concurrent requests
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(make_request) for _ in range(10)]
        results = [future.result() for future in futures]
    
    # Analyze results
    success_rate = sum(1 for status, _ in results if status == 200) / len(results)
    avg_time = sum(time for _, time in results) / len(results)
    
    print(f"Success Rate: {success_rate:.2%}")
    print(f"Average Response Time: {avg_time:.3f}s")

test_api_performance()
```

## Performance Monitoring

### 1. Model Performance Metrics
- **Inference Time**: Average time per evaluation
- **Throughput**: Evaluations per second
- **Memory Usage**: RAM and GPU memory consumption
- **Accuracy**: Model prediction quality

### 2. API Performance Metrics
- **Response Time**: End-to-end API response time
- **Throughput**: Requests per second
- **Error Rate**: Percentage of failed requests
- **Availability**: Uptime percentage

### 3. Monitoring Dashboard
```python
import matplotlib.pyplot as plt
import pandas as pd

def create_performance_dashboard(metrics_data):
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    
    # Response time over time
    axes[0, 0].plot(metrics_data['timestamps'], metrics_data['response_times'])
    axes[0, 0].set_title('Response Time Over Time')
    axes[0, 0].set_ylabel('Response Time (s)')
    
    # Throughput histogram
    axes[0, 1].hist(metrics_data['throughput'], bins=20, alpha=0.7)
    axes[0, 1].set_title('Throughput Distribution')
    axes[0, 1].set_xlabel('Requests per Second')
    
    # Error rate
    axes[1, 0].bar(['Success', 'Error'], metrics_data['error_counts'])
    axes[1, 0].set_title('Success vs Error Rate')
    
    # Memory usage
    axes[1, 1].plot(metrics_data['timestamps'], metrics_data['memory_usage'])
    axes[1, 1].set_title('Memory Usage Over Time')
    axes[1, 1].set_ylabel('Memory (MB)')
    
    plt.tight_layout()
    plt.show()
```

## Troubleshooting

### Common Issues

#### 1. Model Loading Errors
**Problem**: Model fails to load
**Solutions**:
```bash
# Check internet connection
ping huggingface.co

# Clear model cache
rm -rf ~/.cache/huggingface/

# Try different model
export MODEL_NAME=distilbert-base-uncased
```

#### 2. CUDA/GPU Issues
**Problem**: CUDA not available
**Solutions**:
```bash
# Check CUDA installation
nvidia-smi

# Install CUDA-enabled PyTorch
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Force CPU usage
export CUDA_VISIBLE_DEVICES=""
```

#### 3. Memory Issues
**Problem**: Out of memory errors
**Solutions**:
```bash
# Use smaller model
export MODEL_NAME=distilbert-base-uncased

# Reduce batch size
export BATCH_SIZE=1

# Use CPU instead of GPU
export CUDA_VISIBLE_DEVICES=""
```

#### 4. Port Conflicts
**Problem**: Port 5001 already in use
**Solutions**:
```bash
# Find process using port
lsof -i :5001

# Kill process
kill -9 <PID>

# Use different port
export PORT=5002
```

### Debug Mode
Enable debug logging:
```bash
export LOG_LEVEL=DEBUG
python app.py
```

### Log Analysis
```bash
# View API logs
docker logs hf-rubric-api

# Follow logs in real-time
docker logs -f hf-rubric-api

# Check specific error patterns
docker logs hf-rubric-api 2>&1 | grep ERROR
```

## Best Practices

### 1. Model Selection
- Start with smaller models for testing
- Use domain-specific models for better accuracy
- Consider model size vs. performance trade-offs

### 2. Resource Management
- Monitor memory usage during deployment
- Use GPU for production workloads
- Implement proper error handling and fallbacks

### 3. Security
- Use non-root users in Docker containers
- Implement rate limiting for API endpoints
- Validate all input data

### 4. Monitoring
- Set up health checks and alerts
- Monitor performance metrics continuously
- Log all API requests and responses

## Next Steps

1. **Production Deployment**: Deploy to cloud platforms (AWS, GCP, Azure)
2. **Model Fine-tuning**: Customize models for specific domains
3. **Batch Processing**: Implement batch evaluation capabilities
4. **API Scaling**: Add load balancing and auto-scaling
5. **Model Versioning**: Implement model version management

## Support

For issues and questions:
- Check the troubleshooting section above
- Review API documentation in `API_README.md`
- Test with the provided examples
- Contact the development team

---

**Last Updated**: January 2025  
**Version**: 1.0.0  
**Status**: Production Ready ✅
