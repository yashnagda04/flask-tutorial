# /root/tests/test_app.py
import unittest
from unittest.mock import patch
from flask import request
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_hello_world(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'hello world!!')

    def test_greetUser(self):
        response = self.app.get('/home')
        self.assertEqual(response.status_code, 200)
        # Check if 'home.html' is rendered
        self.assertIn('<title>Home</title>', response.data.decode('utf-8'))

    def test_calculateResult_GET(self):
        response = self.app.get('/test')
        self.assertEqual(response.status_code, 200)
        # Check if 'test.html' is rendered
        self.assertIn('<title>Test</title>', response.data.decode('utf-8'))

    @patch('app.request')
    def test_calculateResult_POST_correct(self, mock_request):
        mock_request.method = 'POST'
        mock_request.form = {'height': '8848'}
        with app.test_request_context('/test', method='POST'):
            response = app.dispatch_request()
            self.assertIn("You have passed the test", response)

    @patch('app.request')
    def test_calculateResult_POST_incorrect(self, mock_request):
        mock_request.method = 'POST'
        mock_request.form = {'height': '1234'}
        with app.test_request_context('/test', method='POST'):
            response = app.dispatch_request()
            self.assertIn("You have failed the test", response)

if __name__ == '__main__':
    unittest.main()