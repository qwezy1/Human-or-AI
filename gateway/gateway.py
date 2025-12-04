from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

BACKEND_URL = "http://backend:3000/api/main"  # имя сервиса backend из docker-compose

@app.route("/")
def root():
    return {"info": "Gateway API. Send POST to /predict with 'text'."}

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "Missing 'text' in request"}), 400

    try:
        resp = requests.post(BACKEND_URL, json={"text": data["text"]})
        resp.raise_for_status()
        return jsonify(resp.json())
    except requests.RequestException as e:
        return jsonify({"error": f"Backend request failed: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
