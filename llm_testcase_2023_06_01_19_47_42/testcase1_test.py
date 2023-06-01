#full path of the test case file: /home/user/test_app.py

# import necessary modules
import unittest
from flask import Flask, render_template, request

# import the app module
import sys
sys.path.append('/root')
from app import app

# define the test class
class TestApp(unittest.TestCase):

    # test the hello_world function
    def test_hello_world(self):
        with app.test_client() as client:
            response = client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data, b'hello world!!')

    # test the greetUser function
    def test_greetUser(self):
        with app.test_client() as client:
            response = client.get('/home')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'<h1>Welcome to the Home Page!</h1>', response.data)

    # test the calculateResult function with correct input
    def test_calculateResult_correct(self):
        with app.test_client() as client:
            response = client.post('/test', data=dict(height='8848'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Your Answer:8848\nYou have passed the test,Keep it up.', response.data)

    # test the calculateResult function with incorrect input
    def test_calculateResult_incorrect(self):
        with app.test_client() as client:
            response = client.post('/test', data=dict(height='1234'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Your Answer:1234\nYou have failed the test, keep trying.', response.data)

# run the tests
if __name__ == '__main__':
    unittest.main()