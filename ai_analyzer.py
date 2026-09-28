import os
from dotenv import load_dotenv
from google import genai

load_dotenv()


client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def analyze_resume(resume, job_description):

    prompt = f"""
You are an AI recruitment assistant.

Analyze the candidate's resume against
the job description.

JOB DESCRIPTION:
{job_description}

RESUME:
{resume}

Return the answer in the following format:

1. Matching Skills
2. Missing Skills
3. Candidate Strengths
4. Areas to Improve
5. Overall Recommendation

Keep the response clear and professional.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text