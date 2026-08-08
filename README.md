# MatchMate V2

### Resume Analysis & Interview Preparation Platform

MatchMate is a resume analysis and career preparation web application designed to help job seekers understand how well their resume matches a target job and prepare for interviews.

The application analyzes resumes against job descriptions, identifies matching and missing skills, provides resume optimization suggestions, and generates personalized interview questions based on the candidate's resume and target role.

---

## Features

### 📊 Resume Analysis

- Upload resumes in PDF format
- Paste a target job description
- Calculate a resume-job match score
- Identify matching skills
- Identify missing skills
- Generate personalized recommendations

### ✨ Resume Optimizer

- Analyze resume content
- Identify potential improvements
- Suggest stronger action verbs
- Check resume length
- Identify potentially missing job-related keywords
- Provide ATS optimization tips
- Suggest improvements for resume bullet points

### 🎤 Interview Coach

- Generate personalized interview questions
- Questions are based on the candidate's resume and job description
- Select target job role
- Select experience level
- Choose interview type:
  - Technical
  - HR / Behavioral
  - Mixed
- Choose the number of questions
- Questions include categories and difficulty levels

### 📑 Reports

- View the latest resume analysis
- Review match score
- View matching and missing skills
- Review personalized recommendations

---

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Flask | Web application framework |
| HTML5 | Frontend structure |
| CSS3 | Styling and responsive UI |
| JavaScript | Frontend interactions |
| Sentence Transformers | Resume-job semantic similarity |
| PyMuPDF | PDF text extraction |
| JSON | Data exchange between frontend and backend |

---

## How It Works

### Resume Analysis

1. Upload a resume in PDF format.
2. Paste the target job description.
3. Resume text is extracted using PyMuPDF.
4. Skills are extracted from both the resume and job description.
5. Matching and missing skills are identified.
6. Semantic similarity between the resume and job description is calculated.
7. A combined resume match score is generated.
8. Personalized recommendations are displayed.
9. The latest analysis is available through the Reports section.

### Resume Optimizer

1. Upload a resume.
2. Paste the target job description.
3. Resume content is analyzed.
4. The application identifies potential improvements.
5. ATS and content optimization suggestions are displayed.

### Interview Coach

1. Upload your resume.
2. Paste the target job description.
3. Enter the target job role.
4. Select your experience level.
5. Select the interview type.
6. Select the number of questions.
7. MatchMate generates personalized interview questions based on the provided information.

---

## Match Score

The resume match score considers both:

- **Skill alignment** between the resume and job description
- **Semantic similarity** between the resume and job description

This provides a more meaningful indication of how closely a resume matches a particular job.

---

## Project Structure

```text
MatchMate-V2/
│
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
```
Installation
1. Clone the repository
git clone https://github.com/zubaidhahashim/matchmate-V2.git
2. Move into the project directory
cd matchmate-V2
3. Create a virtual environment
python -m venv .venv
4. Activate the virtual environment
Windows
.venv\Scripts\activate
macOS / Linux
source .venv/bin/activate
5. Install dependencies
pip install -r requirements.txt
6. Run the application
python app.py

The application will be available at:

http://127.0.0.1:5000
Usage

After starting the application, users can access:

Home — overview of MatchMate
Resume Analysis — analyze resume-job compatibility
Resume Optimizer — improve resume content
Interview Coach — generate personalized interview questions
Reports — view the latest analysis report
About — information about the project
Current Version
MatchMate V2

The current version uses a Flask-based web interface and focuses on three core career preparation features:

Resume Analysis
Resume Optimization
Interview Preparation

The project keeps the workflow simple and focuses on practical tools for job seekers.

Future Improvements

Potential future enhancements include:

More comprehensive skill extraction
Additional resume analysis metrics
Improved job-specific recommendations
More interview question categories
Resume report export
Job application tracking
Support for additional document formats
Author

Zubaidha Hashim

BCA Graduate | Aspiring Data Analyst

License

This project is licensed under the MIT License.
