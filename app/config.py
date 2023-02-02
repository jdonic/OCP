import os

KAFKA_BOOTSTRAP_SERVER = "pkc-4ygn6.europe-west3.gcp.confluent.cloud:9092"
KAFKA_SECURITY_PROTOCOL = "SASL_SSL"
KAFKA_USERNAME = os.environ.get("KAFKA_USERNAME")
KAFKA_PASSWORD = os.environ.get("KAFKA_PASSWORD")
KAFKA_SASL_MECHANISM = "PLAIN"
KAFKA_TOPIC = "catalogue_source"
