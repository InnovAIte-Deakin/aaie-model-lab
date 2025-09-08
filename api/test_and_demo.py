#!/usr/bin/env python3
"""
Comprehensive test and demo script for the LLM Rubric Scoring API
This script combines unit testing and integration testing with real examples
"""

import unittest
import requests
import json
import time
from app import app

# API base URL for integration tests
BASE_URL = "http://localhost:5001"

class TestRubricScoringAPI(unittest.TestCase):
    """Unit tests using Flask test client (no server needed)"""
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        
    def test_health_check(self):
        """Test the health check endpoint"""
        response = self.app.get('/health')
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], 'healthy')
        self.assertEqual(data['service'], 'LLM Rubric Scoring API')
        
    def test_rubric_info(self):
        """Test the rubric info endpoint"""
        response = self.app.get('/rubric-info')
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], 'success')
        self.assertIn('rubric_categories', data)
        self.assertIn('rubric_criteria', data)
        
        # Check that all expected categories are present
        expected_categories = ['Structure', 'Clarity', 'Relevance', 'Academic_Writing']
        for category in expected_categories:
            self.assertIn(category, data['rubric_categories'])
            
    def test_evaluate_submission_success(self):
        """Test successful submission evaluation"""
        test_submission = "This is a well-structured essay about climate change. It clearly explains the economic impacts and provides relevant examples. The writing is academic and professional."
        
        response = self.app.post('/llm/rubric-score',
                               data=json.dumps({'student_submission': test_submission}),
                               content_type='application/json')
        
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 200)
        
        # Check that all rubric categories are present in the direct response
        expected_categories = ['Structure', 'Clarity', 'Relevance', 'Academic_Writing']
        for category in expected_categories:
            self.assertIn(category, data)
            self.assertIn(data[category], ['Excellent', 'Good', 'Fair', 'Poor'])
            
    def test_evaluate_submission_missing_text(self):
        """Test submission evaluation with missing text"""
        response = self.app.post('/llm/rubric-score',
                               data=json.dumps({}),
                               content_type='application/json')
        
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['status'], 'error')
        self.assertIn('error', data)
        
    def test_evaluate_submission_empty_text(self):
        """Test submission evaluation with empty text"""
        response = self.app.post('/llm/rubric-score',
                               data=json.dumps({'student_submission': ''}),
                               content_type='application/json')
        
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['status'], 'error')
        self.assertIn('error', data)
        
    def test_evaluate_submission_whitespace_only(self):
        """Test submission evaluation with whitespace-only text"""
        response = self.app.post('/llm/rubric-score',
                               data=json.dumps({'student_submission': '   '}),
                               content_type='application/json')
        
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['status'], 'error')
        self.assertIn('error', data)
        
    def test_evaluate_submission_long_text(self):
        """Test submission evaluation with very long text"""
        long_text = "This is a test. " * 1000  # Create very long text
        
        response = self.app.post('/llm/rubric-score',
                               data=json.dumps({'student_submission': long_text}),
                               content_type='application/json')
        
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['status'], 'error')
        self.assertIn('error', data)
        
    def test_evaluate_submission_excellent_score(self):
        """Test submission that should get excellent scores"""
        excellent_submission = "The economic impact of climate change is significant because it affects multiple sectors including agriculture, infrastructure, and public health. Rising temperatures lead to reduced crop yields, increased infrastructure damage from extreme weather events, and higher healthcare costs due to heat-related illnesses. These factors create a complex web of economic consequences that require comprehensive policy responses."
        
        response = self.app.post('/llm/rubric-score',
                               data=json.dumps({'student_submission': excellent_submission}),
                               content_type='application/json')
        
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 200)
        
        # Based on our mock logic, this should get excellent scores
        self.assertEqual(data['Structure'], 'Excellent')
        self.assertEqual(data['Relevance'], 'Excellent')
        
    def test_evaluate_submission_poor_score(self):
        """Test submission that should get poor scores"""
        poor_submission = "Bad essay."
        
        response = self.app.post('/llm/rubric-score',
                               data=json.dumps({'student_submission': poor_submission}),
                               content_type='application/json')
        
        data = json.loads(response.data)
        
        self.assertEqual(response.status_code, 200)
        
        # Based on our mock logic, this should get poor scores
        self.assertEqual(data['Structure'], 'Poor')
        self.assertEqual(data['Clarity'], 'Poor')
        self.assertEqual(data['Relevance'], 'Poor')
        self.assertEqual(data['Academic_Writing'], 'Poor')


class IntegrationTests:
    """Integration tests using real HTTP requests (server must be running)"""
    
    @staticmethod
    def test_health_check():
        """Test the health check endpoint with real HTTP request"""
        print("Testing Health Check...")
        try:
            response = requests.get(f"{BASE_URL}/health")
            if response.status_code == 200:
                data = response.json()
                print(f"✓ Health Check: {data['status']}")
                print(f"   Service: {data['service']}")
                print(f"   Version: {data['version']}")
                return True
            else:
                print(f"✗ Health Check Failed: {response.status_code}")
                return False
        except requests.exceptions.ConnectionError:
            print("✗ Cannot connect to API. Make sure the server is running.")
            return False

    @staticmethod
    def test_rubric_info():
        """Test the rubric info endpoint with real HTTP request"""
        print("\nTesting Rubric Info...")
        try:
            response = requests.get(f"{BASE_URL}/rubric-info")
            if response.status_code == 200:
                data = response.json()
                print("✓ Rubric Info Retrieved Successfully")
                print(f"   Categories: {', '.join(data['rubric_categories'].keys())}")
                print(f"   Rating Scale: {data['rubric_categories']['Structure']}")
                return True
            else:
                print(f"✗ Rubric Info Failed: {response.status_code}")
                return False
        except Exception as e:
            print(f"✗ Error getting rubric info: {e}")
            return False

    @staticmethod
    def evaluate_submission(submission_text, description):
        """Evaluate a student submission using real HTTP request"""
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
                print("✓ Evaluation Successful")
                print("   Results:")
                for category, score in data.items():
                    print(f"     {category}: {score}")
                return True
            else:
                print(f"✗ Evaluation Failed: {response.status_code}")
                error_data = response.json()
                print(f"   Error: {error_data.get('error', 'Unknown error')}")
                return False
                
        except Exception as e:
            print(f"✗ Error during evaluation: {e}")
            return False

    @staticmethod
    def test_various_submissions():
        """Test the API with various types of student submissions"""
        print("\n" + "="*50)
        print("TESTING VARIOUS SUBMISSIONS")
        print("="*50)
        
        test_cases = [
            # Test 1: Excellent submission
            ("""
            The economic impact of climate change is significant because it affects multiple sectors 
            including agriculture, infrastructure, and public health. Rising temperatures lead to 
            reduced crop yields, increased infrastructure damage from extreme weather events, and 
            higher healthcare costs due to heat-related illnesses. These factors create a complex 
            web of economic consequences that require comprehensive policy responses.
            """, "Excellent Academic Essay"),
            
            # Test 2: Good submission
            ("""
            Climate change has economic effects on agriculture and infrastructure. 
            Higher temperatures reduce crop yields and damage buildings. This costs money 
            and affects people's health. We need policies to address these problems.
            """, "Good Academic Essay"),
            
            # Test 3: Fair submission
            ("""
            Climate change affects the economy. It impacts farming and buildings. 
            Crops don't grow as well. Buildings get damaged. This costs money.
            """, "Fair Academic Essay"),
            
            # Test 4: Poor submission
            ("Climate change bad. Economy hurt.", "Poor Academic Essay"),
            
            # Test 5: Empty submission (should fail)
            ("", "Empty Submission (Should Fail)")
        ]
        
        results = []
        for submission, description in test_cases:
            result = IntegrationTests.evaluate_submission(submission, description)
            results.append(result)
        
        return all(results)


def run_unit_tests():
    """Run unit tests (no server needed)"""
    print("="*60)
    print("RUNNING UNIT TESTS (No server required)")
    print("="*60)
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestRubricScoringAPI)
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result.wasSuccessful()


def run_integration_tests():
    """Run integration tests (server must be running)"""
    print("="*60)
    print("RUNNING INTEGRATION TESTS (Server must be running)")
    print("="*60)
    
    # Check if server is running
    if not IntegrationTests.test_health_check():
        print("\n❌ Server is not running!")
        print("To start the server, run: python app.py")
        return False
    
    # Test rubric info
    IntegrationTests.test_rubric_info()
    
    # Test various submissions
    success = IntegrationTests.test_various_submissions()
    
    return success


def main():
    """Main function to run all tests"""
    print("LLM Rubric Scoring API - Comprehensive Test Suite")
    print("="*60)
    
    # Run unit tests first
    unit_success = run_unit_tests()
    
    print("\n" + "="*60)
    print("INTEGRATION TESTS")
    print("="*60)
    print("Note: Integration tests require the server to be running.")
    print("Start the server with: python app.py")
    print("Then run: python test_and_demo.py --integration")
    print("="*60)
    
    if unit_success:
        print("\n✅ Unit tests passed!")
    else:
        print("\n❌ Unit tests failed!")
    
    return unit_success


if __name__ == "__main__":
    import sys
    
    if "--integration" in sys.argv:
        # Run integration tests
        success = run_integration_tests()
        if success:
            print("\n✅ All integration tests passed!")
        else:
            print("\n❌ Some integration tests failed!")
    else:
        # Run unit tests by default
        main()
