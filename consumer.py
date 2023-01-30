from kafka import KafkaConsumer
import config
import logging

class KafkaMessageConsumer:
    def __init__(self):
        self.consumer = KafkaConsumer(
            bootstrap_servers=config.KAFKA_BOOTSTRAP_SERVER,
            security_protocol=config.KAFKA_SECURITY_PROTOCOL,
            sasl_mechanism=config.KAFKA_SASL_MECHANISM,
            sasl_plain_username=config.KAFKA_USERNAME,
            sasl_plain_password=config.KAFKA_PASSWORD,
            value_deserializer=lambda x: x.decode("utf-8"),
        )

    def receive_messages(self, topic):
        self.consumer.subscribe(topics=[topic])
        logging.info(f"Subscibed to topics: {self.consumer.subscription()}")
        for msg in self.consumer:
            yield msg.value
