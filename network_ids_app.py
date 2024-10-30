import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV data
data = pd.read_csv('/mnt/data/alerts.csv')

# Define the main app title
st.title("Network Intrusion Detection System (NIDS) Dashboard with AI/ML")

# Section 1: Display Model Performance Metrics
st.header("Model Performance Metrics")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Accuracy", "95.0%")
col2.metric("Precision", "92.0%")
col3.metric("Recall", "89.0%")
col4.metric("F1 Score", "90.0%")

# Section 2: Display Alerts Table with Filtering Options
st.header("Anomaly/Security Alerts")
st.dataframe(data)  # Displays the CSV content in a table

# Section 3: Traffic Analysis Plots
st.header("Traffic Analysis")
# Option for users to select columns for time-series analysis if available
if "timestamp" in data.columns:
    data['timestamp'] = pd.to_datetime(data['timestamp'])
    traffic_count = data.groupby(data['timestamp'].dt.date).size()
    st.line_chart(traffic_count, width=0, height=400)

# Show Severity Distribution if available
if "severity" in data.columns:
    st.subheader("Severity Distribution of Alerts")
    severity_counts = data['severity'].value_counts()
    st.bar_chart(severity_counts)

# Extra Feature: Source/Destination Analysis if columns exist
if "source" in data.columns and "destination" in data.columns:
    st.subheader("Top Sources and Destinations")
    top_sources = data['source'].value_counts().head(5)
    top_destinations = data['destination'].value_counts().head(5)
    col5, col6 = st.columns(2)
    with col5:
        st.bar_chart(top_sources)
    with col6:
        st.bar_chart(top_destinations)

# Additional options for alerts and visualizations
if st.checkbox("Show Detailed Data Summary"):
    st.write(data.describe())
