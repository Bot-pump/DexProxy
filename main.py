from flask import Flask, jsonify, request
import requests
import os

app = Flask(__name__)
MORALIS_API_KEY = os.getenv("MORALIS_API_KEY", "Your-Moralis-Key")

@app.route('/proxy', methods=['GET'])
def proxy():
    target_url = request.args.get('url')
    if not target_url:
        return jsonify({"error": "Missing URL parameter"}), 400

    try:
        headers = {
            "X-API-Key": MORALIS_API_KEY
        }
        response = requests.get(target_url, headers=headers)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def home():
    return "DexProxy is running!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000)
