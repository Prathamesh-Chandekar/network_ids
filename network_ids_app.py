import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Load and preprocess data
@st.cache_data
def load_data():
    data = pd.read_csv('network_traffic.csv')
    label_encoders = {}
    for column in ['src_ip', 'dest_ip', 'protocol']:
        le = LabelEncoder()
        data[column] = le.fit_transform(data[column])
        label_encoders[column] = le
    X = data.drop('label', axis=1)
    y = LabelEncoder().fit_transform(data['label'])
    return train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Random Forest model
def train_model(X_train, y_train):
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    return model

# Display model metrics
def display_metrics(y_test, y_pred):
    st.metric("Accuracy", f"{accuracy_score(y_test, y_pred):.2f}")
    st.metric("Precision", f"{precision_score(y_test, y_pred):.2f}")
    st.metric("Recall", f"{recall_score(y_test, y_pred):.2f}")
    st.metric("F1 Score", f"{f1_score(y_test, y_pred):.2f}")

# Visualize alerts
def show_alerts(alerts, severity_filter):
    filtered_alerts = [
        alert for alert in alerts if severity_filter == "All" or alert[1] == severity_filter
    ]
    st.write("### Alert Logs")
    for alert in filtered_alerts:
        st.write(f"**{alert[0]}** | {alert[1]} | {alert[2]} | {alert[3]}")

# Main Streamlit App
def main():
    st.title("Network Intrusion Detection System")
    st.sidebar.header("Filter Alerts")
    severity = st.sidebar.selectbox("Severity", ["All", "High", "Medium", "Low"])
    
    # Load and prepare data
    X_train, X_test, y_train, y_test = load_data()
    model = train_model(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Display metrics
    st.write("## Model Performance")
    display_metrics(y_test, y_pred)

    # Alert visualization
    alerts = [
        ("192.168.1.10:22 -> 10.0.0.5:3306", "High", "SQL Injection", "2023-04-01 12:34:56"),
        ("172.16.0.20:80 -> 192.168.2.15:8080", "Medium", "Web App Attack", "2023-04-02 09:12:34"),
        ("10.0.0.12:22 -> 172.16.1.8:22", "High", "SSH Brute-Force", "2023-04-03 15:45:12"),
        ("192.168.2.15:3306 -> 10.0.0.5:3306", "High", "SQL Injection", "2023-04-04 08:23:45"),
        ("172.16.1.8:80 -> 192.168.1.10:80", "Medium", "Web App Attack", "2023-04-05 14:56:01"),
        ("10.0.0.5:22 -> 192.168.2.15:22", "High", "SSH Brute-Force", "2023-04-06 11:22:33"),
    ]

    show_alerts(alerts, severity)

    # New traffic anomaly detection
    new_traffic = np.random.rand(1, X_train.shape[1])
    prediction = model.predict(new_traffic)
    status = "Potential intrusion detected!" if prediction[0] == 1 else "No anomalies detected."
    st.write(f"## Anomaly Detection: {status}")

if __name__ == "__main__":
    main()
