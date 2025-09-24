#!/usr/bin/env python3
"""
Google Gemini Model Integration for LLM Rubric Scoring API
This module provides integration with Google's Gemini AI model for automated rubric scoring.
"""

import os
import json
import logging
from typing import Dict, Any, Optional
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold

# Configure logging
logger = logging.getLogger(__name__)

class GeminiRubricScorer:
    """
    A class to handle rubric scoring using Google Gemini AI model.
    """
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the Gemini Rubric Scorer.
        
        Args:
            api_key (str, optional): Google AI API key. If not provided, will try to get from environment.
        """
        self.api_key = api_key or os.getenv('GOOGLE_AI_API_KEY')
        if not self.api_key:
            raise ValueError("Google AI API key is required. Set GOOGLE_AI_API_KEY environment variable or pass api_key parameter.")
        
        # Configure the Gemini API
        genai.configure(api_key=self.api_key)
        
        # Initialize the model
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Configure safety settings to be more permissive for educational content
        self.safety_settings = {
            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
        }
        
        logger.info("Gemini Rubric Scorer initialized successfully")
    
    def create_evaluation_prompt(self, student_submission: str) -> str:
        """
        Create a comprehensive prompt for evaluating student submissions.
        
        Args:
            student_submission (str): The student's submission text
            
        Returns:
            str: Formatted prompt for the Gemini model
        """
        prompt = f"""
You are an expert academic evaluator tasked with scoring student submissions using a comprehensive rubric. Please evaluate the following student submission across four key categories: Structure, Clarity, Relevance, and Academic Writing.

**Student Submission:**
{student_submission}

**Evaluation Criteria:**

1. **Structure** (Excellent/Good/Fair/Poor):
   - Excellent: Clear organization with logical flow, well-developed introduction and conclusion, coherent paragraph structure
   - Good: Generally well-organized with clear structure, some minor organizational issues
   - Fair: Basic organization present but may lack logical flow or clear structure
   - Poor: Poorly organized, lacks clear structure, difficult to follow

2. **Clarity** (Excellent/Good/Fair/Poor):
   - Excellent: Crystal clear language, easy to understand, well-articulated ideas
   - Good: Clear language with minor areas that could be clarified
   - Fair: Generally clear but some parts may be confusing
   - Poor: Often unclear, difficult to understand, confusing language

3. **Relevance** (Excellent/Good/Fair/Poor):
   - Excellent: Directly addresses the prompt/question, highly relevant content throughout
   - Good: Mostly relevant to the prompt, some minor digressions
   - Fair: Generally relevant but may have some off-topic content
   - Poor: Often off-topic, lacks relevance to the main question/prompt

4. **Academic Writing** (Excellent/Good/Fair/Poor):
   - Excellent: Professional academic tone, appropriate vocabulary, proper citations if needed
   - Good: Good academic tone with minor informal elements
   - Fair: Mixed academic and informal language, some inappropriate elements
   - Poor: Inappropriate tone, overly informal, lacks academic standards

**Instructions:**
- Read the student submission carefully
- Evaluate each category independently
- Consider the overall quality and coherence of the submission
- Provide constructive feedback based on the rubric criteria
- Return your evaluation in the following JSON format:

{{
    "Structure": "Excellent|Good|Fair|Poor",
    "Clarity": "Excellent|Good|Fair|Poor",
    "Relevance": "Excellent|Good|Fair|Poor",
    "Academic_Writing": "Excellent|Good|Fair|Poor",
    "reasoning": "Brief explanation of your evaluation rationale"
}}

Please provide your evaluation now:
"""
        return prompt
    
    def evaluate_submission(self, student_submission: str) -> Dict[str, str]:
        """
        Evaluate a student submission using Gemini AI model.
        
        Args:
            student_submission (str): The student's submission text
            
        Returns:
            Dict[str, str]: Dictionary with rubric category scores
        """
        try:
            # Create the evaluation prompt
            prompt = self.create_evaluation_prompt(student_submission)
            
            # Generate response from Gemini
            response = self.model.generate_content(
                prompt,
                safety_settings=self.safety_settings,
                generation_config=genai.types.GenerationConfig(
                    temperature=0.1,  # Low temperature for consistent evaluation
                    max_output_tokens=1000,
                )
            )
            
            # Extract the response text
            response_text = response.text.strip()
            
            # Try to parse JSON response
            try:
                # Look for JSON in the response
                start_idx = response_text.find('{')
                end_idx = response_text.rfind('}') + 1
                
                if start_idx != -1 and end_idx != 0:
                    json_str = response_text[start_idx:end_idx]
                    result = json.loads(json_str)
                    
                    # Extract only the rubric scores (remove reasoning if present)
                    rubric_scores = {
                        "Structure": result.get("Structure", "Fair"),
                        "Clarity": result.get("Clarity", "Fair"),
                        "Relevance": result.get("Relevance", "Fair"),
                        "Academic_Writing": result.get("Academic_Writing", "Fair")
                    }
                    
                    # Validate scores
                    valid_scores = ["Excellent", "Good", "Fair", "Poor"]
                    for category, score in rubric_scores.items():
                        if score not in valid_scores:
                            logger.warning(f"Invalid score '{score}' for {category}, defaulting to 'Fair'")
                            rubric_scores[category] = "Fair"
                    
                    logger.info(f"Gemini evaluation completed successfully: {rubric_scores}")
                    return rubric_scores
                    
                else:
                    raise ValueError("No JSON found in response")
                    
            except (json.JSONDecodeError, ValueError) as e:
                logger.error(f"Failed to parse Gemini response as JSON: {e}")
                logger.error(f"Raw response: {response_text}")
                
                # Fallback: try to extract scores using text parsing
                return self._fallback_score_extraction(response_text)
                
        except Exception as e:
            logger.error(f"Error in Gemini evaluation: {str(e)}")
            # Return default scores on error
            return {
                "Structure": "Fair",
                "Clarity": "Fair", 
                "Relevance": "Fair",
                "Academic_Writing": "Fair"
            }
    
    def _fallback_score_extraction(self, response_text: str) -> Dict[str, str]:
        """
        Fallback method to extract scores from text response when JSON parsing fails.
        
        Args:
            response_text (str): The raw response text from Gemini
            
        Returns:
            Dict[str, str]: Dictionary with rubric category scores
        """
        logger.info("Using fallback score extraction method")
        
        # Default scores
        scores = {
            "Structure": "Fair",
            "Clarity": "Fair",
            "Relevance": "Fair", 
            "Academic_Writing": "Fair"
        }
        
        # Try to find scores in the text
        text_lower = response_text.lower()
        
        for category in scores.keys():
            category_lower = category.lower()
            if category_lower in text_lower:
                # Look for score words near the category
                category_idx = text_lower.find(category_lower)
                nearby_text = text_lower[max(0, category_idx-50):category_idx+100]
                
                if "excellent" in nearby_text:
                    scores[category] = "Excellent"
                elif "good" in nearby_text:
                    scores[category] = "Good"
                elif "poor" in nearby_text:
                    scores[category] = "Poor"
                # Fair is already the default
        
        logger.info(f"Fallback extraction result: {scores}")
        return scores

def create_gemini_scorer(api_key: Optional[str] = None) -> GeminiRubricScorer:
    """
    Factory function to create a Gemini Rubric Scorer instance.
    
    Args:
        api_key (str, optional): Google AI API key
        
    Returns:
        GeminiRubricScorer: Configured scorer instance
    """
    return GeminiRubricScorer(api_key=api_key)

# Global scorer instance (will be initialized when needed)
GEMINI_SCORER: Optional[GeminiRubricScorer] = None

def initialize_gemini_model(api_key: Optional[str] = None) -> bool:
    """
    Initialize the global Gemini model instance.
    
    Args:
        api_key (str, optional): Google AI API key
        
    Returns:
        bool: True if initialization successful, False otherwise
    """
    global GEMINI_SCORER
    
    try:
        GEMINI_SCORER = create_gemini_scorer(api_key)
        logger.info("Gemini model initialized successfully")
        return True
    except Exception as e:
        logger.error(f"Failed to initialize Gemini model: {str(e)}")
        return False

def get_gemini_scorer() -> Optional[GeminiRubricScorer]:
    """
    Get the global Gemini scorer instance.
    
    Returns:
        GeminiRubricScorer or None: The scorer instance if available
    """
    return GEMINI_SCORER
