from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    if not openai.api_key:
        return jsonify({"response": "Это тестовый ответ от ИИ-сервера."})

    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Ты дружелюбный NPC в Roblox."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=100
        )
        reply = completion.choices[0].message.content.strip()
        return jsonify({"response": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/", methods=["GET"])
def root():
    return "AI Server Running", 200
