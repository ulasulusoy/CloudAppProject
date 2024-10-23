
from flask import Flask, request, jsonify
app = Flask(__name__)

users = []

@app.route('/users', methods=['POST'])
def create_user():
    user = request.json
    users.append(user)
    return jsonify(user), 201

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = request.json
    if user_id < len(users):
        users[user_id] = user
        return jsonify(user)
    return "User not found", 404

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id < len(users):
        removed_user = users.pop(user_id)
        return jsonify(removed_user)
    return "User not found", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
