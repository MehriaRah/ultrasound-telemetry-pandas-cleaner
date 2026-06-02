# Ultrasonic Telemetry Stream & Pandas Data Automation Pipeline

An end-to-end data engineering project that bridges the gap between raw hardware sensing and live web visualization. This pipeline captures high-frequency distance logs from an ultrasonic sensor via a serial interface, applies real-time deduplication algorithms using Python and Pandas to eliminate idle data bloat, and visualizes the optimized data stream on a live Streamlit web dashboard.

---

## 📊 Pipeline Architecture

The data flows across a clean four-stage system topology:

[Ultrasonic Distance Sensor] ──> [Microcontroller Firmware (C)] ──(High-Speed Serial/UART)──> [Python Cleansing Core (Pandas)] ──> [Streamlit Web UI]

---

## ⚡ Core Features

* **High-Frequency Telemetry Ingestion:** Microcontroller firmware configured to capture real-time acoustic time-of-flight reflections, translating echo durations into metric distance logs streamed continuously over a Serial interface.
* **On-the-Fly Data Deduplication:** A localized Python background process running optimized `Pandas` logic. If the physical environment in front of the ultrasonic sensor is static, consecutive duplicate entries are programmatically dropped to prevent database and log bloat.
* **Dynamic Analytics Visualization:** A lightweight, responsive dashboard built with `Streamlit` that listens directly to the automated data pipeline, updating live moving charts instantly as the physical sensor environment shifts.

---

## 🛠️ Tech Stack & Dependencies

* **Hardware Layer:** Microcontroller Development Platform / Core C, Ultrasonic Sensor (Time-of-Flight)
* **Data Processing Layer:** Python 3.x, Pandas (Dataframes & structural comparative filtering), PySerial (Instrument-to-PC communication interface)
* **User Interface:** Streamlit (Web dashboarding), Rich (Terminal formatting & validation)

---
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/652149de-8e4e-4fca-b5a1-de290b3c92d1" />

<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/f703e845-1f94-41a5-a2c3-96086dda1014" />


## 🚀 Code Implementation Details

### 1. Hardware Stream Generation (Firmware Code Pattern)
The microcontroller continuously pulses the ultrasonic sensor, converts the echo delay into a physical distance, and streams the raw payload down the serial port:
```c
// System loop capturing high-frequency time-of-flight values
void loop() {
  long duration = pulseIn(echoPin, HIGH);
  float distance = duration * 0.034 / 2; // Compute precise distance metric
  Serial.println(distance);             // Stream raw data package
  delay(50);                            // 20Hz high-frequency sampling rate
}



