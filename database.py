import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    connection = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )

    return connection



def save_candidate(
    filename,
    resume_text,
    job_description,
    match_score,
    analysis
):

    # Convert to normal Python float
    match_score = float(match_score)

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO candidates
        (
            filename,
            resume_text,
            job_description,
            match_score,
            analysis
        )
        VALUES (%s, %s, %s, %s, %s)
    """

    cursor.execute(
        query,
        (
            filename,
            resume_text,
            job_description,
            match_score,
            analysis
        )
    )

    connection.commit()

    cursor.close()
    connection.close()


