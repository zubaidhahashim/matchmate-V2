def generate_report(resume_skills, job_skills):

    matching_skills = []
    missing_skills = []

    for skill in job_skills:
        if skill in resume_skills:
            matching_skills.append(skill)
        else:
            missing_skills.append(skill)

    return matching_skills, missing_skills