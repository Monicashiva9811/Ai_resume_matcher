import os
import shutil

from fastapi import FastAPI, UploadFile, File, Form
from pdf_reader import extract_text
from matcher import calculate_match
from ai_analyzer import analyze_resume
from database import save_candidate


app = FastAPI(
    title="AI Resume Matcher"
)


@app.get("/")
def home():

    return {
        "message": "AI Resume Matcher is running"
    }


@app.post("/analyze-resume")
async def analyze(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):

    # Create uploads folder if it does not exist
    os.makedirs("uploads", exist_ok=True)

    # Create file path
    file_path = os.path.join(
        "uploads",
        resume.filename
    )

    # Save uploaded resume
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(
            resume.file,
            buffer
        )

    # Extract text from PDF
    resume_text = extract_text(file_path)

    # Calculate similarity score
    match_score = calculate_match(
        resume_text,
        job_description
    )

    # Get AI analysis
    ai_result = analyze_resume(
        resume_text,
        job_description
    )

    # Save result to PostgreSQL
    save_candidate(
        resume.filename,
        resume_text,
        job_description,
        match_score,
        ai_result
    )

    return {
        "filename": resume.filename,
        "match_score": f"{match_score}%",
        "analysis": ai_result
    }