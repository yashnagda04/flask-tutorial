#full path of the test case file: /home/user/tests/test_app.py

# import necessary modules
import unittest
from flask import Flask, render_template, request
from app import app

class FlaskTest(unittest.TestCase):
    
    # test if the app is running
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
    
    # test if the home page is accessible
    def test_home(self):
        tester = app.test_client(self)
        response = tester.get('/home')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
    
    # test if the test page is accessible
    def test_test(self):
        tester = app.test_client(self)
        response = tester.get('/test')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
    
    # test if the test page returns correct message for correct answer
    def test_test_correct_answer(self):
        tester = app.test_client(self)
        response = tester.post('/test', data=dict(height='8848'), follow_redirects=True)
        self.assertIn(b'You have passed the test,Keep it up.', response.data)
    
    # test if the test page returns correct message for incorrect answer
    def test_test_incorrect_answer(self):
        tester = app.test_client(self)
        response = tester.post('/test', data=dict(height='1234'), follow_redirects=True)
        self.assertIn(b'You have failed the test, keep trying.', response.data)

if __name__ == '__main__':
    unittest.main()