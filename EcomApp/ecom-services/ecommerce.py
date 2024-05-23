#!/usr/local/bin/python3

from flask import Flask, request, jsonify
from flask_cors import CORS
import jwt
import json

app = Flask("ecommerce")
CORS(app)  # Apply CORS for all routes

# Load the config file
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# Access nested config 
SECRET_KEY = config['API']['SECRET_KEY']
PRODUCTS = config['PRODUCTS']
USERS = config['USERS']

@app.route("/login", methods=["POST"])
def login():
    try:
        data = request.get_json()
        print(data)
        username = data.get("username")
        password = data.get("password")

        # Validate user credentials
        if username in USERS and USERS[username] == password:
            # Generate JWT token
            payload = {"username": username}
            token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
            return jsonify({"token": token}), 200
        else:
            return jsonify({"message": "Invalid credentials"}), 401
    except Exception as e:
        return jsonify({"message": str(e)}), 500


# Middleware to verify JWT token 
def verify_token(auth_token, secret_key):
    try:
        payload = jwt.decode(auth_token, secret_key, algorithms=["HS256"])
        print(payload)
        user_id = payload.get('username')  # Extract user ID from the payload
        return user_id
    except jwt.ExpiredSignatureError:
        # Token has expired
        return None
    except jwt.DecodeError:
        # Invalid token
        return None



@app.route("/products", methods=["GET"])
def get_products():
    AUTH_TOKEN = request.headers.get('authorization').split(' ')[1]
    # Verify token
    user_info = verify_token(AUTH_TOKEN,SECRET_KEY)
  
    if not user_info:
        return jsonify({"error": "Invalid token"}), 401

    # Check if user is "user1"
    if user_info != "user1":
        return jsonify({"error": "Access denied"}), 403

    # Send list of 2 products back to client
    user_products = PRODUCTS[:2]
    return jsonify(user_products)


if __name__ == "__main__":
    app.run(host="localhost", port=5000)

