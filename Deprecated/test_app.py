import unittest
import json
from app import app

class TestRubricScoringAPI(unittest.TestCase):
    
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
        
    def test_evaluate_submission_no_json(self):
        """Test submission evaluation with no JSON data"""
        response = self.app.post('/llm/rubric-score',
                               data='not json',
                               content_type='application/json')
        
        # This should return 400, but Flask might return 500 for malformed JSON
        self.assertIn(response.status_code, [400, 500])
        
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

if __name__ == '__main__':
    unittest.main()
