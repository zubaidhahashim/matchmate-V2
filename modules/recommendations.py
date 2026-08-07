RECOMMENDATIONS = {
    "Python": "Add more Python projects to your portfolio.",
    "SQL": "Practice JOINs, GROUP BY, and Window Functions.",
    "Power BI": "Create 2–3 Power BI dashboard projects.",
    "Excel": "Learn Pivot Tables and Power Query.",
    "Tableau": "Learn Tableau and build one dashboard project.",
    "Communication": "Highlight teamwork, presentations, or leadership experience.",
    "Problem Solving": "Mention projects where you solved real-world problems.",
    "Git": "Show GitHub repositories with meaningful commit history.",
    "JavaScript": "Build interactive web projects using JavaScript.",
    "React": "Create a React portfolio project."
}


def get_recommendations(missing_skills):

    recommendations = []

    for skill in missing_skills:
        if skill in RECOMMENDATIONS:
            recommendations.append(RECOMMENDATIONS[skill])

    return recommendations