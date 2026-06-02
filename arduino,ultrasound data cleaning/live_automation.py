import serial
import pandas as pd
import time
import os

# Set hardware configuration parameters
PORT = 'COM6' 
BAUD_RATE = 9600
CSV_FILE = 'live_clean_data.csv'

print("Initializing ultrasound data cleaning pipeline...")

try:
    # Initialize serial communication interface with Arduino
    arduino = serial.Serial(PORT, BAUD_RATE, timeout=1)
    time.sleep(2)  # Hardware settling delay for microcontroller reset
    print(f"Connected to data stream on port: {PORT}")
except Exception as e:
    print(f"Connection failed. Ensure port is not locked by another app. Error: {e}")
    exit()

# Clear out previous session files to guarantee data integrity
if os.path.exists(CSV_FILE):
    os.remove(CSV_FILE)

# Array buffer to store raw incoming laboratory sensor readings
raw_readings = []

try:
    while True:
        # Read incoming byte line from the serial port buffer
        raw_line = arduino.readline().decode('utf-8').strip()
        
        if raw_line:
            try:
                distance = int(raw_line)
                raw_readings.append(distance)
                print(f"Raw incoming reading: {distance} cm")
                
                # Load the tracking buffer into a Pandas DataFrame for data operations
                df = pd.DataFrame(raw_readings, columns=['Distance_CM'])
                
                # Apply shift filter to eliminate consecutive identical duplicates
                # This prevents the log from bloating when the measured state is static
                clean_df = df.loc[df['Distance_CM'].shift() != df['Distance_CM']]
                
                # Write the cleaned data to disk for consumption by the web app
                clean_df.to_csv(CSV_FILE, index=False)
                
                # Output the current tail of the cleaned dataset to verify filter behavior
                print("\nFiltered DataFrame tail (Consecutive duplicates removed):")
                print(clean_df.tail(3).to_string(index=False))
                print("-" * 50)
                
            except ValueError:
                # Catch and ignore corrupted serial frame fragments
                continue
                
except KeyboardInterrupt:
    print("\nData collection paused by user. Closing serial connection.")
    arduino.close()