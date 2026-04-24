# 📚 StudyBuddy AI

> An AI-powered study assistant that transforms your lecture notes into summaries, flashcards, quizzes, and a personal tutor — all from a single PDF upload.

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=flat-square&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green?style=flat-square&logo=fastapi)
![Three.js](https://img.shields.io/badge/Three.js-r128-black?style=flat-square&logo=three.js)
![Status](https://img.shields.io/badge/Status-In%20Development-orange?style=flat-square)

---

## 📖 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [AI Integration](#ai-integration)
- [Mock Client](#mock-client)
- [Sample Data](#sample-data)
- [Roadmap](#roadmap)
- [Known Issues](#known-issues)

---

## Overview

StudyBuddy AI is a full-stack web application built as a personal project during my 3rd year of Software Engineering at the University of Westminster. The goal was to explore real-world AI API integration by building something genuinely useful for students.

The app accepts a PDF (e.g. lecture slides or notes), extracts the text, and uses a large language model to generate a structured summary, key concept definitions, revision flashcards, multiple choice quiz questions, and conversational Q&A grounded in the uploaded material.

---

## Features

- **PDF Upload** — drag-and-drop or browse to upload any lecture PDF
- **AI Summarisation** — generates a structured summary with bullet points, key concepts, and flashcards
- **Quiz Generation** — produces 5 multiple choice questions with answers based on the content
- **Chat with Notes** — ask any question and get an answer sourced directly from your uploaded material
- **3D Animated Hero** — interactive Three.js scene with a floating book, orbital rings, and particles
- **Step Progress Indicator** — tracks your progress through the 4-step workflow
- **Responsive Dark UI** — custom design with Syne + DM Sans typography and a violet/teal/pink palette

---

## Project Structure

```
StudyBuddy-AI/
│
├── backend/
│   ├── main.py              # FastAPI server — defines all API endpoints
│   ├── gemini_client.py     # Google Gemini API integration (requires API key)
│   ├── mock_client.py       # Offline mock AI — returns realistic pre-written responses
│   ├── requirements.txt     # Python dependencies
│   └── .env                 # Secret API keys — never commit this file!
│
├── frontend/
│   ├── index.html           # Full UI — Three.js 3D hero + study dashboard
│   └── favicon-256.png      # Custom StudyBuddy logo/favicon
│
├── ML_Lecture_Slides.pdf    # Sample PDF for testing (see below)
├── LICENSE
└── README.md
```

---

## Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| Backend | Python + FastAPI | REST API server with 4 endpoints |
| PDF Parsing | pdfplumber | Extract raw text from uploaded PDFs |
| AI | Google Gemini / Mock Client | Generate summaries, quizzes, and chat responses |
| Frontend | Vanilla HTML/CSS/JS | Lightweight, no-framework UI |
| 3D Graphics | Three.js (r128) | Animated hero scene |
| Typography | Google Fonts (Syne + DM Sans) | Custom visual identity |
| Environment | python-dotenv | Secure API key management |

---

## Getting Started

### Prerequisites

- Python 3.9 or higher
- A modern web browser

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/your-username/StudyBuddy-AI.git
cd StudyBuddy-AI
```

**2. Install Python dependencies**
```bash
cd backend
pip3 install fastapi uvicorn python-dotenv google-genai pdfplumber python-multipart
```

**3. Set up your environment file**

Create a `.env` file inside the `backend/` folder:
```env
GEMINI_API_KEY=your_google_gemini_api_key_here
```

> ⚠️ Never share or commit your `.env` file. Add it to `.gitignore` immediately.

**4. Start the backend server**
```bash
cd backend
python3 -m uvicorn main:app --reload
```

The API will be running at `http://127.0.0.1:8000`

**5. Open the frontend**

Open `frontend/index.html` directly in your browser. No build step needed.

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/upload` | Upload a PDF and extract its text |
| `POST` | `/summarize` | Generate summary + key concepts + flashcards |
| `POST` | `/quiz` | Generate 5 MCQ questions from the PDF |
| `POST` | `/chat` | Ask a question grounded in the uploaded notes |
| `GET` | `/` | Health check |

---

## AI Integration

StudyBuddy AI is designed to work with **Google Gemini** via the new `google-genai` SDK.

To switch to a live AI model, make sure `main.py` imports from `gemini_client`:

```python
from gemini_client import summarize_text, generate_quiz, chat_with_notes
```

Then ensure your `.env` contains a valid Gemini API key. You can get one free at [aistudio.google.com](https://aistudio.google.com).

> **Note:** The free tier of Gemini requires a Google account with billing enabled to activate quota. Google provides $300 in free credits for new accounts, so no actual charge is incurred.

---

## Mock Client

The file `mock_client.py` is an **offline substitute for the real AI API**. It returns realistic, pre-written responses for summarisation, quiz generation, and chat — without making any external API calls.

### Why does this exist?

During development, several issues blocked access to live AI APIs:

- Google Gemini API keys were auto-revoked after being accidentally exposed in a terminal screenshot (a security lesson learned the hard way!)
- New Google accounts were flagged with `limit: 0` quota on the free tier, requiring billing activation
- OpenAI's free credits had expired

Rather than block all development progress, `mock_client.py` was introduced so that the full application flow — upload → summarise → quiz → chat — could be built, tested, and styled without a working API key.

### How to switch between mock and real AI

In `main.py`, change the import at the top of the file:

```python
# For offline development and testing:
from mock_client import summarize_text, generate_quiz, chat_with_notes

# For production with a real Gemini API key:
from gemini_client import summarize_text, generate_quiz, chat_with_notes
```

The rest of the application is completely unaffected — the same endpoints, the same frontend, the same behaviour.

---

## Sample Data

The file `ML_Lecture_Slides.pdf` is a **synthetically generated lecture PDF** created specifically to test the app. It simulates a real university lecture on *Introduction to Machine Learning* and covers:

- What is Machine Learning and why it matters
- Supervised, Unsupervised, and Reinforcement Learning
- Key concepts: features, labels, training/test split
- Overfitting and underfitting — causes and fixes
- Common algorithms: Linear Regression, Decision Trees, SVM, Neural Networks
- Model evaluation metrics: Accuracy, Precision, Recall, F1 Score, MSE
- Real-world applications across healthcare, finance, and NLP
- Review questions and recommended reading

This PDF was chosen because it is content-rich, well-structured, and representative of what a student would actually upload — making it ideal for testing all four features of the app.

To test the app, upload `ML_Lecture_Slides.pdf` and try:
- Generating the summary
- Taking the quiz
- Asking: *"What is overfitting and how do I fix it?"*

---

## Roadmap

| Feature | Status |
|---|---|
| PDF upload + text extraction | ✅ Done |
| AI summarisation + flashcards | ✅ Done |
| MCQ quiz generation | ✅ Done |
| Chat with notes | ✅ Done |
| 3D animated hero (Three.js) | ✅ Done |
| Custom favicon + branding | ✅ Done |
| Mock client for offline dev | ✅ Done |
| SQLite session persistence | 🔜 Planned |
| User authentication (JWT) | 🔜 Planned |
| React frontend upgrade | 🔜 Planned |
| Free deployment (Render.com) | 🔜 Planned |

---

## Known Issues

- **Gemini free tier quota** — New API keys may show `limit: 0` until billing is activated on the associated Google Cloud project. Use `mock_client.py` in the meantime.
- **API key security** — Never paste your API key into a terminal that is being shared or screenshotted. Always read secrets from `.env` files.
- **Python 3.9 deprecation warnings** — The `google-genai` and `urllib3` packages emit `FutureWarning` messages on Python 3.9. These do not affect functionality but upgrading to Python 3.11+ is recommended.
- **Session storage** — Uploaded PDFs are stored in memory only. Restarting the server clears all uploaded files.

---

## Security Notes

- The `.env` file containing your API key must **never** be committed to GitHub
- Add `.env` to your `.gitignore`:
  ```bash
  echo ".env" >> .gitignore
  ```
- If an API key is accidentally exposed, revoke it immediately at [aistudio.google.com/apikey](https://aistudio.google.com/apikey)

---

## License

This project is licensed under the MIT License. See `LICENSE` for details.
