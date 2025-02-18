from fastapi import FastAPI, UploadFile, File
import os
import uvicorn
from pdf_processing import extract_text_from_pdf
from summarizer import summarize_text
from qa_system import get_answer_from_text

app = FastAPI()
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        f.write(file.file.read())
    text = extract_text_from_pdf(file_path)
    return {"filename": file.filename, "extracted_text": text}

@app.post("/summarize/")
async def summarize_pdf(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f: 
        f.write(file.file.read())       
    text = extract_text_from_pdf(file_path) 
    summary = summarize_text(text)
    return {"filename": file.filename, "summaray": summary}

@app.post("/ask/")
async def ask_question(file: UploadFile = File(...), question: str = "What is this PDF about?"):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        f.write(file.file.read())
    text = extract_text_from_pdf(file_path)
    answer = get_answer_from_text(text, question)
    return {"filename": file.filename, "question": question, "answer": answer}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
