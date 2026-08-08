from flask import Flask, render_template, request, jsonify, session
import os

from modules.interview_coach import generate_questions
from modules.optimizer import optimize_resume
from modules.pdf_reader import read_pdf
from modules.skill_extractor import extract_skills
from modules.similarity import resume_compare
from modules.report_generator import generate_report
from modules.recommendations import get_recommendations


app = Flask(__name__)


# =====================================================
# FLASK SESSION
# =====================================================

app.secret_key = "matchmate-development-key"


# =====================================================
# CONFIGURATION
# =====================================================

UPLOAD_FOLDER = "uploads"

ALLOWED_EXTENSIONS = {"pdf"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)


# =====================================================
# HOME
# =====================================================

@app.route("/")
def home():

    return render_template(
        "index.html"
    )


# =====================================================
# RESUME ANALYSIS PAGE
# =====================================================

@app.route("/analysis")
def analysis():

    return render_template(
        "analysis.html"
    )


# =====================================================
# RESUME OPTIMIZER
# =====================================================

@app.route(
    "/optimizer",
    methods=["GET", "POST"]
)
def optimizer():

    # Open optimizer page

    if request.method == "GET":

        return render_template(
            "optimizer.html"
        )


    # -----------------------------------------
    # Get uploaded resume
    # -----------------------------------------

    resume = request.files["resume"]

    job_description = request.form[
        "job_description"
    ]


    # -----------------------------------------
    # Save resume
    # -----------------------------------------

    resume_path = os.path.join(

        app.config["UPLOAD_FOLDER"],

        resume.filename

    )

    resume.save(
        resume_path
    )


    # -----------------------------------------
    # Read resume
    # -----------------------------------------

    resume_text = read_pdf(
        resume_path
    )


    # -----------------------------------------
    # Generate suggestions
    # -----------------------------------------

    suggestions = optimize_resume(

        resume_text,

        job_description

    )


    # -----------------------------------------
    # Return suggestions
    # -----------------------------------------

    return jsonify({

        "suggestions": suggestions

    })


# =====================================================
# INTERVIEW COACH
# =====================================================

@app.route(
    "/interview",
    methods=["GET", "POST"]
)
def interview():

    # Open interview page

    if request.method == "GET":

        return render_template(
            "interview.html"
        )


    # -----------------------------------------
    # Get form data
    # -----------------------------------------

    job_role = request.form[
        "job_role"
    ]

    experience_level = request.form[
        "experience_level"
    ]

    interview_type = request.form[
        "interview_type"
    ]

    question_count = request.form[
        "question_count"
    ]

    job_description = request.form[
        "job_description"
    ]


    # -----------------------------------------
    # Get resume
    # -----------------------------------------

    resume = request.files[
        "resume"
    ]


    # -----------------------------------------
    # Save resume
    # -----------------------------------------

    resume_path = os.path.join(

        app.config["UPLOAD_FOLDER"],

        resume.filename

    )

    resume.save(
        resume_path
    )


    # -----------------------------------------
    # Read resume
    # -----------------------------------------

    resume_text = read_pdf(
        resume_path
    )


    # -----------------------------------------
    # Generate personalized questions
    # -----------------------------------------

    questions = generate_questions(

        resume_text,

        job_description,

        job_role,

        experience_level,

        interview_type,

        question_count

    )


    # -----------------------------------------
    # Return questions
    # -----------------------------------------

    return jsonify({

        "questions": questions

    })


# =====================================================
# REPORTS
# =====================================================

@app.route("/reports")
def reports():

    report = session.get(
        "latest_report"
    )


    return render_template(

        "reports.html",

        report=report

    )


# =====================================================
# ABOUT
# =====================================================

@app.route("/about")
def about():

    return render_template(
        "about.html"
    )


# =====================================================
# RESUME ANALYSIS
# =====================================================

@app.route(
    "/analyze",
    methods=["POST"]
)
def analyze():

    # -----------------------------------------
    # Get uploaded resume
    # -----------------------------------------

    resume = request.files[
        "resume"
    ]

    job_description = request.form[
        "job_description"
    ]


    # -----------------------------------------
    # Save resume
    # -----------------------------------------

    resume_path = os.path.join(

        app.config["UPLOAD_FOLDER"],

        resume.filename

    )

    resume.save(
        resume_path
    )


    # -----------------------------------------
    # Extract resume text
    # -----------------------------------------

    resume_text = read_pdf(
        resume_path
    )


    # -----------------------------------------
    # Extract skills
    # -----------------------------------------

    resume_skills = extract_skills(
        resume_text
    )

    job_skills = extract_skills(
        job_description
    )


    # -----------------------------------------
    # Find matching and missing skills
    # -----------------------------------------

    matching_skills, missing_skills = generate_report(

        resume_skills,

        job_skills

    )


    # -----------------------------------------
    # Calculate match score
    #
    # Score now considers:
    #
    # 70% = Skill Match
    # 30% = Semantic Similarity
    # -----------------------------------------

    score = resume_compare(

        resume_text,

        job_description,

        matching_skills,

        job_skills

    )


    # -----------------------------------------
    # Generate recommendations
    # -----------------------------------------

    recommendations = get_recommendations(

        missing_skills

    )


    # -----------------------------------------
    # Prepare report
    # -----------------------------------------

    report = {

        "score": round(
            score,
            2
        ),

        "matching_skills":
            matching_skills,

        "missing_skills":
            missing_skills,

        "recommendations":
            recommendations

    }


    # -----------------------------------------
    # Save latest report
    # -----------------------------------------

    session[
        "latest_report"
    ] = report


    # -----------------------------------------
    # Return result
    # -----------------------------------------

    return jsonify(
        report
    )


# =====================================================
# RUN APPLICATION
# =====================================================

if __name__ == "__main__":

    app.run(
        debug=True
    )