import streamlit as st
import pickle
from utils import extract_features  # Make sure this function returns a consistent feature length

# Load the pre-trained model
with open("model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Streamlit App Config
st.set_page_config(
    page_title="🔍 Intelligent Malware Analyzer",
    page_icon="🛡",
    layout="wide",
)

# Sidebar - Upload File Section
st.sidebar.header("🗂 File Upload")
uploaded_file = st.sidebar.file_uploader("Upload a file to analyze", type=["exe", "dll", "pdf"])

st.sidebar.markdown("----")
st.sidebar.write("Built with ❤ by [Your Name]")

# Title and Description
st.title("🔍 Intelligent Malware Analyzer 🛡")
st.write("Welcome to the Intelligent Malware Analyzer! Upload a file to detect if it's malicious or safe. 🚫🟢")

# Sample Button for Test Files
if st.sidebar.button("🔄 Use a sample file"):
    # Optionally load a sample file for testing
    uploaded_file = "data/sample_files/malicious_sample.exe"

# Main Content
if uploaded_file:
    # Display file details
    st.subheader("📄 File Details")
    st.write(f"File Name: {uploaded_file.name}")
    st.write(f"File Size: {len(uploaded_file.getvalue()) / 1024:.2f} KB")

    # Feature Extraction
    st.subheader("⚙ Feature Extraction")
    st.write("Analyzing the file... 🕵‍♂")
    
    # Extract features from file
    features = extract_features(uploaded_file)
    
    # Validate feature count
    if len(features) != model.n_features_in_:
        st.error(f"Feature mismatch: Model expects {model.n_features_in_} features, but {len(features)} were provided.")
    else:
        # Predict Malware or Benign
        st.subheader("🧠 Model Prediction")
        prediction = model.predict([features])[0]
        prediction_proba = model.predict_proba([features])[0]

        # Display Results
        if prediction == 1:
            st.error("🚨 Alert! This file is malicious. Proceed with caution! ⚠", icon="🚫")
            st.write(f"Confidence: {prediction_proba[1] * 100:.2f}%")
        else:
            st.success("🎉 Good news! This file appears to be safe. 😌", icon="🟢")
            st.write(f"Confidence: {prediction_proba[0] * 100:.2f}%")

else:
    st.warning("👆 Please upload a file to begin the analysis!")

# Footer Section with Emojis and Additional Links
st.markdown("---")
st.write("🔒 Secure, Reliable, and AI-powered malware detection system.")
st.write("💡 Tips: Avoid suspicious downloads and always scan files before use.")
st.write("📊 Built with: Streamlit, Scikit-learn, and more!")
