def generate_questions(
    resume_text,
    job_description,
    job_role,
    experience_level,
    interview_type,
    question_count
):

    # ==============================
    # Resume / Experience Questions
    # ==============================

    resume_questions = [

        "Tell me about yourself and your background.",

        "Can you walk me through your resume and highlight "
        "the experience most relevant to this role?",

        "Tell me about one of the projects or experiences "
        "mentioned on your resume.",

        "What was your specific contribution to one of "
        "your projects or previous roles?",

        "What was the biggest challenge you faced in one "
        "of your projects or previous roles, and how did "
        "you overcome it?"

    ]


    # ==============================
    # Job-Specific Questions
    # ==============================

    job_questions = [

        f"Why are you interested in the {job_role} position?",

        f"What do you understand about the responsibilities "
        f"of a {job_role}?",

        f"Which skills from your background make you a good "
        f"fit for this {job_role} position?",

        "Which requirement in the job description do you "
        "think would be most challenging for you, and how "
        "would you prepare for it?",

        f"How would you approach your responsibilities "
        f"during your first few months as a {job_role}?"

    ]


    # ==============================
    # Behavioral Questions
    # ==============================

    behavioral_questions = [

        "What are your greatest strengths?",

        "What is one weakness you are currently working on?",

        "Tell me about a time you had to solve a difficult problem.",

        "Tell me about a time you worked successfully as part of a team.",

        "How do you handle pressure or tight deadlines?",

        "Tell me about a time you received criticism or feedback. "
        "How did you respond?",

        "How do you prioritize when you have multiple tasks "
        "to complete?",

        "Where do you see yourself in the next five years?"

    ]


    # ==============================
    # Role / Problem-Solving Questions
    # ==============================

    role_questions = [

        f"What do you think makes someone successful "
        f"in a {job_role} role?",

        f"How would you handle an unfamiliar task "
        f"in a {job_role} position?",

        "How do you make decisions when you do not have "
        "all the information you need?",

        "How do you keep yourself updated with developments "
        "relevant to your profession?",

        "Describe how you would approach solving an "
        "unexpected problem at work."

    ]


    # ==============================
    # Select Questions
    # ==============================

    questions = []


    if interview_type == "technical":

        questions.extend(resume_questions[:2])

        questions.extend(job_questions)

        questions.extend(role_questions)


    elif interview_type == "hr":

        questions.extend(resume_questions[:3])

        questions.extend(behavioral_questions)

        questions.extend(job_questions[:2])


    else:

        # Mixed interview

        questions.extend(resume_questions[:3])

        questions.extend(job_questions[:3])

        questions.extend(behavioral_questions[:3])

        questions.extend(role_questions[:2])


    # ==============================
    # Remove Duplicates
    # ==============================

    unique_questions = []

    for question in questions:

        if question not in unique_questions:

            unique_questions.append(question)


    # ==============================
    # Limit Question Count
    # ==============================

    return unique_questions[:int(question_count)]