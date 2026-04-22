import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
MODEL = "models/gemini-2.0-flash-lite"


def summarize_text(text: str) -> str:
    prompt = f"""
    You are StudyBuddy, a smart study assistant.
    Given the following study material, provide:
    1. 📝 A clear summary (5-7 bullet points)
    2. 🔑 Key concepts (list 5 important terms with one-line definitions)
    3. 🃏 Flashcards (5 Q&A pairs for revision)

    Study material:
    {text[:8000]}
    """
    response = client.models.generate_content(model=MODEL, contents=prompt)
    return response.text


def generate_quiz(text: str) -> str:
    prompt = f"""
    Based on the following study material, generate 5 multiple choice questions.
    Format each question exactly like this:

    Q1: [Question]
    A) [Option]
    B) [Option]
    C) [Option]
    D) [Option]
    Answer: [Correct letter]

    Study material:
    {text[:8000]}
    """
    response = client.models.generate_content(model=MODEL, contents=prompt)
    return response.text


def chat_with_notes(text: str, user_question: str) -> str:
    prompt = f"""
    You are StudyBuddy. The student has uploaded their study notes below.
    Answer the student's question based ONLY on the provided notes.
    If the answer isn't in the notes, say so honestly.

    Notes:
    {text[:8000]}

    Student's question: {user_question}
    """
    response = client.models.generate_content(model=MODEL, contents=prompt)
    return response.text