import re


# Dictionary of supported skills

SKILLS = {

    # Programming
    "python": "Python",
    "java": "Java",
    "javascript": "JavaScript",
    "c++": "C++",
    "c#": "C#",

    # Web
    "html": "HTML",
    "css": "CSS",
    "react": "React",
    "node.js": "Node.js",
    "flask": "Flask",

    # Data / Analytics
    "sql": "SQL",
    "excel": "Excel",
    "power bi": "Power BI",
    "tableau": "Tableau",
    "data analysis": "Data Analysis",
    "data visualization": "Data Visualization",
    "business intelligence": "Business Intelligence",
    "statistics": "Statistics",
    "machine learning": "Machine Learning",

    # Databases
    "mongodb": "MongoDB",
    "mysql": "MySQL",
    "postgresql": "PostgreSQL",

    # Tools
    "git": "Git",
    "github": "GitHub",
    "figma": "Figma",

    # Professional skills
    "communication": "Communication",
    "problem solving": "Problem Solving",
    "problem-solving": "Problem Solving",
    "leadership": "Leadership",
    "teamwork": "Teamwork",
    "time management": "Time Management",

}


def extract_skills(text):
    """
    Extract known skills from the given text.

    Args:
        text (str): Resume or job description text.

    Returns:
        list: List of detected skills.
    """

    text = text.lower()

    found_skills = []

    for skill, display_name in SKILLS.items():

        # Escape special characters such as + and .
        pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"

        if re.search(pattern, text):

            if display_name not in found_skills:

                found_skills.append(display_name)

    return found_skills