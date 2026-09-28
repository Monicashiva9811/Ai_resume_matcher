from sklearn.metrics.pairwise import cosine_similarity
from embeddings import create_embedding


def calculate_match(resume_text, job_description):

    resume_embedding = create_embedding(resume_text)

    job_embedding = create_embedding(job_description)

    similarity = cosine_similarity(
        [resume_embedding],
        [job_embedding]
    )[0][0]

    # Convert NumPy value to normal Python float
    match_percentage = float(
        round(float(similarity) * 100, 2)
    )

    return match_percentage