from flask import Flask, render_template, request, jsonify

import os

from modules.pdf_reader import read_pdf
from modules.skill_extractor import extract_skills
from modules.similarity import resume_compare
from modules.report_generator import generate_report
from modules.recommendations import get_recommendations

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"pdf"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analysis")
def analysis():
    return render_template("analysis.html")


@app.route("/optimizer")
def optimizer():
    return render_template("optimizer.html")


@app.route("/interview")
def interview():
    return render_template("interview.html")


@app.route("/roadmap")
def roadmap():
    return render_template("roadmap.html")


@app.route("/reports")
def reports():
    return render_template("reports.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/analyze", methods=["POST"])
def analyze():

    resume = request.files["resume"]

    job_description = request.form["job_description"]

    resume_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        resume.filename
    )

    resume.save(resume_path)

    resume_text = read_pdf(resume_path)

    score = resume_compare(
        resume_text,
        job_description
    )

    resume_skills = extract_skills(resume_text)

    job_skills = extract_skills(job_description)

    matching_skills, missing_skills = generate_report(
        resume_skills,
        job_skills
    )

    recommendations = get_recommendations(
        missing_skills
    )

    return jsonify({

    "score": round(score, 2),

    "matching_skills": matching_skills,

    "missing_skills": missing_skills,

    "recommendations": recommendations

})
if __name__ == "__main__":
    app.run(debug=True)