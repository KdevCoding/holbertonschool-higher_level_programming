from flask import Flask, jsonify, abort, request

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to the Flask API!"


@app.route('/status')
def status():
    return "OK"


@app.route('/data')
def dat():
    keys_list = list(users.keys())
    return jsonify(keys_list)


@app.route('/users/<username>')
def display_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        abort(404, description='{"error": "User not found"}')


@app.route('/add_user', methods=["POST"])
def add_user():
    data = request.get_json(force=True, silent=True)
    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data

    return jsonify({"message": "User added successfully", "user": data}), 201


if __name__ == "__main__":
    app.run()
