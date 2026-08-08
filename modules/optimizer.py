import re


# =====================================================
# SKILL CATEGORIES
# =====================================================

SKILL_CATEGORIES = {

    # =================================================
    # Technical Skills & Tools
    # =================================================

    "Technical & Tools": {

        # Data / Analytics
        "python",
        "sql",
        "excel",
        "power bi",
        "powerbi",
        "tableau",
        "data analysis",
        "data analytics",
        "data visualization",
        "machine learning",
        "statistics",
        "statistical analysis",
        "data cleaning",
        "data preprocessing",
        "business intelligence",
        "reporting",
        "dashboard",
        "dashboards",
        "data modeling",

        # Programming / Development
        "javascript",
        "java",
        "c++",
        "c#",
        "php",
        "html",
        "html5",
        "css",
        "css3",
        "react",
        "node.js",
        "node",
        "flask",
        "django",
        "git",
        "github",
        "api",
        "rest api",
        "mongodb",
        "mysql",
        "postgresql",

        # Design
        "figma",
        "adobe illustrator",
        "adobe photoshop",
        "graphic design",
        "ui design",
        "ux design",
        "ui/ux",
        "user experience",
        "user research",
        "wireframing",
        "prototyping",
        "visual design",
        "branding"
    },


    # =================================================
    # Soft Skills
    # =================================================

    "Soft Skills": {

        "communication",
        "teamwork",
        "leadership",
        "problem solving",
        "problem-solving",
        "critical thinking",
        "time management",
        "presentation",
        "negotiation",
        "customer service",
        "adaptability",
        "creativity",
        "creative thinking",
        "collaboration",
        "decision making",
        "decision-making"
    },


    # =================================================
    # Business & Domain Skills
    # =================================================

    "Business & Domain": {

        "business analysis",
        "business strategy",
        "project management",
        "product management",
        "stakeholder management",
        "stakeholder communication",
        "market research",
        "market analysis",
        "financial analysis",
        "operations",
        "operations management",

        # Marketing
        "digital marketing",
        "content marketing",
        "social media marketing",
        "seo",
        "sem",
        "content creation",
        "email marketing",
        "campaign management",
        "brand management",

        # Finance
        "accounting",
        "financial reporting",
        "financial planning",
        "budgeting",
        "forecasting",

        # HR
        "human resources",
        "recruitment",
        "talent acquisition",
        "employee relations",
        "payroll",
        "performance management"
    }
}


# =====================================================
# COMMON WORDS TO IGNORE
# =====================================================

STOP_WORDS = {

    # General words
    "about",
    "above",
    "across",
    "after",
    "again",
    "against",
    "along",
    "also",
    "among",
    "and",
    "any",
    "are",
    "around",
    "because",
    "been",
    "before",
    "being",
    "below",
    "between",
    "both",
    "but",
    "can",
    "could",
    "during",
    "each",
    "either",
    "for",
    "from",
    "further",
    "get",
    "give",
    "given",
    "have",
    "having",
    "here",
    "how",
    "into",
    "its",
    "just",
    "more",
    "most",
    "much",
    "must",
    "need",
    "not",
    "now",
    "of",
    "off",
    "on",
    "once",
    "only",
    "or",
    "other",
    "our",
    "out",
    "over",
    "same",
    "should",
    "since",
    "some",
    "such",
    "than",
    "that",
    "the",
    "their",
    "them",
    "then",
    "there",
    "these",
    "they",
    "this",
    "those",
    "through",
    "to",
    "under",
    "until",
    "use",
    "used",
    "using",
    "very",
    "was",
    "were",
    "what",
    "when",
    "where",
    "which",
    "while",
    "who",
    "will",
    "with",
    "within",
    "would",
    "you",
    "your",

    # Job description filler
    "candidate",
    "candidates",
    "position",
    "positions",
    "role",
    "roles",
    "job",
    "jobs",
    "company",
    "organization",
    "organization's",
    "team",
    "teams",
    "work",
    "working",
    "employee",
    "employees",
    "responsibilities",
    "responsibility",
    "requirements",
    "requirement",
    "experience",
    "experienced",
    "skills",
    "skill",
    "ability",
    "abilities",
    "knowledge",
    "preferred",
    "prefer",
    "desirable",
    "required",
    "strong",
    "excellent",
    "successful",
    "successfully",
    "including",
    "includes",
    "provide",
    "providing",
    "support",
    "closely",
    "clear",
    "degree",
    "related",
    "field",
    "environment",
    "professional",
    "professionals",
    "looking",
    "seeking",

    # Generic action words
    "develop",
    "developed",
    "developing",
    "manage",
    "managed",
    "managing",
    "create",
    "created",
    "creating",
    "build",
    "built",
    "building",
    "perform",
    "performed",
    "performing",
    "analyze",
    "analyzed",
    "analyzing",
    "ensure",
    "ensuring",
    "maintain",
    "maintaining"
}


# =====================================================
# HELPER: CHECK WHETHER A SKILL EXISTS IN TEXT
# =====================================================

def skill_exists(skill, text):

    skill = skill.lower()

    text = text.lower()

    # Handle skills containing special characters
    pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"

    return bool(re.search(pattern, text))


# =====================================================
# MAIN OPTIMIZER
# =====================================================

def optimize_resume(resume_text, job_description):

    suggestions = []

    resume_lower = resume_text.lower()

    job_lower = job_description.lower()


    # =================================================
    # 1. STRONG ACTION VERBS
    # =================================================

    weak_words = [

        "worked",
        "helped",
        "responsible",
        "did",
        "made",
        "handled",
        "participated",
        "assisted",
        "involved"

    ]

    found_weak_words = []


    for word in weak_words:

        if re.search(
            r"\b" + re.escape(word) + r"\b",
            resume_lower
        ):

            found_weak_words.append(word)


    if found_weak_words:

        suggestions.append({

            "title": "Use Stronger Action Verbs",

            "items": [

                (
                    f"Replace '{word}' with stronger verbs such as "
                    "Developed, Designed, Implemented, Led, "
                    "Created, Optimized or Coordinated."
                )

                for word in found_weak_words

            ]

        })


    # =================================================
    # 2. RESUME LENGTH
    # =================================================

    word_count = len(
        re.findall(r"\w+", resume_text)
    )


    if word_count < 250:

        suggestions.append({

            "title": "Resume Length",

            "items": [

                "Your resume appears quite short.",

                (
                    "Consider adding relevant projects, "
                    "internships, certifications or achievements."
                ),

                (
                    "Add measurable results to demonstrate "
                    "the impact of your work."
                )

            ]

        })


    elif word_count > 1000:

        suggestions.append({

            "title": "Resume Length",

            "items": [

                "Your resume contains a large amount of text.",

                (
                    "Remove information that is not relevant "
                    "to the target position."
                ),

                (
                    "Keep your most relevant experience "
                    "and achievements prominent."
                )

            ]

        })


    else:

        suggestions.append({

            "title": "Resume Length",

            "items": [

                "Your resume has a reasonable amount of content.",

                (
                    "Focus on keeping the content relevant "
                    "to the target position."
                )

            ]

        })


    # =================================================
    # 3. SKILL ANALYSIS
    # =================================================

    skill_analysis = {}


    for category, skills in SKILL_CATEGORIES.items():

        job_skills = []

        resume_skills = []


        for skill in skills:

            if skill_exists(skill, job_lower):

                job_skills.append(skill)


            if skill_exists(skill, resume_lower):

                resume_skills.append(skill)


        matching = [

            skill

            for skill in job_skills

            if skill in resume_skills

        ]


        missing = [

            skill

            for skill in job_skills

            if skill not in resume_skills

        ]


        if matching or missing:

            skill_analysis[category] = {

                "matching": matching,

                "missing": missing

            }


    # =================================================
    # 4. MATCHING SKILLS
    # =================================================

    for category, data in skill_analysis.items():

        if data["matching"]:

            suggestions.append({

                "title": f"Matching Skills — {category}",

                "items": [

                    (
                        f"Your resume already includes "
                        f"'{skill}', which is relevant to this job."
                    )

                    for skill in data["matching"][:12]

                ]

            })


    # =================================================
    # 5. MISSING SKILLS
    # =================================================

    for category, data in skill_analysis.items():

        if data["missing"]:

            suggestions.append({

                "title": f"Potential Missing Skills — {category}",

                "items": [

                    (
                        f"'{skill}' appears relevant to the "
                        "job description but was not detected "
                        "in your resume. Add it only if you "
                        "genuinely have this skill."
                    )

                    for skill in data["missing"][:10]

                ]

            })


    # =================================================
    # 6. PROFESSIONAL SUMMARY
    # =================================================

    summary_terms = [

        "professional summary",
        "summary",
        "profile",
        "objective"

    ]


    has_summary = any(

        term in resume_lower

        for term in summary_terms

    )


    if not has_summary:

        suggestions.append({

            "title": "Professional Summary",

            "items": [

                (
                    "Consider adding a short professional "
                    "summary at the top of your resume."
                ),

                (
                    "Mention your background, strongest "
                    "relevant skills and target role."
                ),

                (
                    "Keep the summary concise and tailored "
                    "to the job description."
                )

            ]

        })


    else:

        suggestions.append({

            "title": "Professional Summary",

            "items": [

                (
                    "A summary or profile section was detected."
                ),

                (
                    "Make sure it clearly communicates your "
                    "background, relevant skills and career target."
                )

            ]

        })


    # =================================================
    # 7. QUANTIFIABLE ACHIEVEMENTS
    # =================================================

    numbers = re.findall(

        r"\b\d+(?:\.\d+)?%?\b",

        resume_text

    )


    if len(numbers) < 2:

        suggestions.append({

            "title": "Add Measurable Achievements",

            "items": [

                (
                    "Your resume contains few measurable results."
                ),

                (
                    "Where possible, include percentages, "
                    "project counts, users reached, time saved "
                    "or performance improvements."
                ),

                (
                    "Example: 'Reduced processing time by 25%.'"
                )

            ]

        })


    else:

        suggestions.append({

            "title": "Quantifiable Achievements",

            "items": [

                (
                    "Your resume includes measurable information."
                ),

                (
                    "Continue using numbers and results to "
                    "demonstrate the impact of your work."
                )

            ]

        })


    # =================================================
    # 8. SKILLS SECTION
    # =================================================

    skill_headers = [

        "skills",
        "technical skills",
        "core skills",
        "competencies",
        "expertise"

    ]


    has_skills_section = any(

        term in resume_lower

        for term in skill_headers

    )


    if not has_skills_section:

        suggestions.append({

            "title": "Skills Section",

            "items": [

                (
                    "Consider adding a clearly labeled "
                    "Skills section."
                ),

                (
                    "Prioritize skills that are directly "
                    "relevant to the target position."
                )

            ]

        })


    # =================================================
    # 9. EXPERIENCE / PROJECTS
    # =================================================

    experience_terms = [

        "experience",
        "employment",
        "work experience",
        "internship",
        "projects",
        "project"

    ]


    has_experience = any(

        term in resume_lower

        for term in experience_terms

    )


    if not has_experience:

        suggestions.append({

            "title": "Experience & Projects",

            "items": [

                (
                    "No obvious Experience or Projects "
                    "section was detected."
                ),

                (
                    "Add relevant projects, internships, "
                    "freelance work or practical experience "
                    "where applicable."
                )

            ]

        })


    # =================================================
    # 10. ATS OPTIMIZATION
    # =================================================

    suggestions.append({

        "title": "ATS Optimization Tips",

        "items": [

            (
                "Use standard headings such as Summary, "
                "Skills, Experience, Education and Projects."
            ),

            (
                "Avoid placing important information inside "
                "images or complex graphics."
            ),

            (
                "Use consistent dates, job titles and formatting."
            ),

            (
                "Tailor important skills and terminology "
                "to each job description."
            ),

            (
                "Use clear bullet points instead of large "
                "paragraphs."
            )

        ]

    })


    # =================================================
    # 11. BULLET POINTS
    # =================================================

    bullet_lines = re.findall(

        r"(?:^|\n)\s*[-•*]\s*(.+)",

        resume_text

    )


    if bullet_lines:

        short_bullets = [

            bullet

            for bullet in bullet_lines

            if len(bullet.split()) < 8

        ]


        if short_bullets:

            suggestions.append({

                "title": "Improve Resume Bullet Points",

                "items": [

                    (
                        "Some bullet points appear very short."
                    ),

                    (
                        "Try using the structure: "
                        "Action + Task + Result."
                    ),

                    (
                        "Example: 'Developed a dashboard "
                        "that reduced manual reporting "
                        "time by 30%.'"
                    )

                ]

            })


        else:

            suggestions.append({

                "title": "Resume Bullet Points",

                "items": [

                    (
                        "Your resume uses bullet points effectively."
                    ),

                    (
                        "Continue focusing each bullet on an "
                        "action, responsibility and measurable result."
                    )

                ]

            })


    else:

        suggestions.append({

            "title": "Resume Bullet Points",

            "items": [

                (
                    "Consider using concise bullet points "
                    "for experience and project descriptions."
                ),

                (
                    "Start bullets with strong action verbs."
                )

            ]

        })


    # =================================================
    # RETURN RESULTS
    # =================================================

    return suggestions