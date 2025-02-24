#!/usr/bin/python3
"""
task_04_flask.py

A simple API built using Flask.

This API provides the following endpoints:
    GET /
        Returns "Welcome to the Flask API!"
    GET /data
        Returns a JSON list of all usernames stored in the API.
    GET /status
        Returns the status "OK".
    GET /users/<username>
        Returns the full user object for the given username.
        If the user doesn't exist, returns {"error": "User not found"}.
    POST /add_user
        Expects JSON data to add a new user.
        If "username" is missing in the request data, returns a 400 error with {"error": "Username is required"}.
        Otherwise, adds the user to the API and returns a 201 confirmation with the user data.
"""

from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

users = {}


@app.route('/')
def home():
    """
    GET /
    
    Returns a welcome message.
    """
    return "Welcome to the Flask API!"


@app.route('/data')
def get_data():
    """
    GET /data
    
    Returns a JSON list of all usernames stored in the API.
    """
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """
    GET /status
    
    Returns a plain text status "OK".
    """
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """
    GET /users/<username>
    
    Returns the user object for the provided username.
    If the user is not found, returns {"error": "User not found"}.
    """
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"})


@app.route('/add_user', methods=["POST"])
def add_user():
    """
    POST /add_user
    
    Expects JSON data with the following format:
        {
            "username": "alice",
            "name": "Alice",
            "age": 25,
            "city": "San Francisco"
        }
        
    If the "username" key is missing, returns a 400 error with:
        {"error": "Username is required"}
    Otherwise, adds the new user to the users dictionary and returns a confirmation message with status 201.
    """
    data = request.get_json()
    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400
    username = data["username"]
    if username in users:
        return jsonify({"error": "Username already exists"}), 400
    username = data["username"]
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
