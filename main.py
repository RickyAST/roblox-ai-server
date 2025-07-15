from flask import Flask, request, jsonify
import os
import openai

app = Flask(__name__)

openai.api_key = os.environ.get("OPENROUTER_API_KEY")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    if not openai.api_key:
        return jsonify({"response": "⚠️ OpenAI ключ не установлен."})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # или gpt-4, если есть доступ
            messages=[
                {"role": "system", "content": "Ты дружелюбный NPC в Roblox. Отвечай просто, интересно и с юмором."},
                {"role": "user", "content": user_message}
            ],
            max_tokens=150,
            temperature=0.8,
        )
        reply = response.choices[0].message.content.strip()
        return jsonify({"response": reply})
    except Exception as e:
        return jsonify({"response": f"❌ Ошибка ИИ: {str(e)}"}), 500

@app.route("/", methods=["GET"])
def root():
    return "AI Server Running", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
