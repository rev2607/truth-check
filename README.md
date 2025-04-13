# TruthCheck  
**“Don’t believe everything you scroll. Check it with AI.”**

A real-time misinformation detector built for the social media era — fact-check tweets, forwards, TikToks, and headlines with AI.  
Styled like ChatGPT or WhatsApp to make it familiar, fast, and Gen Z-friendly.

---

## ✨ Features

- ✅ **Instant AI Fact-Checking** using Google’s Gemini 2.0
- 💬 **Chat UI Inspired by ChatGPT & WhatsApp**
- 🧠 **Structured AI Reasoning** with citations & verdict
- 🔂 **Session-Based Chat History**
- 🧑‍🎓 Perfect for hackathons, media literacy apps, or social impact tools

---

## 🧠 Tech Stack

| Layer     | Stack                      |
|-----------|----------------------------|
| Frontend  | HTML + CSS (Custom styling) |
| Backend   | Flask (Python)             |
| AI Engine | Google Gemini 2.0 API      |
| Storage   | Flask session (chat history) |

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/TruthCheck.git
cd TruthCheck
```

### 2. Install Dependencies

```bash
pip install flask requests
```

### 3. Export Gemini API Key

Set your [Gemini API Key](https://aistudio.google.com/app/apikey) in your terminal:

#### Mac/Linux
```bash
export GEMINI_API_KEY="your_api_key_here"
```

#### Windows (CMD)
```cmd
set GEMINI_API_KEY="your_api_key_here"
```

#### Windows (PowerShell)
```powershell
$env:GEMINI_API_KEY="your_api_key_here"
```

### 4. Run the App

```bash
python run.py
```

Then go to:  
[http://localhost:5000](http://localhost:5000)

---

## 💡 Inspiration

We live in an age where misinformation spreads faster than truth. From viral TikTok clips to politically charged tweets and WhatsApp forwards, it’s becoming harder to tell fact from fiction. We wanted to build something *fast*, *familiar*, and *frictionless* — a tool that doesn’t feel like “another fact-checking site,” but like texting a friend who’s always right.

Thus, **TruthCheck AI** was born:  
A Gen Z-friendly, chat-based AI assistant that tells you if that “news” you just saw is actually real — with reasoning and sources.

---

## 🧠 What It Does

TruthCheck AI is an **AI-powered real-time fact-checking assistant** that:

- Accepts any text input — tweet, headline, message, or quote
- Uses **Google’s Gemini 2.0** to verify the claim
- Responds in a clean **chat format**
- Provides:
  - ✅ **Verdict**
  - 🧠 **Reasoning**
  - 🌐 **Sources**

---

> *“You can’t believe everything you scroll — but you can always check it.”*

