from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

model = SentenceTransformer("all-MiniLM-L6-v2")


def resume_compare(
    resume_text,
    job_description,
    matching_skills=None,
    job_skills=None
):

    # -----------------------------------
    # Semantic similarity
    # -----------------------------------

    resume_embedding = model.encode(
        resume_text,
        convert_to_tensor=True
    )

    job_embedding = model.encode(
        job_description,
        convert_to_tensor=True
    )

    similarity = cos_sim(
        resume_embedding,
        job_embedding
    ).item()

    # Convert similarity to percentage
    semantic_score = max(
        0,
        min(100, similarity * 100)
    )


    # -----------------------------------
    # Skill match
    # -----------------------------------

    if job_skills:

        job_skill_count = len(job_skills)

        matching_skill_count = len(
            matching_skills or []
        )

        if job_skill_count > 0:

            skill_score = (
                matching_skill_count /
                job_skill_count
            ) * 100

        else:

            skill_score = 0

    else:

        skill_score = semantic_score


    # -----------------------------------
    # Final score
    # -----------------------------------

    final_score = (

        skill_score * 0.70

        +

        semantic_score * 0.30

    )


    return final_score