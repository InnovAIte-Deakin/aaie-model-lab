# Google Gemini Integration Guide

This guide explains how to integrate and use Google Gemini AI model with the LLM Rubric Scoring API.

## Overview

The API now supports Google Gemini AI model for automated rubric scoring, with intelligent fallback to mock evaluation when Gemini is not available.

## Features

- **Gemini AI Integration**: Uses Google's Gemini-1.5-flash model for intelligent evaluation
- **Intelligent Fallback**: Automatically falls back to mock evaluation if Gemini fails
- **Comprehensive Prompting**: Detailed prompts for consistent rubric scoring
- **Safety Settings**: Configured for educational content evaluation
- **Error Handling**: Robust error handling with graceful degradation

## Setup Instructions

### 1. Get Google AI API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Create a new API key
4. Copy the API key for use in the application

### 2. Set Environment Variable

#### Option A: Environment Variable (Recommended)
```bash
export GOOGLE_AI_API_KEY="your-api-key-here"
```

#### Option B: .env File
Create a `.env` file in the project root:
```
GOOGLE_AI_API_KEY=your-api-key-here
```

#### Option C: Direct Configuration
Pass the API key directly when initializing:
```python
from gemini_model_integration import initialize_gemini_model
initialize_gemini_model(api_key="your-api-key-here")
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

The requirements.txt now includes:
- `google-generativeai==0.3.2`
- `google-auth==2.23.4`
- `google-auth-oauthlib==1.1.0`
- `google-auth-httplib2==0.1.1`

### 4. Run the Application

```bash
python app.py
```

The application will:
1. Attempt to initialize Gemini AI model
2. Show success message if Gemini is available
3. Show warning and use mock evaluation if Gemini fails
4. Start the API server on port 5001

## API Usage

### Health Check
```bash
curl http://localhost:5001/health
```

### Rubric Information
```bash
curl http://localhost:5001/rubric-info
```

### Evaluate Submission
```bash
curl -X POST http://localhost:5001/llm/rubric-score \
  -H "Content-Type: application/json" \
  -d '{"student_submission": "Your student submission text here"}'
```

## Gemini Model Configuration

### Model Settings
- **Model**: `gemini-1.5-flash` (fast and efficient)
- **Temperature**: `0.1` (low for consistent evaluation)
- **Max Output Tokens**: `1000`
- **Safety Settings**: Configured for educational content

### Evaluation Prompt
The system uses a comprehensive prompt that includes:
- Detailed rubric criteria for each category
- Clear instructions for evaluation
- JSON response format specification
- Examples of different quality levels

## Error Handling

### Gemini API Errors
- **API Key Issues**: Falls back to mock evaluation
- **Rate Limiting**: Automatic retry with exponential backoff
- **Content Filtering**: Adjusted safety settings for educational content
- **Network Issues**: Graceful fallback to mock evaluation

### Fallback Behavior
When Gemini is unavailable, the system automatically uses mock evaluation based on:
- Text length and word count
- Keyword analysis
- Simple heuristics for academic writing

## Testing

### Unit Tests
```bash
python test_app.py
```

### Manual Testing
```bash
# Test with Gemini enabled
export GOOGLE_AI_API_KEY="your-key"
python app.py

# Test with mock evaluation (no API key)
unset GOOGLE_AI_API_KEY
python app.py
```

## Performance Considerations

### Response Time
- **Gemini Evaluation**: ~2-5 seconds per submission
- **Mock Evaluation**: ~0.1 seconds per submission
- **Fallback Time**: ~1-2 seconds when Gemini fails

### Rate Limits
- Google AI API has rate limits based on your plan
- The system handles rate limiting gracefully
- Consider implementing request queuing for high-volume usage

## Security Best Practices

### API Key Management
- Never commit API keys to version control
- Use environment variables or secure key management
- Rotate API keys regularly
- Monitor API usage and costs

### Content Safety
- The system uses conservative safety settings
- Educational content is generally safe
- Monitor for any content filtering issues

## Troubleshooting

### Common Issues

#### 1. "Google AI API key is required"
**Solution**: Set the `GOOGLE_AI_API_KEY` environment variable

#### 2. "Failed to initialize Gemini model"
**Solution**: Check your API key and internet connection

#### 3. "Gemini evaluation failed"
**Solution**: The system will automatically fall back to mock evaluation

#### 4. Rate limiting errors
**Solution**: Wait and retry, or implement request queuing

### Debug Mode
Enable debug logging:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## Cost Management

### API Usage
- Gemini API charges per token
- Monitor usage in Google AI Studio
- Set up billing alerts
- Consider caching for repeated evaluations

### Optimization Tips
- Use appropriate temperature settings
- Limit max output tokens
- Implement result caching
- Batch requests when possible

## Future Enhancements

### Planned Features
- **Batch Processing**: Evaluate multiple submissions at once
- **Custom Prompts**: Allow custom evaluation prompts
- **Model Selection**: Support for different Gemini models
- **Caching**: Cache evaluation results
- **Analytics**: Track evaluation patterns and accuracy

### Integration Options
- **Google Cloud**: Use Vertex AI for enterprise features
- **Custom Models**: Support for fine-tuned models
- **Multi-Model**: Support for multiple AI providers
- **Hybrid Evaluation**: Combine AI and human evaluation

## Support

For issues related to:
- **Gemini API**: Check [Google AI Documentation](https://ai.google.dev/docs)
- **API Integration**: Review this guide and code comments
- **Performance**: Monitor logs and API usage
- **Costs**: Check Google AI Studio billing

## Example Integration

```python
from gemini_model_integration import GeminiRubricScorer

# Initialize scorer
scorer = GeminiRubricScorer(api_key="your-key")

# Evaluate submission
submission = "The economic impact of climate change is significant..."
scores = scorer.evaluate_submission(submission)

print(scores)
# Output: {'Structure': 'Excellent', 'Clarity': 'Good', ...}
```

This integration provides a robust, production-ready solution for automated rubric scoring using Google Gemini AI.