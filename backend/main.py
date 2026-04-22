from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import pdfplumber
import io
from mock_client import summarize_text, generate_quiz, chat_with_notes

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

extracted_texts = {}

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    contents = await file.read()
    text = ""
    with pdfplumber.open(io.BytesIO(contents)) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    if not text.strip():
        return {"error": "Could not extract text from PDF."}
    extracted_texts[file.filename] = text
    return {"filename": file.filename, "message": "PDF uploaded successfully!", "preview": text[:300]}

@app.post("/summarize")
async def summarize(filename: str = Form(...)):
    text = extracted_texts.get(filename)
    if not text:
        return {"error": "File not found. Please upload first."}
    summary = summarize_text(text)
    return {"summary": summary}

@app.post("/quiz")
async def quiz(filename: str = Form(...)):
    text = extracted_texts.get(filename)
    if not text:
        return {"error": "File not found. Please upload first."}
    questions = generate_quiz(text)
    return {"quiz": questions}

@app.post("/chat")
async def chat(filename: str = Form(...), question: str = Form(...)):
    text = extracted_texts.get(filename)
    if not text:
        return {"error": "File not found. Please upload first."}
    answer = chat_with_notes(text, question)
    return {"answer": answer}

@app.get("/")
def root():
    return {"message": "StudyBuddy API is running! 🎓"}
