from flask import Flask, jsonify, request
import requests
import os

app = Flask(__name__)

# تأكد أن متغير MORALIS_API_KEY مضاف إلى بيئة Render
MORALIS_API_KEY = os.getenv("MORALIS_API_KEY")

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
    print("[ERROR] Proxy failed:", e)
    return jsonify({"error": str(e)}), 500

@app.route('/')
def home():
    return "✅ DexProxy is running and ready to fetch from Moralis API."

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000)
