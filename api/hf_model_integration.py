#!/usr/bin/env python3
"""
Hugging Face Model Integration for Rubric Scoring
This module integrates Hugging Face models for student submission evaluation
"""

import torch
from transformers import (
    AutoTokenizer, 
    AutoModelForSequenceClassification,
    pipeline
)
import logging
from typing import Dict, Any, List
import os

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class HFRubricScorer:
    """
    Hugging Face model-based rubric scorer for student submissions
    """
    
    def __init__(self, model_name: str = "microsoft/DialoGPT-medium"):
        """
        Initialize the HF model for rubric scoring
        
        Args:
            model_name (str): Hugging Face model identifier
        """
        self.model_name = model_name
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.tokenizer = None
        self.model = None
        self.classifier = None
        
        logger.info(f"Initializing HF model: {model_name}")
        logger.info(f"Using device: {self.device}")
        
    def load_model(self):
        """Load the Hugging Face model and tokenizer"""
        try:
            logger.info("Loading tokenizer...")
            self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
            
            logger.info("Loading model...")
            self.model = AutoModelForSequenceClassification.from_pretrained(
                self.model_name,
                num_labels=4,  # 4 rubric categories
                torch_dtype=torch.float16 if self.device == "cuda" else torch.float32
            )
            
            # Create classification pipeline
            self.classifier = pipeline(
                "text-classification",
                model=self.model,
                tokenizer=self.tokenizer,
                device=0 if self.device == "cuda" else -1
            )
            
            logger.info("Model loaded successfully!")
            return True
            
        except Exception as e:
            logger.error(f"Error loading model: {str(e)}")
            return False
    
    def evaluate_submission(self, student_submission: str) -> Dict[str, str]:
        """
        Evaluate student submission using HF model
        
        Args:
            student_submission (str): The student's submission text
            
        Returns:
            Dict[str, str]: Rubric scores for each category
        """
        if not self.classifier:
            logger.error("Model not loaded. Call load_model() first.")
            return self._get_fallback_scores()
        
        try:
            # Prepare text for evaluation
            evaluation_text = self._prepare_evaluation_text(student_submission)
            
            # Get predictions for each rubric category
            scores = {}
            
            for category in ["Structure", "Clarity", "Relevance", "Academic_Writing"]:
                category_text = f"Evaluate {category}: {evaluation_text}"
                
                # Get prediction from HF model
                result = self.classifier(category_text)
                
                # Convert prediction to rubric score
                score = self._convert_prediction_to_score(result, category)
                scores[category] = score
                
                logger.info(f"{category}: {score}")
            
            return scores
            
        except Exception as e:
            logger.error(f"Error during evaluation: {str(e)}")
            return self._get_fallback_scores()
    
    def _prepare_evaluation_text(self, submission: str) -> str:
        """
        Prepare submission text for model evaluation
        
        Args:
            submission (str): Raw submission text
            
        Returns:
            str: Prepared text for evaluation
        """
        # Clean and prepare text
        text = submission.strip()
        
        # Truncate if too long (HF models have token limits)
        max_length = 512
        if len(text) > max_length:
            text = text[:max_length] + "..."
        
        return text
    
    def _convert_prediction_to_score(self, prediction: List[Dict], category: str) -> str:
        """
        Convert HF model prediction to rubric score
        
        Args:
            prediction (List[Dict]): HF model prediction
            category (str): Rubric category being evaluated
            
        Returns:
            str: Rubric score (Excellent, Good, Fair, Poor)
        """
        try:
            # Extract confidence score
            confidence = prediction[0]['score']
            
            # Convert confidence to rubric score
            if confidence > 0.8:
                return "Excellent"
            elif confidence > 0.6:
                return "Good"
            elif confidence > 0.4:
                return "Fair"
            else:
                return "Poor"
                
        except Exception as e:
            logger.error(f"Error converting prediction: {str(e)}")
            return "Fair"  # Default fallback
    
    def _get_fallback_scores(self) -> Dict[str, str]:
        """
        Get fallback scores when model fails
        
        Returns:
            Dict[str, str]: Default rubric scores
        """
        return {
            "Structure": "Fair",
            "Clarity": "Fair", 
            "Relevance": "Fair",
            "Academic_Writing": "Fair"
        }
    
    def get_model_info(self) -> Dict[str, Any]:
        """
        Get information about the loaded model
        
        Returns:
            Dict[str, Any]: Model information
        """
        return {
            "model_name": self.model_name,
            "device": self.device,
            "is_loaded": self.classifier is not None,
            "model_type": "Hugging Face Transformers"
        }


# Alternative implementation using a simpler approach
class SimpleHFRubricScorer:
    """
    Simplified HF model integration for rubric scoring
    Uses a pre-trained model for text classification
    """
    
    def __init__(self, model_name: str = "distilbert-base-uncased"):
        self.model_name = model_name
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.classifier = None
        
    def load_model(self):
        """Load a simple classification model"""
        try:
            from transformers import pipeline
            
            self.classifier = pipeline(
                "text-classification",
                model=self.model_name,
                device=0 if self.device == "cuda" else -1
            )
            logger.info(f"Simple HF model loaded: {self.model_name}")
            return True
        except Exception as e:
            logger.error(f"Error loading simple model: {str(e)}")
            return False
    
    def evaluate_submission(self, student_submission: str) -> Dict[str, str]:
        """
        Evaluate submission using simple HF model
        """
        if not self.classifier:
            return self._get_fallback_scores()
        
        try:
            # Simple evaluation based on text characteristics
            text_length = len(student_submission.split())
            
            # Use HF model to get overall sentiment/quality score
            result = self.classifier(student_submission[:512])  # Truncate for token limit
            confidence = result[0]['score']
            
            # Map to rubric scores based on confidence and text characteristics
            if confidence > 0.7 and text_length > 50:
                base_score = "Excellent"
            elif confidence > 0.5 and text_length > 30:
                base_score = "Good"
            elif confidence > 0.3 and text_length > 15:
                base_score = "Fair"
            else:
                base_score = "Poor"
            
            # Return scores for all categories (simplified approach)
            return {
                "Structure": base_score,
                "Clarity": base_score,
                "Relevance": base_score,
                "Academic_Writing": base_score
            }
            
        except Exception as e:
            logger.error(f"Error in simple evaluation: {str(e)}")
            return self._get_fallback_scores()
    
    def _get_fallback_scores(self) -> Dict[str, str]:
        """Fallback scores when model fails"""
        return {
            "Structure": "Fair",
            "Clarity": "Fair",
            "Relevance": "Fair", 
            "Academic_Writing": "Fair"
        }


# Factory function to create appropriate scorer
def create_hf_scorer(model_type: str = "simple", model_name: str = None) -> Any:
    """
    Factory function to create HF scorer instance
    
    Args:
        model_type (str): Type of scorer ("simple" or "advanced")
        model_name (str): Specific model name to use
        
    Returns:
        HFRubricScorer or SimpleHFRubricScorer instance
    """
    if model_type == "simple":
        model_name = model_name or "distilbert-base-uncased"
        return SimpleHFRubricScorer(model_name)
    else:
        model_name = model_name or "microsoft/DialoGPT-medium"
        return HFRubricScorer(model_name)


if __name__ == "__main__":
    # Test the HF integration
    print("Testing Hugging Face Model Integration...")
    
    # Test simple scorer
    scorer = create_hf_scorer("simple")
    if scorer.load_model():
        test_submission = "This is a well-structured essay about climate change and its economic impacts."
        scores = scorer.evaluate_submission(test_submission)
        print(f"Test scores: {scores}")
    else:
        print("Failed to load model")
