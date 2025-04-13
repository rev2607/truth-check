from flask import Blueprint, render_template, request
import requests
import os
import json
import re

main = Blueprint('main', __name__)

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

def clean_gemini_response(text):
    # Remove Markdown code block formatting (```json ... ```)
    text = re.sub(r"```json|```", "", text).strip()

    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return {"Unstructured Output": [text]}

    structured = {}
    for key, value in data.items():
        if isinstance(value, list):
            structured[key] = value
        else:
            structured[key] = [value]
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
                        {
                            "text": f"""
You're an AI fact-checker. For the following claim, respond ONLY in this JSON format:

{{
    "Claim": "...",
    "Verdict": "...",
    "Reasoning": "...",
    "Source(s)": ["...", "..."]
}}

Claim: {user_input}
                            """
                        }
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
