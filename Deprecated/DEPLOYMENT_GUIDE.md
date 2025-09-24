# Google Gemini Model Deployment Guide

## Overview
This guide provides comprehensive instructions for deploying the LLM Rubric Scoring API with Google Gemini AI integration using Docker containerization. The deployment supports both local development and production environments.

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
- 4GB+ RAM (8GB recommended)
- 2GB+ free disk space
- Docker and Docker Compose (for containerized deployment)

### Software Dependencies
```bash
# Core dependencies
pip install google-generativeai==0.3.2
pip install google-auth==2.23.4
pip install flask flask-cors requests
pip install python-dotenv

# Docker (if using containerized deployment)
# Install Docker Desktop from https://www.docker.com/products/docker-desktop
```

### Google AI API Key
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Create a new API key
4. Copy the API key for configuration

## Local Deployment

### 1. Quick Start
```bash
# Clone the repository
git clone <repository-url>
cd aaie-model-lab/Deprecated

# Install dependencies
pip install -r requirements.txt

# Set up API key
export GOOGLE_AI_API_KEY="your-api-key-here"

# Run the API with Gemini integration
python app.py
```

### 2. Environment Configuration
Create a `.env` file:
```bash
# API Configuration
PORT=5001
GOOGLE_AI_API_KEY=your-api-key-here

# Optional: Logging Configuration
LOG_LEVEL=INFO
```

### 3. Model Configuration
The API uses Google Gemini-1.5-flash model with the following settings:
- **Model**: `gemini-1.5-flash` (fast and efficient)
- **Temperature**: `0.1` (low for consistent evaluation)
- **Max Output Tokens**: `1000`
- **Safety Settings**: Configured for educational content

## Docker Deployment

### 1. Build Docker Image
```bash
# Production image
docker build -t gemini-rubric-api .

# Development image with debugging tools
docker build --target dev -t gemini-rubric-api-dev .
```

### 2. Run Container
```bash
# Production deployment
docker run -p 5001:5001 \
  -e GOOGLE_AI_API_KEY="your-api-key-here" \
  gemini-rubric-api

# Development deployment
docker run -p 5001:5001 -p 8888:8888 \
  -e GOOGLE_AI_API_KEY="your-api-key-here" \
  -e LOG_LEVEL=DEBUG \
  -v $(pwd):/app \
  gemini-rubric-api-dev
```

### 3. Docker Compose (Recommended)
Create `.env` file:
```bash
GOOGLE_AI_API_KEY=your-api-key-here
```

Run with Docker Compose:
```bash
# Production deployment
docker-compose up -d

# Development deployment
docker-compose --profile dev up -d

# With Nginx reverse proxy
docker-compose --profile production up -d
```

### 4. Docker Compose Configuration
The `docker-compose.yml` includes:
- **Production service**: Optimized for production use
- **Development service**: Includes debugging tools and hot reload
- **Nginx proxy**: Optional reverse proxy for production
- **Health checks**: Automatic health monitoring
- **Volume mounts**: Persistent logging

## Google Colab Deployment

### 1. Open Colab Notebook
- Upload `gemini_deployment_colab.ipynb` to Google Colab
- Ensure you have a Google AI API key

### 2. Run Deployment
```python
# Install dependencies
!pip install google-generativeai==0.3.2
!pip install flask flask-cors requests

# Set up API key
import os
os.environ['GOOGLE_AI_API_KEY'] = 'your-api-key-here'

# Run the notebook cells
# Follow the step-by-step instructions in the notebook
```

### 3. Colab-Specific Features
- Automatic API key setup
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
  -d '{"student_submission": "This is a test essay about climate change and its economic impacts."}'
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
python test_app.py

# Test with Docker
docker run --rm -e GOOGLE_AI_API_KEY="your-key" gemini-rubric-api python test_app.py
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
    
    # Test with 5 concurrent requests (Gemini has rate limits)
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(make_request) for _ in range(5)]
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
- **Inference Time**: Average time per evaluation (~2-5 seconds)
- **Throughput**: Evaluations per second (limited by Gemini API)
- **Memory Usage**: RAM consumption (~500MB)
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

#### 1. API Key Issues
**Problem**: "Google AI API key is required"
**Solutions**:
```bash
# Check environment variable
echo $GOOGLE_AI_API_KEY

# Set API key
export GOOGLE_AI_API_KEY="your-api-key-here"

# Check API key validity
curl -H "Authorization: Bearer $GOOGLE_AI_API_KEY" \
  "https://generativelanguage.googleapis.com/v1beta/models"
```

#### 2. Rate Limiting
**Problem**: Gemini API rate limit exceeded
**Solutions**:
```bash
# Implement request queuing
# Add delays between requests
# Use batch processing when possible
# Monitor usage in Google AI Studio
```

#### 3. Network Issues
**Problem**: Cannot connect to Gemini API
**Solutions**:
```bash
# Check internet connection
ping generativelanguage.googleapis.com

# Check firewall settings
# Use proxy if behind corporate firewall
# Verify DNS resolution
```

#### 4. Memory Issues
**Problem**: Out of memory errors
**Solutions**:
```bash
# Monitor memory usage
docker stats

# Increase container memory limits
docker run -m 2g -p 5001:5001 gemini-rubric-api

# Use smaller batch sizes
# Implement request queuing
```

#### 5. Port Conflicts
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
# Local deployment
export LOG_LEVEL=DEBUG
python app.py

# Docker deployment
docker run -e LOG_LEVEL=DEBUG -p 5001:5001 gemini-rubric-api
```

### Log Analysis
```bash
# View API logs
docker logs gemini-rubric-api

# Follow logs in real-time
docker logs -f gemini-rubric-api

# Check specific error patterns
docker logs gemini-rubric-api 2>&1 | grep ERROR
```

## Best Practices

### 1. API Key Management
- Never commit API keys to version control
- Use environment variables or secure key management
- Rotate API keys regularly
- Monitor API usage and costs

### 2. Resource Management
- Monitor memory usage during deployment
- Implement proper error handling and fallbacks
- Use health checks for container monitoring
- Set appropriate resource limits

### 3. Security
- Use non-root users in Docker containers
- Implement rate limiting for API endpoints
- Validate all input data
- Use HTTPS in production

### 4. Monitoring
- Set up health checks and alerts
- Monitor performance metrics continuously
- Log all API requests and responses
- Track API usage and costs

## Production Deployment

### 1. Cloud Platform Deployment
```bash
# AWS ECS
aws ecs create-service --cluster my-cluster --service-name gemini-api

# Google Cloud Run
gcloud run deploy gemini-api --source .

# Azure Container Instances
az container create --resource-group myRG --name gemini-api
```

### 2. Kubernetes Deployment
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: gemini-rubric-api
spec:
  replicas: 3
  selector:
    matchLabels:
      app: gemini-rubric-api
  template:
    metadata:
      labels:
        app: gemini-rubric-api
    spec:
      containers:
      - name: gemini-api
        image: gemini-rubric-api:latest
        ports:
        - containerPort: 5001
        env:
        - name: GOOGLE_AI_API_KEY
          valueFrom:
            secretKeyRef:
              name: gemini-secrets
              key: api-key
```

### 3. Load Balancing
```nginx
upstream gemini_api {
    server gemini-rubric-api-1:5001;
    server gemini-rubric-api-2:5001;
    server gemini-rubric-api-3:5001;
}

server {
    listen 80;
    location / {
        proxy_pass http://gemini_api;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

## Cost Optimization

### 1. API Usage Monitoring
- Monitor token usage in Google AI Studio
- Set up billing alerts
- Implement request caching
- Use batch processing when possible

### 2. Resource Optimization
- Use appropriate container sizes
- Implement auto-scaling
- Monitor memory and CPU usage
- Optimize Docker images

### 3. Caching Strategies
```python
import redis
import json
import hashlib

class GeminiCache:
    def __init__(self):
        self.redis_client = redis.Redis(host='localhost', port=6379, db=0)
    
    def get_cached_result(self, submission):
        key = hashlib.md5(submission.encode()).hexdigest()
        cached = self.redis_client.get(key)
        if cached:
            return json.loads(cached)
        return None
    
    def cache_result(self, submission, result):
        key = hashlib.md5(submission.encode()).hexdigest()
        self.redis_client.setex(key, 3600, json.dumps(result))  # 1 hour TTL
```

## Next Steps

1. **Production Deployment**: Deploy to cloud platforms (AWS, GCP, Azure)
2. **Model Optimization**: Fine-tune prompts for better accuracy
3. **Batch Processing**: Implement batch evaluation capabilities
4. **API Scaling**: Add load balancing and auto-scaling
5. **Monitoring**: Implement comprehensive monitoring and alerting

## Support

For issues and questions:
- Check the troubleshooting section above
- Review Gemini integration guide in `GEMINI_INTEGRATION_GUIDE.md`
- Test with the provided examples
- Contact the development team

---

**Last Updated**: January 2025  
**Version**: 1.0.0  
**Status**: Production Ready ✅
