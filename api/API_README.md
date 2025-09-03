# LLM Rubric Scoring API

## Overview
This API provides automated evaluation of student submissions using rubric categories. The main endpoint `/llm/rubric-score` evaluates student work and returns scores across four key dimensions: Structure, Clarity, Relevance, and Academic Writing.

## API Endpoints

### 1. POST /llm/rubric-score
**Main endpoint for evaluating student submissions**

#### Request
- **Method**: POST
- **Content-Type**: application/json
- **Body**:
```json
{
    "student_submission": "The student's submission text here..."
}
```

#### Response
**Success (200)**:
```json
{
    "Structure": "Excellent",
    "Clarity": "Good", 
    "Relevance": "Excellent",
    "Academic_Writing": "Good"
}
```

**Error (400)**:
```json
{
    "error": "Student submission text is required",
    "status": "error"
}
```

**Error (500)**:
```json
{
    "error": "Internal server error during evaluation",
    "status": "error"
}
```

### 2. GET /health
**Health check endpoint**

**Response**:
```json
{
    "status": "healthy",
    "service": "LLM Rubric Scoring API",
    "version": "1.0.0"
}
```

### 3. GET /rubric-info
**Get information about rubric categories and criteria**

**Response**:
```json
{
    "status": "success",
    "rubric_categories": {
        "Structure": ["Excellent", "Good", "Fair", "Poor"],
        "Clarity": ["Excellent", "Good", "Fair", "Poor"],
        "Relevance": ["Excellent", "Good", "Fair", "Poor"],
        "Academic_Writing": ["Excellent", "Good", "Fair", "Poor"]
    },
    "rubric_criteria": {
        "Structure": {
            "Excellent": "Clear organization with logical flow...",
            "Good": "Generally well-organized...",
            "Fair": "Basic organization present...",
            "Poor": "Poorly organized..."
        }
        // ... other categories
    }
}
```

## Rubric Categories and Criteria

### Structure
- **Excellent**: Clear organization with logical flow, well-developed introduction and conclusion, coherent paragraph structure
- **Good**: Generally well-organized with clear structure, some minor organizational issues
- **Fair**: Basic organization present but may lack logical flow or clear structure
- **Poor**: Poorly organized, lacks clear structure, difficult to follow

### Clarity
- **Excellent**: Crystal clear language, easy to understand, well-articulated ideas
- **Good**: Clear language with minor areas that could be clarified
- **Fair**: Generally clear but some parts may be confusing
- **Poor**: Often unclear, difficult to understand, confusing language

### Relevance
- **Excellent**: Directly addresses the prompt/question, highly relevant content throughout
- **Good**: Mostly relevant to the prompt, some minor digressions
- **Fair**: Generally relevant but may have some off-topic content
- **Poor**: Often off-topic, lacks relevance to the main question/prompt

### Academic Writing
- **Excellent**: Professional academic tone, appropriate vocabulary, proper citations if needed
- **Good**: Good academic tone with minor informal elements
- **Fair**: Mixed academic and informal language, some inappropriate elements
- **Poor**: Inappropriate tone, overly informal, lacks academic standards

## Example Usage

### cURL Example
```bash
curl -X POST http://localhost:5000/llm/rubric-score \
  -H "Content-Type: application/json" \
  -d '{
    "student_submission": "The economic impact of climate change is significant because it affects multiple sectors including agriculture, infrastructure, and public health. Rising temperatures lead to reduced crop yields, increased infrastructure damage from extreme weather events, and higher healthcare costs due to heat-related illnesses. These factors create a complex web of economic consequences that require comprehensive policy responses."
  }'
```

### Python Example
```python
import requests
import json

url = "http://localhost:5000/llm/rubric-score"
data = {
    "student_submission": "The economic impact of climate change is significant because it affects multiple sectors including agriculture, infrastructure, and public health. Rising temperatures lead to reduced crop yields, increased infrastructure damage from extreme weather events, and higher healthcare costs due to heat-related illnesses. These factors create a complex web of economic consequences that require comprehensive policy responses."
}

response = requests.post(url, json=data)
result = response.json()

print("Evaluation Results:")
for category, score in result.items():
    print(f"{category}: {score}")
```

### JavaScript Example
```javascript
const evaluateSubmission = async (submission) => {
    try {
        const response = await fetch('http://localhost:5000/llm/rubric-score', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                student_submission: submission
            })
        });
        
        const result = await response.json();
        return result;
    } catch (error) {
        console.error('Error:', error);
    }
};

// Usage
const submission = "The economic impact of climate change is significant...";
evaluateSubmission(submission).then(result => {
    console.log('Evaluation:', result);
});
```

## Input Validation

The API validates the following:
- **Required field**: `student_submission` must be provided
- **Data type**: Must be a string
- **Length**: Maximum 10KB (10,000 characters)
- **Content**: Cannot be empty or whitespace-only

## Error Handling

### Common Error Codes
- **400 Bad Request**: Invalid input (missing text, wrong format, too long)
- **500 Internal Server Error**: Server-side processing error

### Error Response Format
```json
{
    "error": "Description of the error",
    "status": "error"
}
```

## Setup and Installation

### Prerequisites
- Python 3.8+
- pip

### Installation
1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python app.py
   ```

### Environment Variables
- `PORT`: Server port (default: 5000)

## Current Implementation Notes

### LLM Integration
- **Current**: Mock implementation with simple scoring logic
- **Future**: Replace `mock_llm_evaluation()` function with actual LLM API calls
- **Integration**: Can easily integrate with OpenAI GPT, Anthropic Claude, or other LLM providers

### Scoring Logic
The current mock implementation uses:
- Text length (word count)
- Content analysis (keyword presence)
- Basic heuristics for demonstration

Replace with actual LLM prompts and evaluation logic for production use.

## Testing

### Manual Testing
1. Start the server: `python app.py`
2. Use the provided examples above
3. Test with various submission lengths and content

### Automated Testing
```bash
# Install pytest
pip install pytest

# Run tests
pytest test_app.py
```

## Future Enhancements

1. **Real LLM Integration**: Connect to actual LLM APIs
2. **Custom Rubrics**: Allow dynamic rubric configuration
3. **Batch Processing**: Evaluate multiple submissions at once
4. **Confidence Scores**: Add confidence levels to evaluations
5. **Detailed Feedback**: Provide specific improvement suggestions
6. **Analytics**: Track evaluation patterns and performance

## Support

For questions or issues, please refer to the project documentation or contact the development team.
