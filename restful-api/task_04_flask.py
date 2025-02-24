#!/usr/bin/python3
from flask import Flask, jsonify, request, make_response

app = Flask(__name__)

users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}


@app.route('/')
def home():

    return "Welcome to the Flask API!"


@app.route('/data')
def get_data():

    return jsonify(list(users.keys()))


@app.route('/status')
def status():

    return "OK"


@app.route('/users/<username>')
def get_user(username):

    if username in users:
        return jsonify(users[username])
    else:
        response = jsonify({"error": "User not found"})
        response.status_code = 404
        return response


@app.route('/add_user', methods=["POST"])
def add_user():
    data = request.get_json()
    if not data or "username" not in data:
        return make_response(jsonify({"error": "Username is required"}), 400)

    username = data["username"]
    if username in users:
        return make_response(jsonify({"error": "Username already exists"}), 400)

    users[username] = data
    return make_response(jsonify({"message": "User added", "user": data}), 201)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
