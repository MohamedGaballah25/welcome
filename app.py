from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/greet', methods=['POST'])
def greet():
    data = request.json
    if not data or 'name' not in data:
        return jsonify({"error": "Please provide a name"}), 400
    
    name = data['name']
    return jsonify({"message": f"Thanks for the name, {name}!"})

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the greeting API. Send a POST request to /greet with a name to get started!"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)