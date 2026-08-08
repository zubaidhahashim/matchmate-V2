# MatchMate V2

### Resume Analysis & Interview Preparation Platform

MatchMate is a resume analysis and career preparation web application designed to help job seekers understand how well their resume matches a target job and improve their chances of being interview-ready.

The application analyzes resumes against job descriptions, identifies matching and missing skills, provides resume optimization suggestions, and generates personalized interview questions based on the candidate's resume and target role.

---

## Features

### Resume Analysis

- Upload resumes in PDF format
- Paste a target job description
- Calculate a resume-job match score
- Identify matching skills
- Identify missing skills
- Generate personalized recommendations

### Resume Optimizer

- Analyze resume content
- Identify potential improvements
- Suggest stronger action verbs
- Check resume length
- Identify potentially missing job-related keywords
- Provide ATS optimization tips
- Suggest improvements for resume bullet points

### Interview Coach

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

### Reports

- View the latest resume analysis
- Review match score
- View matching and missing skills
- Review personalized recommendations

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Flask | Web application framework |
| HTML5 | Frontend structure |
| CSS3 | Styling and responsive UI |
| JavaScript | Frontend interactions |
| Sentence Transformers | Resume-job semantic similarity |
| PyMuPDF | PDF text extraction |
| JSON | Data exchange between frontend and backend |

---

## Project Structure

```text
MatchMate/
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
│   │
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
├── uploads/
│
├── app.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
---

How It Works
Resume Analysis
Upload a resume in PDF format.
Paste the target job description.
Resume text is extracted using PyMuPDF.
Skills are extracted from both the resume and job description.
Matching and missing skills are identified.
Semantic similarity between the resume and job description is calculated.
A combined resume match score is generated.
Personalized recommendations are displayed.
The latest analysis is available through the Reports section.
Resume Optimizer
Upload a resume.
Paste the target job description.
Resume content is analyzed.
The application identifies potential improvements.
ATS and content optimization suggestions are displayed.
Interview Coach
Upload your resume.
Paste the target job description.
Enter the target job role.
Select your experience level.
Select the interview type.
Select the number of questions.
MatchMate generates personalized interview questions based on the provided information.
Match Score

The resume match score considers both:

Skill alignment between the resume and job description
Semantic similarity between the resume and job description

This provides a more meaningful indication of how closely a resume matches a particular job.

Installation
1. Clone the repository
git clone https://github.com/YOUR_USERNAME/MatchMate.git
2. Move into the project directory
cd MatchMate
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

The project intentionally keeps the workflow simple and focuses on practical features for job seekers.

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

BCA Graduate 

License

This project is licensed under the MIT License.
