from kafka import KafkaProducer
import json, time
import yfinance as yf

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

stock = yf.Ticker("AAPL")

while True:
    data = stock.history(period="1d", interval="1m").tail(1)

    record = {
        "symbol": "AAPL",
        "price": float(data["Close"].values[0]),
        "timestamp": str(data.index[-1])
    }

    print("Sending:", record)
    producer.send("stock-topic", value=record)

    time.sleep(60)
