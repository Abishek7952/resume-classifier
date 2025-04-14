from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import joblib
from app.utils import extract_text_from_pdf

app = FastAPI()

# Enable CORS if you use a frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # set to frontend URL if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model and vectorizer
model = joblib.load("model/resume_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

@app.get("/")
def home():
    return {"message": "Resume Classifier API is live!"}

@app.post("/predict/")
async def predict_resume(file: UploadFile = File(...)):
    content = await file.read()
    text = extract_text_from_pdf(content)
    if not text:
        return {"error": "Could not read text from the PDF"}

    features = vectorizer.transform([text])
    prediction = model.predict(features)[0]
    return {"predicted_category": prediction}
