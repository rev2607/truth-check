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

## 🖼 Screenshot

![screenshot](https://your-screenshot-url.com/chat-ui.png) <!-- Add a chat UI screenshot -->

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
- Responds in a clean **chat format**, styled like WhatsApp/ChatGPT
- Provides:
  - ✅ **Verdict**
  - 🧠 **Reasoning**
  - 🌐 **Sources**
- Maintains **chat history** throughout your session

---

## 🏐 How We Built It

- **Backend**: Flask with session management to maintain chat history
- **Frontend**: Custom HTML/CSS with a modern chat UI design
- **AI Engine**: Gemini 2.0 (`generativelanguage.googleapis.com`) using a structured prompt for consistent JSON replies
- **Prompt Engineering**: Carefully designed to ensure structured, reliable outputs from Gemini
- **Session Storage**: In-memory session data with `flask.session` to simulate real-time chat

---

## 🧱 Challenges We Ran Into

- Gemini sometimes responded with unstructured output, so we had to sanitize and fallback safely
- Handling inconsistent AI formatting while still preserving a clean UI was tricky
- Maintaining chat history across user inputs required careful session handling
- Balancing simplicity with UX — especially for Gen Z users — meant many UI tweaks

---

## 🏆 Accomplishments That We're Proud Of

- Built a full-stack AI-powered app in just hours
- Created a **zero-friction user experience** — no login, no config, just paste and go
- Achieved reliable structured outputs from Gemini using smart prompting
- Designed a Gen Z aesthetic that feels like a real app, not a hackathon prototype

---

## 📚 What We Learned

- 🧠 Prompt engineering is *everything* — structured AI output requires precision
- Flask session storage is surprisingly powerful for prototyping
- Even with powerful models, post-processing is key to making things usable
- Building for Gen Z means thinking like Gen Z — speed, simplicity, and aesthetics matter

---

## 🚀 What's Next for TruthCheck AI

Here’s where we’re heading:

- 🔐 **User Accounts & Chat History**: Save conversations across devices
- 📊 **Truth Score**: Quantify the reliability of a claim using LLM confidence + citation trust
- 🌐 **Browser Extension**: Check any tweet or post inline, like Grammarly for truth
- 📱 **Mobile PWA**: Turn it into a real mobile app, offline-ready
- 🤝 **Community Feedback Loop**: Users can upvote/downvote verdicts to train a finetuned model
- 💬 **Multimodal Support**: Let users upload screenshots, audio clips, or TikToks for verification

> “The truth isn’t hidden — it’s just buried under noise. We built TruthCheck to clear the static.”

---

## 💼 License

MIT License — free to use, remix, and improve.

---

## 😎 Author

Built with 💻, ☕, and trust issues by [Your Name](https://github.com/your-username)

> *“You can’t believe everything you scroll — but you can always check it.”*

