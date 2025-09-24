# LLM Rubric Scoring API with Google Gemini Integration

## Deprecated Folder Structure

This folder contains the complete implementation of the LLM Rubric Scoring API with Google Gemini AI integration for evaluating student submissions.

```
Deprecated/
├── README.md                    # This overview file
├── app.py                       # Main Flask application with Gemini integration
├── requirements.txt             # Python dependencies (includes Gemini)
├── API_README.md               # Comprehensive API documentation
├── test_app.py                 # Unit tests for the API
├── gemini_model_integration.py # Google Gemini AI integration module
└── GEMINI_INTEGRATION_GUIDE.md # Complete Gemini setup and usage guide
```

## Quick Start

### 1. Install Dependencies
```bash
cd Deprecated
pip install -r requirements.txt
```

### 2. Set up Google AI API Key (Optional)
```bash
export GOOGLE_AI_API_KEY="your-api-key-here"
```

### 3. Run the API Server
```bash
python app.py
```
The server will start on `http://localhost:5001`

### 4. Test the API
```bash
# Run unit tests
python test_app.py
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
- **`GEMINI_INTEGRATION_GUIDE.md`** - Complete Gemini setup and usage guide
- **`test_app.py`** - Comprehensive test suite
- **`gemini_model_integration.py`** - Gemini AI integration module

## Google Gemini Integration

- **Gemini AI**: Uses Google's Gemini-1.5-flash model for intelligent evaluation
- **Intelligent Fallback**: Automatically falls back to mock evaluation when Gemini is unavailable
- **Production Ready**: Includes input validation, error handling, and logging
- **Comprehensive Prompting**: Detailed prompts for consistent rubric scoring

## Features

- **AI-Powered Evaluation**: Real AI evaluation using Google Gemini
- **Robust Fallback**: Seamless fallback to mock evaluation
- **Safety Settings**: Configured for educational content
- **Error Handling**: Graceful error handling with detailed logging

## Usage Example

```python
import requests

# Evaluate a student submission
response = requests.post('http://localhost:5001/llm/rubric-score', 
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

Run tests with: `python test_app.py`

---

**Status**: Ready for development and testing  
**Version**: 1.0.0  
**Last Updated**: January 2025