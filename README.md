# MatchMate 

### Intelligent Resume Screening Platform

MatchMate is an AI-powered resume screening application that helps job seekers evaluate how well their resume matches a specific job description. The application uses Natural Language Processing (NLP) and semantic similarity to identify matching skills, highlight skill gaps, and generate personalized recommendations.

---

## Features

- Upload resumes in PDF format
- Paste any job description
- AI-powered semantic similarity analysis
- Automatic skill extraction
- Matching and missing skill identification
- Personalized improvement recommendations
- Downloadable analysis report
- Clean and user-friendly Streamlit interface

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Streamlit | Web application framework |
| Sentence Transformers | Semantic similarity analysis |
| spaCy | Natural Language Processing |
| PyMuPDF | PDF text extraction |

---

## Project Structure

```
MatchMate/
│
├── modules/
│   ├── pdf_reader.py
│   ├── recommendations.py
│   ├── report_generator.py
│   ├── similarity.py
│   └── skill_extractor.py
│
├── app.py
├── streamlit_app.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## How It Works

1. Upload a resume in PDF format.
2. Paste a job description into the application.
3. Resume text is extracted using PyMuPDF.
4. Semantic similarity between the resume and job description is calculated.
5. Skills are extracted from both documents.
6. Matching and missing skills are identified.
7. Personalized recommendations are generated.
8. Users can download the analysis report.

---

## Future Enhancements (Version 2)

- AI-powered dynamic skill extraction
- Automatic job role detection
- Modern HTML/CSS user interface
- Interactive analytics dashboard
- AI-generated resume improvement suggestions
- Multiple resume comparison and ranking
- Enhanced PDF report generation

---

## Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/MatchMate-AI.git
```

Move into the project directory

```bash
cd MatchMate-AI
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run streamlit_app.py
```

---

## Author

**Zubaidha Hashim**

BCA Graduate | Aspiring Data Analyst

---

## License

This project is licensed under the MIT License.