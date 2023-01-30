from config import KAFKA_TOPIC
from consumer import KafkaMessageConsumer


consumer = KafkaMessageConsumer()

print("Consumer set")

for message in consumer.receive_messages(KAFKA_TOPIC):
    print("Received message:", message)