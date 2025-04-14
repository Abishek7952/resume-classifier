import streamlit as st
import requests

st.set_page_config(page_title="Resume Classifier", layout="centered")

st.title("📄 Resume Classifier")
st.write("Upload your resume PDF and get a predicted job category.")

# Upload PDF
uploaded_file = st.file_uploader("Choose a resume PDF", type=["pdf"])

if uploaded_file:
    st.success("File uploaded successfully!")

    if st.button("🔍 Predict Job Category"):
        try:
            files = {"file": uploaded_file.getvalue()}
            response = requests.post(
                "https://resume-classifier-c1ub.onrender.com/predict/",  # Your FastAPI URL
                files={"file": ("resume.pdf", uploaded_file, "application/pdf")}
            )

            if response.status_code == 200:
                result = response.json()
                st.success(f"🎯 Predicted Role: `{result['predicted_category']}`")
            else:
                st.error("❌ API Error: Unable to get prediction.")

        except Exception as e:
            st.error(f"Something went wrong: {e}")
