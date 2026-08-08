# MatchMate V2

### Resume Analysis & Interview Preparation Platform

MatchMate is a career preparation web application that helps job seekers analyze their resumes, compare them with job descriptions, improve resume content, and practice personalized interview questions.

---

## Features

### Resume Analysis

- Upload a resume in PDF format
- Paste a job description
- Calculate a resume-job match score
- Identify matching skills
- Identify missing skills
- Generate personalized recommendations

### Resume Optimizer

- Analyze resume content
- Identify potential improvements
- Suggest stronger action verbs
- Check resume length
- Identify relevant keywords
- Provide ATS optimization tips
- Improve resume bullet points

### Interview Coach

- Generate personalized interview questions
- Questions based on the resume and target job
- Select target job role
- Select experience level
- Choose interview type
- Choose number of questions

### Reports

- View the latest resume analysis
- View match score
- View matching skills
- View missing skills
- View recommendations

---

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Flask | Web framework |
| HTML5 | Frontend structure |
| CSS3 | Styling |
| JavaScript | Frontend interactions |
| Sentence Transformers | Semantic similarity |
| PyMuPDF | PDF text extraction |

---

## How It Works

### Resume Analysis

1. Upload your resume in PDF format.
2. Paste the target job description.
3. MatchMate extracts the resume text.
4. Skills are extracted from the resume and job description.
5. Matching and missing skills are identified.
6. Semantic similarity is calculated.
7. A match score is generated.
8. Personalized recommendations are displayed.

### Resume Optimizer

1. Upload your resume.
2. Paste the target job description.
3. MatchMate analyzes your resume.
4. Potential improvements are identified.
5. ATS optimization suggestions are displayed.

### Interview Coach

1. Upload your resume.
2. Paste the target job description.
3. Enter the target job role.
4. Select your experience level.
5. Select the interview type.
6. Select the number of questions.
7. MatchMate generates personalized interview questions.

---

## Project Structure

    MatchMate-V2/
    ├── modules/
    │   ├── interview_coach.py
    │   ├── optimizer.py
    │   ├── pdf_reader.py
    │   ├── recommendations.py
    │   ├── report_generator.py
    │   ├── similarity.py
    │   └── skill_extractor.py
    │
    ├── static/
    │   ├── css/
    │   │   └── style.css
    │   └── js/
    │       ├── analysis.js
    │       ├── interview.js
    │       └── optimizer.js
    │
    ├── templates/
    │   ├── about.html
    │   ├── analysis.html
    │   ├── base.html
    │   ├── index.html
    │   ├── interview.html
    │   ├── optimizer.html
    │   └── reports.html
    │
    ├── app.py
    ├── requirements.txt
    ├── README.md
    ├── LICENSE
    └── .gitignore

---

## Installation

### 1. Clone the repository

    git clone https://github.com/zubaidhahashim/matchmate-V2.git

### 2. Move into the project directory

    cd matchmate-V2

### 3. Create a virtual environment

    python -m venv .venv

### 4. Activate the virtual environment

**Windows:**

    .venv\Scripts\activate

**macOS / Linux:**

    source .venv/bin/activate

### 5. Install dependencies

    pip install -r requirements.txt

### 6. Run the application

    python app.py

The application will be available at:

    http://127.0.0.1:5000

---

## Usage

After starting MatchMate, users can access:

- **Home** — Application overview
- **Resume Analysis** — Analyze resume-job compatibility
- **Resume Optimizer** — Improve resume content
- **Interview Coach** — Practice interview questions
- **Reports** — View the latest analysis report
- **About** — Project information

---

## Current Version

### MatchMate V2

MatchMate V2 is built with Flask and focuses on three main career preparation features:

1. Resume Analysis
2. Resume Optimization
3. Interview Preparation

The goal is to provide simple and practical tools that help job seekers prepare for applications and interviews.

---

## Future Improvements

- More comprehensive skill extraction
- Improved job-specific recommendations
- More interview question categories
- Resume report export
- Job application tracking
- Support for additional document formats

---

## Author

**Zubaidha Hashim**

BCA Graduate 

---

## License

This project is licensed under the MIT License.
