import re


def optimize_resume(resume_text, job_description):
    """
    Generates resume improvement suggestions.
    """

    suggestions = []

    # Strong action verbs
    weak_words = [
        "worked",
        "helped",
        "responsible for",
        "did",
        "made"
    ]

    found_weak = []

    for word in weak_words:

        if word.lower() in resume_text.lower():
            found_weak.append(word)

    if found_weak:

        suggestions.append(
            "Replace weak action verbs like "
            + ", ".join(found_weak)
            + " with stronger verbs such as Developed, Designed, Led, Implemented, or Optimized."
        )

    # Resume length

    words = len(re.findall(r"\w+", resume_text))

    if words < 250:

        suggestions.append(
            "Your resume is quite short. Consider adding more project details, achievements, and technical skills."
        )

    elif words > 900:

        suggestions.append(
            "Your resume is lengthy. Try keeping it concise and focused."
        )

    # Job keywords

    job_keywords = set(re.findall(r"\b[A-Za-z+#]+\b", job_description.lower()))

    resume_words = set(re.findall(r"\b[A-Za-z+#]+\b", resume_text.lower()))

    missing = sorted(list(job_keywords - resume_words))

    missing = [w for w in missing if len(w) > 3][:15]

    if missing:

        suggestions.append(
            "Consider adding these relevant keywords if applicable: "
            + ", ".join(missing)
        )

    if not suggestions:

        suggestions.append(
            "Your resume already looks strong. Only minor formatting improvements are recommended."
        )

    return suggestions