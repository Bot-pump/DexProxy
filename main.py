from flask import Flask, jsonify, request
import requests
import os

app = Flask(__name__)

MORALIS_API_KEY = os.getenv("MORALIS_API_KEY")

@app.route('/v1/token/new')
def get_new_tokens():
    chain = request.args.get("chain")
    limit = request.args.get("limit", 10)

    if not chain:
        return jsonify({"error": "Missing chain parameter"}), 400

    headers = {
        "X-API-Key": MORALIS_API_KEY
    }
    url = f"https://token-api.moralis.io/v1/token/new?chain={chain}&limit={limit}"

    try:
        response = requests.get(url, headers=headers)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/')
def home():
    return "DexProxy is running!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000)
