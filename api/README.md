# LLM Rubric Scoring API

## API Folder Structure

This folder contains the complete implementation of the LLM Rubric Scoring API for evaluating student submissions.

```
api/
├── README.md              # This overview file
├── app.py                 # Main Flask application with API endpoints
├── requirements.txt       # Python dependencies
├── API_README.md         # Comprehensive API documentation
└── test_and_demo.py      # Combined unit tests and integration demo
```

## Quick Start

### 1. Install Dependencies
```bash
cd api
pip install -r requirements.txt
```

### 2. Run the API Server
```bash
python app.py
```
The server will start on `http://localhost:5000`

### 3. Test the API
```bash
# Run unit tests (no server needed)
python test_and_demo.py

# Run integration tests (server must be running)
python app.py &                    # Start server in background
python test_and_demo.py --integration
```

## API Endpoints

### Main Endpoint
- **POST** `/llm/rubric-score` - Evaluate student submissions

### Utility Endpoints
- **GET** `/health` - Health check
- **GET** `/rubric-info` - Get rubric information

## What This API Does

The API evaluates student submissions across four rubric categories:
- **Structure** - Organization and logical flow
- **Clarity** - Language clarity and understandability  
- **Relevance** - Content relevance to the prompt
- **Academic_Writing** - Academic tone and standards

Each category receives a score: **Excellent**, **Good**, **Fair**, or **Poor**.

## Documentation

- **`API_README.md`** - Complete API documentation with examples
- **`test_and_demo.py`** - Combined unit tests and integration demo

## Current Implementation

- **Mock LLM**: Currently uses simple scoring logic for demonstration
- **Ready for Integration**: Easy to replace with actual LLM API calls
- **Production Ready**: Includes input validation, error handling, and logging

## Next Steps

1. **Replace Mock LLM**: Integrate with actual LLM providers (OpenAI, Anthropic, etc.)
2. **Custom Rubrics**: Allow dynamic rubric configuration
3. **Batch Processing**: Evaluate multiple submissions at once
4. **Confidence Scores**: Add confidence levels to evaluations

## Usage Example

```python
import requests

# Evaluate a student submission
response = requests.post('http://localhost:5000/llm/rubric-score', 
    json={'student_submission': 'Your essay text here...'})

result = response.json()
print(f"Structure: {result['Structure']}")
print(f"Clarity: {result['Clarity']}")
```

## Testing

The API includes comprehensive tests covering:
- Successful evaluations
- Input validation
- Error handling
- Edge cases
- Response format validation

Run tests with: `python test_and_demo.py`

---

**Status**: Ready for development and testing  
**Version**: 1.0.0  
**Last Updated**: January 2025