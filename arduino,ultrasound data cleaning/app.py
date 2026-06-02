import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Ultrasound Telemetry Platform", layout="centered")

st.title("Ultrasound Data Cleaning Hub")
st.subheader("Sensor Metrics and Analytics Pipeline")

CSV_FILE = 'live_clean_data.csv'

# Check if the collection script has initialized the data matrix
if os.path.exists(CSV_FILE):
    try:
        df = pd.read_csv(CSV_FILE)
        
        if not df.empty:
            # Extract the most recent validated metric
            latest_reading = df['Distance_CM'].iloc[-1]
            st.metric(label="Validated Distance Output", value=f"{latest_reading} cm")
            
            # Plot the historical trend array with the duplicates removed
            st.write("Distance Tracking History")
            st.line_chart(df['Distance_CM'])
            
            # Display raw tabular grid of the cleaned logs
            st.write("Clean Data Log Matrix View")
            st.dataframe(df.tail(10), use_container_width=True)
            
        else:
            st.info("Serial connection active. Awaiting initial sensor variations...")
            
    except Exception as e:
        st.error(f"Error accessing data file: {e}")
else:
    st.warning("Awaiting initial data generation from collection script...")

# Manual trigger to force immediate DataFrame re-read from disk
if st.button("Refresh Telemetry"):
    st.rerun()