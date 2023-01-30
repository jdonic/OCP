from consumer import KafkaMessageConsumer
from database import DatabaseHandler
from msg_handler import MessageHandler

consumer = KafkaMessageConsumer()

print("Consumer set")

db = DatabaseHandler()
db.create_tables()
print("Database created")

parser = MessageHandler(db)


message = {"metadata": {"type": "category"}, "payload": {"name": "Electronics"}}
parser.handle_message(message)


message2 = {
    "metadata": {"type": "category"},
    "payload": {"name": "coffee", "parent_category": "books"},
}

parser.handle_message(message2)

message3 = {
    "metadata": {"type": "offer"},
    "payload": {
        "category": "Electronics",
        "id": 12345,
        "name": "Samsung Galaxy S21",
        "description": "The latest smartphone from Samsung",
        "parameters": [{"color": "pink"}, {"storage": "128GB"}],
    },
}
parser.handle_message(message3)

categories = db.get_categories()
print(categories)
offers = db.get_offers()
print(offers)
# for message in consumer.receive_messages(KAFKA_TOPIC):
#     print("Received message:", message)
