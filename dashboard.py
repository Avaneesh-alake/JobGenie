
import pandas as pd
import streamlit as st
import os
import re
from datetime import datetime
import plotly.express as px

LOG_FILE = "logs/interview_log.txt"

# Function to read and parse log file
def load_logs():
    if not os.path.exists(LOG_FILE):
        st.warning("No logs found yet. Start recording in JobGenie first.")
        return pd.DataFrame(columns=["DateTime", "Transcript", "Feedback"])
    
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        raw = f.read()

    entries = raw.strip().split("\n---\n")
    data = []
    for entry in entries:
        if not entry.strip():
            continue
        try:
            date = re.search(r"🕒 (.+)", entry).group(1)
            transcript = re.search(r"🎙️ Transcript: (.+)", entry).group(1)
            feedback = re.search(r"💬 Feedback: (.+)", entry).group(1)
            data.append({
                "DateTime": datetime.strptime(date, "%Y-%m-%d %H:%M:%S"),
                "Transcript": transcript,
                "Feedback": feedback
            })
        except:
            continue

    return pd.DataFrame(data)

# Streamlit App
st.set_page_config(page_title="JobGenie Dashboard", layout="wide")
st.title("📊 JobGenie - Voice Interview Feedback Dashboard")

df = load_logs()

if not df.empty:
    # Show raw data
    st.subheader("🧾 Feedback History")
    st.dataframe(df.sort_values("DateTime", ascending=False), use_container_width=True)

    # Optional: Line chart showing number of responses per day
    st.subheader("📈 Attempts Over Time")
    df["Date"] = df["DateTime"].dt.date
    daily_counts = df.groupby("Date").size().reset_index(name="Attempts")
    fig = px.bar(daily_counts, x="Date", y="Attempts", title="Interview Attempts per Day")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("No feedback history to show yet. Start recording some answers in the app.")

