# Step 1: Start Kafka
docker-compose up -d

# Step 2: Create topic
kafka-topics --create --topic stock-topic --bootstrap-server localhost:9092

# Step 3: Install deps
pip install -r requirements.txt

# Step 4: Run producer
python producer.py

# Step 5: Run consumer
python consumer.py

# Step 6: Run dashboard
streamlit run app.py

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
docker exec -it kafka kafka-topics \
--create --topic stock-topic \
--bootstrap-server localhost:9092
