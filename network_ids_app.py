import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Load the CSV data or use example data if file load fails
try:
    data = pd.read_csv('/mnt/data/alerts.csv')
    data['timestamp'] = pd.to_datetime(data['timestamp'])
except:
    # Example data if CSV not loaded
    data = pd.DataFrame({
        'timestamp': pd.date_range(start='2023-01-01', periods=100, freq='H'),
        'severity': np.random.choice(['Low', 'Medium', 'High'], size=100),
        'alert_type': np.random.choice(['Port Scan', 'Brute Force', 'DDoS', 'Malware'], size=100),
        'source': np.random.choice(['192.168.1.1', '192.168.1.2', '10.0.0.1', '10.0.0.2'], size=100),
        'destination': np.random.choice(['192.168.1.3', '192.168.1.4', '10.0.0.3', '10.0.0.4'], size=100),
    })

# Load icons (You may need to replace these paths with actual logo paths)
accuracy_icon = Image.open("path/to/accuracy_icon.png")
precision_icon = Image.open("path/to/precision_icon.png")
recall_icon = Image.open("path/to/recall_icon.png")
f1_icon = Image.open("path/to/f1_icon.png")
alerts_icon = Image.open("path/to/alerts_icon.png")
traffic_icon = Image.open("path/to/traffic_icon.png")

# Title with main logo (optional)
st.title("🔒 Network Intrusion Detection System (NIDS) Dashboard with AI/ML")

# Model Performance Metrics with Icons
st.header("Model Performance Metrics")
col1, col2, col3, col4 = st.columns(4)
col1.image(accuracy_icon, width=50)
col1.metric("Accuracy", "95.0%")
col2.image(precision_icon, width=50)
col2.metric("Precision", "92.0%")
col3.image(recall_icon, width=50)
col3.metric("Recall", "89.0%")
col4.image(f1_icon, width=50)
col4.metric("F1 Score", "90.0%")

# Alerts Table with Filtering Options and Icon
st.header("📊 Anomaly/Security Alerts")
severity_filter = st.selectbox("Filter by Severity", options=['All', 'Low', 'Medium', 'High'])
alert_type_filter = st.selectbox("Filter by Alert Type", options=['All', 'Port Scan', 'Brute Force', 'DDoS', 'Malware'])

filtered_data = data.copy()
if severity_filter != 'All':
    filtered_data = filtered_data[filtered_data['severity'] == severity_filter]
if alert_type_filter != 'All':
    filtered_data = filtered_data[filtered_data['alert_type'] == alert_type_filter]

st.image(alerts_icon, width=50)
st.dataframe(filtered_data)  # Display filtered data

# Traffic Analysis with Icon
st.header("📈 Traffic Analysis")

if 'timestamp' in data.columns:
    traffic_count = data.groupby(data['timestamp'].dt.date).size()
    st.image(traffic_icon, width=50)
    st.line_chart(traffic_count, width=0, height=400)

# Severity Distribution
if 'severity' in data.columns:
    st.subheader("Severity Distribution of Alerts")
    severity_counts = data['severity'].value_counts()
    st.bar_chart(severity_counts)

# Source/Destination Analysis
if 'source' in data.columns and 'destination' in data.columns:
    st.subheader("Top Sources and Destinations")
    top_sources = data['source'].value_counts().head(5)
    top_destinations = data['destination'].value_counts().head(5)
    col5, col6 = st.columns(2)
    with col5:
        st.bar_chart(top_sources)
    with col6:
        st.bar_chart(top_destinations)

# Additional options
if st.checkbox("Show Detailed Data Summary"):
    st.write(data.describe())
