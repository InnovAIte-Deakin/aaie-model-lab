from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
from typing import Dict, Any
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# Rubric categories and their possible labels
RUBRIC_CATEGORIES = {
    "Structure": ["Excellent", "Good", "Fair", "Poor"],
    "Clarity": ["Excellent", "Good", "Fair", "Poor"],
    "Relevance": ["Excellent", "Good", "Fair", "Poor"],
    "Academic_Writing": ["Excellent", "Good", "Fair", "Poor"]
}

# Rubric criteria definitions for each category
RUBRIC_CRITERIA = {
    "Structure": {
        "Excellent": "Clear organization with logical flow, well-developed introduction and conclusion, coherent paragraph structure",
        "Good": "Generally well-organized with clear structure, some minor organizational issues",
        "Fair": "Basic organization present but may lack logical flow or clear structure",
        "Poor": "Poorly organized, lacks clear structure, difficult to follow"
    },
    "Clarity": {
        "Excellent": "Crystal clear language, easy to understand, well-articulated ideas",
        "Good": "Clear language with minor areas that could be clarified",
        "Fair": "Generally clear but some parts may be confusing",
        "Poor": "Often unclear, difficult to understand, confusing language"
    },
    "Relevance": {
        "Excellent": "Directly addresses the prompt/question, highly relevant content throughout",
        "Good": "Mostly relevant to the prompt, some minor digressions",
        "Fair": "Generally relevant but may have some off-topic content",
        "Poor": "Often off-topic, lacks relevance to the main question/prompt"
    },
    "Academic_Writing": {
        "Excellent": "Professional academic tone, appropriate vocabulary, proper citations if needed",
        "Good": "Good academic tone with minor informal elements",
        "Fair": "Mixed academic and informal language, some inappropriate elements",
        "Poor": "Inappropriate tone, overly informal, lacks academic standards"
    }
}

def mock_llm_evaluation(student_submission: str) -> Dict[str, str]:
    """
    Mock LLM evaluation function that returns rubric scores.
    In a real implementation, this would call an actual LLM API.
    
    Args:
        student_submission (str): The student's submission text
        
    Returns:
        Dict[str, str]: Dictionary with rubric category scores
    """
    # This is a mock implementation (will replace with actual LLM API call)
    # For now, it returns a simple evaluation based on text length and content
    
    text_length = len(student_submission)
    word_count = len(student_submission.split())
    
    # Simple scoring logic (replace with actual LLM evaluation)
    if word_count > 50 and "because" in student_submission.lower() and "economic" in student_submission.lower():
        structure = "Excellent"
        clarity = "Good"
        relevance = "Excellent"
        academic_writing = "Good"
    elif word_count > 30 and ("climate" in student_submission.lower() or "economic" in student_submission.lower()):
        structure = "Good"
        clarity = "Good"
        relevance = "Good"
        academic_writing = "Fair"
    elif word_count > 15:
        structure = "Fair"
        clarity = "Fair"
        relevance = "Fair"
        academic_writing = "Fair"
    else:
        structure = "Poor"
        clarity = "Poor"
        relevance = "Poor"
        academic_writing = "Poor"
    
    return {
        "Structure": structure,
        "Clarity": clarity,
        "Relevance": relevance,
        "Academic_Writing": academic_writing
    }

def validate_input(student_submission: str) -> Dict[str, Any]:
    """
    Validate the input student submission.
    
    Args:
        student_submission (str): The student's submission text
        
    Returns:
        Dict[str, Any]: Validation result with success status and any error messages
    """
    if not student_submission:
        return {"valid": False, "error": "Student submission text is required"}
    
    if not isinstance(student_submission, str):
        return {"valid": False, "error": "Student submission must be a string"}
    
    if len(student_submission.strip()) == 0:
        return {"valid": False, "error": "Student submission cannot be empty"}
    
    if len(student_submission) > 10000:  # 10KB limit
        return {"valid": False, "error": "Student submission is too long (max 10KB)"}
    
    return {"valid": True}

@app.route('/llm/rubric-score', methods=['POST'])
def evaluate_submission():
    """
    POST endpoint to evaluate a student submission using rubric categories.
    
    Expected JSON input:
    {
        "student_submission": "The student's submission text here..."
    }
    
    Returns:
    {
        "Structure": "Excellent|Good|Fair|Poor",
        "Clarity": "Excellent|Good|Fair|Poor", 
        "Relevance": "Excellent|Good|Fair|Poor",
        "Academic_Writing": "Excellent|Good|Fair|Poor"
    }
    """
    try:
        # Get JSON data from request
        data = request.get_json()
        
        if not data:
            return jsonify({
                "error": "No JSON data provided",
                "status": "error"
            }), 400
        
        # Extract student submission
        student_submission = data.get('student_submission')
        
        # Validate input
        validation = validate_input(student_submission)
        if not validation["valid"]:
            return jsonify({
                "error": validation["error"],
                "status": "error"
            }), 400
        
        # Log the evaluation request
        logger.info(f"Evaluating submission of length: {len(student_submission)} characters")
        
        # Call LLM evaluation (currently mocked)
        rubric_scores = mock_llm_evaluation(student_submission)
        
        # Log the evaluation results
        logger.info(f"Evaluation completed: {rubric_scores}")
        
        # Return the rubric scores in the exact format requested
        return jsonify(rubric_scores), 200
        
    except Exception as e:
        logger.error(f"Error in evaluation endpoint: {str(e)}")
        return jsonify({
            "error": "Internal server error during evaluation",
            "status": "error"
        }), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({
        "status": "healthy",
        "service": "LLM Rubric Scoring API",
        "version": "1.0.0"
    }), 200

@app.route('/rubric-info', methods=['GET'])
def get_rubric_info():
    """Get information about the rubric categories and criteria."""
    return jsonify({
        "status": "success",
        "rubric_categories": RUBRIC_CATEGORIES,
        "rubric_criteria": RUBRIC_CRITERIA
    }), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
