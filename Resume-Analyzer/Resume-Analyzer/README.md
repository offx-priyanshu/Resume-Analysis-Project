# 🚀 AI Resume Analyzer & Matcher

An intelligent Flask-based application that analyzes resumes, extracts technical skills, and provides AI-powered feedback using **Google Gemini Pro**. It also calculates a semantic match score between a resume and a job description.

---

## ✨ Features

- 🔐 **User Authentication**: Secure Login and Registration system.
- 📄 **Multi-format Support**: Upload resumes in **PDF** or **DOCX** format.
- 🛠 **Skill Extraction**: Automatically extracts technical skills using NLP.
- 🤖 **Gemini AI Engine**:
    - **Overall Suitability**: Deep analysis of the candidate's profile.
    - **Actionable Suggestions**: Smart tips to improve your resume.
    - **Quantification Tips**: Guidance on how to add metrics to your experience.
    - **Semantic Match**: Context-aware matching against job descriptions.
- 📊 **Interactive Dashboard**: Track your previous resume analysis history.
- 🛡 **Admin Panel**: Management of users and resume statistics.

---

## 🛠 Tech Stack

- **Backend**: Python, Flask
- **Database**: SQLite (SQLAlchemy)
- **AI/NLP**: Google Gemini Pro API, Spacy, NLTK, Scikit-learn
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Security**: Flask-Bcrypt, CSRF Protection, JWT (for session management)

---

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.9+ installed
- A Google Gemini API Key ([Get it here](https://aistudio.google.com/))

### 2. Installation
Clone the repository and install dependencies:

```bash
# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Setting Up Environment Variables
Create a `.env` file in the root directory:

```env
SECRET_KEY=your_secret_key_here
DATABASE_URL=sqlite:///resume_analyzer.db
GEMINI_API_KEY=your_gemini_api_key_here
```

### 4. Running the Application
Launch the Flask server:

```bash
python app.py
```
Open **`http://127.0.0.1:5000`** in your browser.

---

## 📂 Project Structure

```text
Resume-Analyzer/
├── ai_engine/          # Gemini API Service
├── auth/               # User Authentication logic
├── matcher/            # Traditional & Semantic scoring
├── resume_parser/      # PDF/DOCX text extraction
├── skill_extractor/    # NLP-based skill extraction
├── static/             # CSS, JS, and Images
├── templates/          # HTML Templates
├── uploads/            # Temporary storage for resumes
├── app.py              # Main Application Entry point
├── config.py           # Configuration Management
├── models.py           # Database Models
└── .env                # Secret Keys (Not for Git)
```

---

## 🤝 Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

---

## 📝 License
This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Priyanshu Kumar**  
*Lead Developer & Creator*

- 🌐 [LinkedIn](https://linkedin.com)
- 💻 [GitHub](https://github.com)
- 📧 [Email](mailto:contact@example.com)
