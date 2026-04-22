import streamlit as st
import pandas as pd
import time
import os

st.title("📈 Real-Time Stock Dashboard")

file_path = "data/AAPL.json"

while True:
    if os.path.exists(file_path):
        df = pd.read_json(file_path, lines=True)
        st.line_chart(df.set_index("timestamp")["price"])
    else:
        st.write("Waiting for data...")

    time.sleep(5)
