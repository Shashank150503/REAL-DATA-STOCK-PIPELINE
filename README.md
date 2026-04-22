# Real-Time Stock Data Pipeline

## Overview
This project implements a real-time stock data pipeline using Kafka, Python, and Streamlit.

## Tech Stack
- Kafka
- Python
- Streamlit
- Docker

## Setup Instructions

### 1. Start Kafka
docker-compose up -d

### 2. Install dependencies
pip install -r requirements.txt

### 3. Run Producer
python producer/producer.py

### 4. Run Consumer
python consumer/consumer.py

### 5. Run Dashboard
streamlit run dashboard/app.py

## Features
- Real-time data ingestion
- Streaming pipeline
- Live dashboard visualization
