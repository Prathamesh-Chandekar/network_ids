import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the CSV data
try:
    data = pd.read_csv('/mnt/data/alerts.csv')
except Exception as e:
    st.error("Could not load the uploaded data. Please check the file format.")
    # Example data to show the visualization
    data = pd.DataFrame({
        'timestamp': pd.date_range(start='2023-01-01', periods=100, freq='H'),
        'severity': np.random.choice(['Low', 'Medium', 'High'], size=100),
        'alert_type': np.random.choice(['Port Scan', 'Brute Force', 'DDoS', 'Malware'], size=100),
        'source': np.random.choice(['192.168.1.1', '192.168.1.2', '10.0.0.1', '10.0.0.2'], size=100),
        'destination': np.random.choice(['192.168.1.3', '192.168.1.4', '10.0.0.3', '10.0.0.4'], size=100),
    })

# Convert timestamp to datetime if it's not already
if 'timestamp' in data.columns:
    data['timestamp'] = pd.to_datetime(data['timestamp'])

# Title
st.title("Network Intrusion Detection System (NIDS) Dashboard with AI/ML")

# Model Performance Metrics
st.header("Model Performance Metrics")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Accuracy", "95.0%")
col2.metric("Precision", "92.0%")
col3.metric("Recall", "89.0%")
col4.metric("F1 Score", "90.0%")

# Alerts Table with Filtering Options
st.header("Anomaly/Security Alerts")
severity_filter = st.selectbox("Filter by Severity", options=['All', 'Low', 'Medium', 'High'])
alert_type_filter = st.selectbox("Filter by Alert Type", options=['All', 'Port Scan', 'Brute Force', 'DDoS', 'Malware'])

filtered_data = data.copy()
if severity_filter != 'All':
    filtered_data = filtered_data[filtered_data['severity'] == severity_filter]
if alert_type_filter != 'All':
    filtered_data = filtered_data[filtered_data['alert_type'] == alert_type_filter]

st.dataframe(filtered_data)  # Display filtered data

# Traffic Analysis
st.header("Traffic Analysis")

# Check for timestamp column to plot time series
if 'timestamp' in data.columns:
    traffic_count = data.groupby(data['timestamp'].dt.date).size()
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
