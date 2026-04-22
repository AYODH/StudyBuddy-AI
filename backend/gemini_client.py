import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    with open(".env") as f:
        for line in f:
            if line.startswith("GEMINI_API_KEY"):
                api_key = line.strip().split("=", 1)[1]
                break

client = genai.Client(api_key=api_key)
MODEL = "models/gemini-2.0-flash-lite"


def summarize_text(text: str) -> str:
    response = client.models.generate_content(model=MODEL, contents=f"""
You are StudyBuddy, a smart study assistant.
Given the following study material, provide:
1. A clear summary (5-7 bullet points)
2. Key concepts (list 5 important terms with one-line definitions)
3. Flashcards (5 Q&A pairs for revision)

Study material:
{text[:8000]}
""")
    return response.text


def generate_quiz(text: str) -> str:
    response = client.models.generate_content(model=MODEL, contents=f"""
Based on the following study material, generate 5 multiple choice questions.
Format each:

Q1: [Question]
A) [Option]
B) [Option]
C) [Option]
D) [Option]
Answer: [Correct letter]

Study material:
{text[:8000]}
""")
    return response.text


def chat_with_notes(text: str, user_question: str) -> str:
    response = client.models.generate_content(model=MODEL, contents=f"""
You are StudyBuddy. Answer ONLY based on the notes below.
If the answer isn't in the notes, say so honestly.

Notes:
{text[:8000]}

Student's question: {user_question}
""")
    return response.text
