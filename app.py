from flask import Flask, request
import google.generativeai as genai
import os

app = Flask(__name__)

# Konfigurasi Gemini
GEMINI_API_KEY = os.getenv("AIzaSyAD3MuhDu3HvT-O5aqXulY4qeC8tjfrdxw")
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")

@app.route("/", methods=["GET"])
def home():
    return "Gemini AI Flask Bot is running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    from_number = request.form.get("From")
    user_msg = request.form.get("Body")

    print(f"Pesan dari {from_number}: {user_msg}")

    try:
        response = model.generate_content(user_msg)
        reply = response.text.strip()
    except Exception as e:
        reply = f"Error: {str(e)}"

    return f"<Response><Message>{reply}</Message></Response>", 200, {"Content-Type": "text/xml"}
