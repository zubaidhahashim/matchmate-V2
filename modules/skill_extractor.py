# Dictionary of supported skills
SKILLS = {
    "python": "Python",
    "sql": "SQL",
    "power bi": "Power BI",
    "excel": "Excel",
    "tableau": "Tableau",
    "communication": "Communication",
    "problem solving": "Problem Solving",
    "git": "Git",
    "javascript": "JavaScript",
    "react": "React",
    "html": "HTML",
    "css": "CSS",
    "mongodb": "MongoDB",
    "figma": "Figma"
}


def extract_skills(text):
    """
    Extracts known skills from the given text.

    Args:
        text (str): Resume or job description text.

    Returns:
        list: List of detected skills.
    """

    # Convert text to lowercase for case-insensitive matching
    text = text.lower()

    found_skills = []

    # Check each skill in the text
    for skill in SKILLS:
        if skill in text:
            found_skills.append(SKILLS[skill])

    return found_skills