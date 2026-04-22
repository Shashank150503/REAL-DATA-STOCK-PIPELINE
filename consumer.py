from kafka import KafkaConsumer
import json
import os

os.makedirs("data", exist_ok=True)

consumer = KafkaConsumer(
    'stock-topic',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for message in consumer:
    data = message.value

    file_name = f"data/{data['symbol']}.json"

    with open(file_name, "a") as f:
        f.write(json.dumps(data) + "\n")

    print("Stored:", data)
