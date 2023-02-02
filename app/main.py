from consumer import KafkaMessageConsumer
from database import DatabaseHandler
from msg_handler import MessageHandler

import config


def main() -> None:
    consumer = KafkaMessageConsumer()
    db = DatabaseHandler()
    parser = MessageHandler(db)
    db.create_tables()

    for message in consumer.receive_messages(config.KAFKA_TOPIC):
        parser.handle_message(message)


if __name__ == "__main__":
    main()
