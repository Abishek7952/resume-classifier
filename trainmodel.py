import os
import fitz  # PyMuPDF
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

texts = []
labels = []

base_dir = "data/data"  # your top-level folder with role-wise PDF folders

# Loop through all subfolders (each folder = label)
for category in os.listdir(base_dir):
    folder_path = os.path.join(base_dir, category)
    if not os.path.isdir(folder_path):
        continue

    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            file_path = os.path.join(folder_path, filename)
            try:
                doc = fitz.open(file_path)
                text = ""
                for page in doc:
                    text += page.get_text()
                texts.append(text)
                labels.append(category)
            except Exception as e:
                print(f"Error reading {file_path}: {e}")

print(f"Loaded {len(texts)} resumes across {len(set(labels))} categories.")

# Vectorize
vectorizer = TfidfVectorizer(stop_words="english", max_features=3000)
X = vectorizer.fit_transform(texts)

# Split & train
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Save
os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/resume_model.pkl")
joblib.dump(vectorizer, "model/vectorizer.pkl")

print("Model trained. Accuracy:", model.score(X_test, y_test))
