# 🎙️ Social Profile Narrator / Reviewer

A Python CLI tool that fetches social media profiles, generates an AI-powered review using Groq (LLaMA 3), and narrates it out loud using gTTS.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![AI](https://img.shields.io/badge/AI-Groq%20LLaMA3-orange)

---

## 🚀 How It Works
```
User picks platform → enters username/bio → GitHub API fetches data
→ Groq AI generates review → gTTS speaks it out loud → saved as MP3
```

## 🛠️ How I Built It

1. Started with `main.py` as the skeleton — user input and platform selection
2. Built `github.py` to fetch real profile data using GitHub's free public API
3. For Instagram and LinkedIn — user manually enters bio (APIs are restricted)
4. Built `narrator.py` with two functions:
   - `generate_summary()` — sends profile data to Groq AI, gets back a review
   - `generate_audio()` — converts that review to speech using gTTS and plays it
5. Used `.env` file to keep API keys secure and out of GitHub

## 📁 Project Structure
```
social-profile-narrator/
├── main.py              # entry point of the program
├── narrator.py          # AI summary + text to speech
├── requirements.txt     # all libraries needed
├── README.md            # project documentation
└── platforms/
    ├── __init__.py      # marks platforms as a python package
    ├── github.py        # fetches real GitHub profile via API
    ├── instagram.py     # manual input for Instagram
    └── linkedin.py      # manual input for LinkedIn
```

## ⚙️ Installation
```bash
git clone https://github.com/venux09/social-profile-narrator
cd social-profile-narrator
pip install -r requirements.txt
```

Create a `.env` file:
```
API=your_groq_api_key_here
```

Run:
```bash
python main.py
```

## 🎬 Demo

> Video demo coming soon!

## 🔮 Future Upgrades

- [ ] Upgrade voice to ElevenLabs for more realistic narration
- [ ] Add Flask web interface
- [ ] Add webbrowser integration for Instagram/LinkedIn
- [ ] Support more platforms

## 📄 License

MIT License — feel free to use and modify!

## 👨‍💻 Author

Made by [venux09](https://github.com/venux09) aka Monu Verma
```

demo:video