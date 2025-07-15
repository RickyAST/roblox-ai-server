from flask import Flask, request, jsonify
import os, openai

app = Flask(__name__)
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message","")
    # Если API не настроен — просто эхо
    return jsonify({"response": f"Эхо: {user_message}"})

@app.route("/", methods=["GET"])
def root():
    return "AI Server Running", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
