import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Set Streamlit page configuration
st.set_page_config(
    page_title="Network IDS",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon=":shield:"
)

# Custom CSS for better UI
st.markdown("""
    <style>
        .main { background-color: #1e1e1e; }
        .stTextInput, .stSelectbox { margin-bottom: 20px; }
        .stTextInput > div, .stSelectbox > div { color: #fff; }
        .metric { font-size: 20px; }
        .alert { font-family: monospace; margin: 10px 0; }
    </style>
""", unsafe_allow_html=True)

# Sidebar filters
st.sidebar.header("Filter Alerts")
severity_filter = st.sidebar.selectbox("Severity", options=["All", "High", "Medium", "Low"])

# Model Performance Section with some example metrics
st.title("Network Intrusion Detection System")

st.subheader("Model Performance")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Accuracy", "0.92")
col2.metric("Precision", "0.88")
col3.metric("Recall", "0.90")
col4.metric("F1 Score", "0.89")

# Sample alert data
alerts = [
    ("192.168.1.10:22 -> 10.0.0.5:3306", "High", "SQL Injection", "2023-04-01 12:34:56"),
    ("172.16.0.20:80 -> 192.168.2.15:8080", "Medium", "Web App Attack", "2023-04-02 09:12:34"),
    ("10.0.0.12:22 -> 172.16.1.8:22", "High", "SSH Brute-Force", "2023-04-03 15:45:12"),
    ("192.168.2.15:3306 -> 10.0.0.5:3306", "Low", "Reconnaissance", "2023-04-04 08:23:45"),
]

# Filter alerts based on severity
filtered_alerts = [alert for alert in alerts if severity_filter == "All" or alert[1] == severity_filter]

# Display alert logs
st.subheader("Alert Logs")
for alert in filtered_alerts:
    alert_info = f"{alert[0]} | {alert[1]} | {alert[2]} | {alert[3]}"
    st.markdown(f"<div class='alert'>{alert_info}</div>", unsafe_allow_html=True)

# Dummy dataset for predictions
X = np.random.rand(5, 10)  # Example data with 5 rows, 10 features

# Example machine learning model
model = RandomForestClassifier()
y = np.random.randint(0, 2, 5)  # Dummy labels (0 = normal, 1 = anomaly)

# Train model
model.fit(X, y)

# Predict new traffic (simulating an anomaly)
new_traffic = np.random.rand(1, 10)
prediction = model.predict(new_traffic)

# Display prediction result
st.subheader("Anomaly Detection")
if prediction[0] == 1:
    st.error("🚨 Potential Intrusion Detected!")
else:
    st.success("✅ No anomalies detected.")

