#!/usr/local/bin/python3
from ecommerce import login

import unittest
import requests
import json

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# Access nested config 
LOGIN_URL = config['URLS'][0]["login"]
    
class TestLoginService(unittest.TestCase):
       
    def test_authenticate_user_valid_credentials(self):
        # Simulate a POST request to the login service
        data = {"username": "user1", "password": "password1"}
        response = requests.post(LOGIN_URL, json=data)

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        print( f"login test passed with code {response.status_code} ")

        # Add more assertions as needed (e.g., check response content)

    def test_authenticate_user_invalid_credentials(self):
        # Simulate a POST request with invalid credentials
        data = {"username": "invalid_user", "password": "wrong_password"}
        response = requests.post(LOGIN_URL, json=data)

        # Assert that the response status code is 401 (Unauthorized)
        self.assertEqual(response.status_code, 401)
        print(f"login test failed with code {response.status_code} ")

        # Add more assertions as needed

if __name__ == "__main__":
    unittest.main()
