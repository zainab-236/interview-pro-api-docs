from flask import Flask, request, jsonify
import secrets

app = Flask(__name__)

# In-memory storage for users and their API keys (Use a database in production)
user_api_keys = {}

# Function to generate a new API key
def generate_api_key():
    return secrets.token_hex(16)  # Generates a random 32-character API key

# Route to create a new API key for a user
@app.route('/generate-api-key', methods=['POST'])
def generate_key_for_user():
    # Get the username from the POST request
    username = request.json.get('username')

    if not username:
        return jsonify({"message": "Username is required"}), 400
    
    # Generate a new API key
    new_api_key = generate_api_key()

    # Store the API key for the user
    user_api_keys[username] = new_api_key

    return jsonify({
        "message": "API key generated successfully",
        "username": username,
        "api_key": new_api_key
    })

# Route to get protected data (requires API key)
@app.route('/data', methods=['GET'])
def get_protected_data():
    api_key = request.headers.get('x-api-key')

    # Check if the API key is valid
    if api_key not in user_api_keys.values():
        return jsonify({"message": "Invalid API key"}), 401
    
    return jsonify({"message": "Here is your protected data!"})

if __name__ == '__main__':
    app.run(debug=True)
