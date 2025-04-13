from flask import Blueprint, render_template, request
import requests
import os
import re

main = Blueprint('main', __name__)

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

def clean_gemini_response(text):
    # Remove markdown bold/italics
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"\*(.*?)\*", r"\1", text)

    # Split sections
    lines = text.split("\n")
    structured = {}
    current_section = "Main"
    structured[current_section] = []

    for line in lines:
        if ":" in line and len(line.split(":")[0]) < 50:
            key, val = line.split(":", 1)
            current_section = key.strip()
            structured[current_section] = [val.strip()]
        else:
            structured[current_section].append(line.strip())

    return structured

@main.route('/', methods=['GET', 'POST'])
def index():
    result = None
    user_input = ""

    if request.method == 'POST':
        user_input = request.form['user_input'].strip()

        if not user_input:
            result = {"Error": ["Please enter some text to fact-check."]}
            return render_template('index.html', result=result, user_input=user_input)

        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
        headers = {"Content-Type": "application/json"}
        data = {
            "contents": [
                {
                    "parts": [
                        {"text": f"Fact-check this statement and explain briefly:\n\n{user_input}"}
                    ]
                }
            ]
        }

        try:
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()
            json_data = response.json()
            raw_text = json_data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "No response from Gemini.")
            result = clean_gemini_response(raw_text)

        except Exception as e:
            result = {"Error": [f"❌ {str(e)}"]}

    return render_template('index.html', result=result, user_input=user_input)
