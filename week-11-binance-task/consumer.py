import confluent_kafka
import schemas
from reposiroty import insert_to_db
import json

consumer = confluent_kafka.Consumer(
    {'bootstrap.servers': 'localhost:9092', 'group.id': 'binance_group'}
)

topic = 'binance_topic'
consumer.subscribe([topic])
number_of_messages = 30


def consume():
    try:
        message_count = 0
        while True:
            messages = consumer.consume(num_messages=number_of_messages, timeout=2)
            if messages is None:
                break
            for message in messages:
                bitcoin = schemas.BitcoinCreate(**json.loads(message.value().decode("utf-8")))
                print(bitcoin)
                insert_to_db(bitcoin)
                message_count += 1
                if message_count >= 20:
                    print("All messages consumed")
                    continue
    except Exception as e:
        print(f"Error: {e}")
    finally:
        consumer.close()
        print("Consumer closed")


if __name__ == '__main__':
    consume()
