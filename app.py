from flask import Flask, request
import google.generativeai as genai
import os

app = Flask(__name__)

# Load API key dari environment
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "AIzaSyAD3MuhDu3HvT-O5aqXulY4qeC8tjfrdxw")
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")

@app.route("/", methods=["GET"])
def index():
    return "Gemini Flask Bot is Live!"

@app.route("/webhook", methods=["POST"])
def webhook():
    user_msg = request.form.get("Body")
    from_number = request.form.get("From")

    try:
        response = model.generate_content(user_msg)
        reply = response.text.strip()
    except Exception as e:
        reply = f"Gagal: {str(e)}"

    print(f"User {from_number} → {user_msg}")
    print(f"Bot → {reply}")

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Message>{reply}</Message>
</Response>""", 200, {"Content-Type": "text/xml"}
