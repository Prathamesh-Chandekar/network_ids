import streamlit as st
import pandas as pd
import plotly.graph_objs as go
from datetime import datetime

# Sample alert data - mimicking data from React code
alerts = [
    {
        "id": 1,
        "timestamp": "2024-10-30 10:15:23",
        "type": "TCP SYN Flood",
        "confidence": 98.5,
        "severity": "high",
        "sourceIP": "192.168.1.105",
        "destinationIP": "10.0.0.1"
    },
    {
        "id": 2,
        "timestamp": "2024-10-30 10:14:55",
        "type": "Port Scan",
        "confidence": 85.2,
        "severity": "medium",
        "sourceIP": "192.168.1.110",
        "destinationIP": "10.0.0.2"
    }
]

# Model metrics - similar to the React model metrics
model_metrics = {
    "accuracy": 0.95,
    "precision": 0.92,
    "recall": 0.89,
    "f1Score": 0.90
}

# Traffic statistics for the bar chart
traffic_stats = {
    "Normal": 2450,
    "Suspicious": 150,
    "Malicious": 50
}

# Sidebar and main title
st.title("Network Intrusion Detection System")
st.markdown("### System Active :white_check_mark:")

# Display model metrics
st.subheader("Model Performance")
for metric, value in model_metrics.items():
    st.metric(metric.capitalize(), f"{value * 100:.1f}%")

# Traffic analysis chart
st.subheader("Traffic Analysis")
fig = go.Figure(data=[
    go.Bar(name='Traffic Type', x=list(traffic_stats.keys()), y=list(traffic_stats.values()))
])
fig.update_layout(title='Traffic Analysis', xaxis_title="Type", yaxis_title="Count")
st.plotly_chart(fig)

# Recent alerts section
st.subheader("Recent Security Alerts")
for alert in alerts:
    severity_color = {
        'high': '#FFCDD2',
        'medium': '#FFECB3',
        'low': '#BBDEFB'
    }.get(alert['severity'], '#ECEFF1')
    
    st.markdown(f"<div style='background-color: {severity_color}; padding: 10px; border-radius: 5px;'>"
                f"<strong>Type:</strong> {alert['type']}<br>"
                f"<strong>Confidence:</strong> {alert['confidence']}%<br>"
                f"<strong>Source IP:</strong> {alert['sourceIP']}<br>"
                f"<strong>Destination IP:</strong> {alert['destinationIP']}<br>"
                f"<strong>Timestamp:</strong> {alert['timestamp']}<br>"
                f"<strong>Severity:</strong> {alert['severity'].upper()}</div>", 
                unsafe_allow_html=True)

# System status
st.subheader("System Status")
st.success(f"All detection systems operating normally | Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
