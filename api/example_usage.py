#!/usr/bin/env python3
"""
Example usage script for the LLM Rubric Scoring API
This script demonstrates how to interact with the API endpoints
"""

import requests
import json
import time

# API base URL
BASE_URL = "http://localhost:5000"

def test_health_check():
    """Test the health check endpoint"""
    print("Testing Health Check...")
    try:
        response = requests.get(f"{BASE_URL}/health")
        if response.status_code == 200:
            data = response.json()
            print(f"Health Check: {data['status']}")
            print(f"   Service: {data['service']}")
            print(f"   Version: {data['version']}")
        else:
            print(f"Health Check Failed: {response.status_code}")
    except requests.exceptions.ConnectionError:
        print("Cannot connect to API. Make sure the server is running.")
        return False
    return True

def test_rubric_info():
    """Test the rubric info endpoint"""
    print("\nTesting Rubric Info...")
    try:
        response = requests.get(f"{BASE_URL}/rubric-info")
        if response.status_code == 200:
            data = response.json()
            print("Rubric Info Retrieved Successfully")
            print(f"   Categories: {', '.join(data['rubric_categories'].keys())}")
            print(f"   Rating Scale: {data['rubric_categories']['Structure']}")
        else:
            print(f"Rubric Info Failed: {response.status_code}")
    except Exception as e:
        print(f"Error getting rubric info: {e}")
    return True

def evaluate_submission(submission_text, description):
    """Evaluate a student submission using the API"""
    print(f"\nEvaluating: {description}")
    print(f"   Text: {submission_text[:100]}{'...' if len(submission_text) > 100 else ''}")
    
    try:
        response = requests.post(
            f"{BASE_URL}/llm/rubric-score",
            json={"student_submission": submission_text},
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            data = response.json()
            print("Evaluation Successful")
            print("   Results:")
            for category, score in data.items():
                print(f"     {category}: {score}")
        else:
            print(f"Evaluation Failed: {response.status_code}")
            error_data = response.json()
            print(f"   Error: {error_data.get('error', 'Unknown error')}")
            
    except Exception as e:
        print(f"Error during evaluation: {e}")

def test_various_submissions():
    """Test the API with various types of student submissions"""
    print("\nTesting Various Submissions...")
    
    # Test 1: Excellent submission
    excellent_submission = """
    The economic impact of climate change is significant because it affects multiple sectors 
    including agriculture, infrastructure, and public health. Rising temperatures lead to 
    reduced crop yields, increased infrastructure damage from extreme weather events, and 
    higher healthcare costs due to heat-related illnesses. These factors create a complex 
    web of economic consequences that require comprehensive policy responses.
    """
    evaluate_submission(excellent_submission, "Excellent Academic Essay")
    
    # Test 2: Good submission
    good_submission = """
    Climate change has economic effects on agriculture and infrastructure. 
    Higher temperatures reduce crop yields and damage buildings. This costs money 
    and affects people's health. We need policies to address these problems.
    """
    evaluate_submission(good_submission, "Good Academic Essay")
    
    # Test 3: Fair submission
    fair_submission = """
    Climate change affects the economy. It impacts farming and buildings. 
    Crops don't grow as well. Buildings get damaged. This costs money.
    """
    evaluate_submission(fair_submission, "Fair Academic Essay")
    
    # Test 4: Poor submission
    poor_submission = "Climate change bad. Economy hurt."
    evaluate_submission(poor_submission, "Poor Academic Essay")
    
    # Test 5: Empty submission (should fail)
    print("\nTesting Error Handling...")
    evaluate_submission("", "Empty Submission (Should Fail)")

def main():
    """Main function to run all tests"""
    print("LLM Rubric Scoring API - Example Usage")
    print("=" * 50)
    
    # Check if API is running
    if not test_health_check():
        print("\nTo start the API server, run: python app.py")
        return
    
    # Test rubric info
    test_rubric_info()
    
    # Test various submissions
    test_various_submissions()
    
    print("\nExample usage completed!")
    print("\nTo run the tests, use: python test_app.py")

if __name__ == "__main__":
    main()
