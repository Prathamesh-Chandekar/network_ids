import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Load data from CSV
alert_df = pd.read_csv("alerts.csv")

# Sidebar filters
st.sidebar.header("Filter Alerts")
severity_filter = st.sidebar.selectbox("Severity", options=["All", "High", "Medium", "Low"])

# Display main title and metrics
st.title("Network Intrusion Detection System")
st.subheader("Model Performance")

# Sample model metrics (replace with real metrics if available)
model_metrics = {"accuracy": 0.92, "precision": 0.88, "recall": 0.90, "f1Score": 0.89}
for metric, value in model_metrics.items():
    st.metric(metric.capitalize(), f"{value * 100:.1f}%")

# Filter alerts based on severity
filtered_alerts = alert_df if severity_filter == "All" else alert_df[alert_df['severity'] == severity_filter]

# Display alert logs
st.subheader("Alert Logs")
for _, row in filtered_alerts.iterrows():
    st.markdown(f"<div class='alert'>{row['timestamp']} | {row['severity']} | {row['type']} | {row['sourceIP']} -> {row['destinationIP']}</div>", unsafe_allow_html=True)

# Run anomaly detection on new traffic
new_data = np.random.rand(1, 10)  # Dummy data; replace with real input data
prediction = RandomForestClassifier().fit(new_data, [0]).predict(new_data)

st.subheader("Anomaly Detection")
if prediction[0] == 1:
    st.error("🚨 Potential Intrusion Detected!")
else:
    st.success("✅ No anomalies detected.")
