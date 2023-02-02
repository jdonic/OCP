from kafka import KafkaConsumer
from typing import Generator

import config
import json


class KafkaMessageConsumer:
    def __init__(self) -> None:
        self.consumer = KafkaConsumer(
            bootstrap_servers=config.KAFKA_BOOTSTRAP_SERVER,
            security_protocol=config.KAFKA_SECURITY_PROTOCOL,
            sasl_mechanism=config.KAFKA_SASL_MECHANISM,
            sasl_plain_username=config.KAFKA_USERNAME,
            sasl_plain_password=config.KAFKA_PASSWORD,
            value_deserializer=lambda x: json.loads(x.decode("utf-8")),
            auto_offset_reset="earliest",
        )

    def receive_messages(self, topic: str) -> Generator:
        """
        Subscribes to a topic and generates back
        recieved messages.
        """
        self.consumer.subscribe(topics=[topic])
        for msg in self.consumer:
            yield msg.value
