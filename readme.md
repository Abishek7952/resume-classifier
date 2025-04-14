# 🧠 Resume Classifier – ML Web App (FastAPI + Docker + Render)

This project is a **machine learning-powered web application** that predicts the **job-fit category** of uploaded resumes (PDFs) using natural language processing (NLP).

It’s built with:
- 🔍 **Scikit-learn** for training a resume classifier
- ⚡ **FastAPI** for creating a lightweight backend API
- 🐳 **Docker** for containerization
- 🌐 **Render** for live cloud deployment

> 📍 **Live App**: [https://resume-classifier-c1ub.onrender.com/docs](https://resume-classifier-c1ub.onrender.com/docs)

---

## 🚀 Features

- Upload **PDF resumes**
- Automatically extracts text using **PyMuPDF**
- Predicts the candidate's likely role:
  - `Data Scientist`, `Web Developer`, `Business Analyst`, etc.
- Returns results via a **RESTful API**
- Fully deployed using Docker + Render

---

## 🛠️ Tech Stack

| Layer            | Tools                         |
|------------------|-------------------------------|
| Machine Learning | Scikit-learn, TfidfVectorizer |
| Backend API      | FastAPI, Uvicorn              |
| PDF Parsing      | PyMuPDF                       |
| Deployment       | Docker, Render                |

---

## 📁 Project Structure

resume-classifier/ 
├── app/ │
         ├── main.py # FastAPI app │ 
         └── utils.py # PDF text extraction 
├── model/ │
           ├── resume_model.pkl │
           └── vectorizer.pkl 
├── data/ # Resume PDFs (used for training)
├── train_model.py # Script to train model from PDFs 
├── requirements.txt 
├── Dockerfile 
└── README.md


---

## ⚙️ How to Run Locally

```bash
# Clone the repo
git clone https://github.com/Abishek7952/resume-classifier.git
cd resume-classifier

# Create virtual environment
python -m venv venv
venv\Scripts\activate   # On Windows

# Install dependencies
pip install -r requirements.txt

# Train the model (optional, already included)
python train_model.py

# Run FastAPI server
uvicorn app.main:app --reload

Visit: http://127.0.0.1:8000/docs to test locally.

# Build Docker image
docker build -t resume-classifier .

# Run container
docker run -p 8000:8000 resume-classifier

```
👨‍💻 Author
Abishek Ravichandiran
Aspiring ML Engineer | CSE + Business Analytics
🔗 LinkedIn https://www.linkedin.com/in/abishek316/
📬 abishekravichandiran7@gmail.com

⭐️ Show Your Support
If you found this useful, please ⭐️ the repo and share it!
s
