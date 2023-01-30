from database import DatabaseHandler

from typing import Any


class MessageHandler:
    def __init__(self, database_handler: DatabaseHandler) -> None:
        self.database_handler = database_handler

    def handle_message(self, message: dict[str, Any]) -> None:
        metadata = message.get("metadata")
        payload = message.get("payload")

        if metadata is None or payload is None:
            return

        message_type = metadata.get("type")

        if message_type == "category":
            self.handle_category(payload)
        elif message_type == "offer":
            self.handle_offer(payload)
        else:
            return

    def handle_category(self, payload: dict[str, Any]) -> None:
        self.database_handler.insert_category(
            payload.get("name"), payload.get("parent_category")
        )

    def handle_offer(self, payload: dict[str, Any]) -> None:
        self.database_handler.insert_offer(
            payload.get("id"),
            payload.get("name"),
            payload.get("description"),
            payload.get("category"),
        )
