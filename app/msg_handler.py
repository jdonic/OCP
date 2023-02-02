from database import DatabaseHandler
from fetch_matches import get_offer_matches
from typing import Any, Dict, Tuple
import json


class MessageHandler:
    def __init__(self, database_handler: DatabaseHandler) -> None:
        self.database_handler = database_handler

    def handle_message(self, message: Dict[str, Any]) -> None:
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

    def handle_category(self, payload: Dict[str, Any]) -> None:
        self.database_handler.insert_category(
            payload.get("name"), payload.get("parent_category")
        )

    def handle_offer(self, payload: Dict[str, Any]) -> None:
        inserted = self.database_handler.insert_offer(
            payload.get("id"),
            payload.get("name"),
            payload.get("description"),
            payload.get("category"),
            json.dumps(payload.get("parameters")),
        )

        if inserted:
            self.create_products(payload.get("id"), payload.get("parameters"))  # type: ignore

    def create_products(self, offer_id: str, parameters: Dict) -> None:
        matches = get_offer_matches(offer_id)
        if matches:
            for match_id in matches:
                matching_offer = self.database_handler.get_offer_by_id(match_id)
                if matching_offer and matching_offer["id"] != offer_id:
                    differences, commonalities = self.find_differences(
                        parameters, matching_offer["parameters"]
                    )
                    self.database_handler.insert_product(
                        offer_id, match_id, differences, commonalities
                    )

    @staticmethod
    def find_differences(
        offer_parameters: Dict, match_parameters: Dict
    ) -> Tuple[int, int]:
        same_keys = set(offer_parameters.keys()) & set(match_parameters.keys())
        same_parameters = sum(
            offer_parameters[key] == match_parameters[key] for key in same_keys
        )
        different_parameters = len(same_keys) - same_parameters
        return (same_parameters, different_parameters)
