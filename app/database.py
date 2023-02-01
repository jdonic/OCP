import sqlite3
import logging
import json

logger = logging.getLogger(__name__)


class DatabaseHandler:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("data.sqlite")
        self.cursor = self.connection.cursor()

    def create_tables(self) -> None:
        with self.connection:
            self.cursor.execute(
                """CREATE TABLE category (
                name TEXT PRIMARY KEY,
                parent_category TEXT,
                FOREIGN KEY (parent_category) REFERENCES category(name)
                )"""
            )

            self.cursor.execute(
                """CREATE TABLE offer (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT NOT NULL,
                category_name TEXT NOT NULL,
                parameters TEXT NOT NULL,
                FOREIGN KEY (category_name) REFERENCES category(name)
                )"""
            )

            self.cursor.execute(
                """CREATE TABLE product (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                offer_id TEXT NOT NULL,
                match_id TEXT NOT NULL,
                differences INTEGER NOT NULL,
                commonalities INTEGER NOT NULL,
                FOREIGN KEY (offer_id) REFERENCES offer(id),
                FOREIGN KEY (match_id) REFERENCES offer(id)
                )"""
            )

    def insert_category(self, name: str, parent_category: str = None) -> None:
        with self.connection:
            if parent_category:
                result = self.cursor.execute(
                    """SELECT name FROM category WHERE name=?""", (parent_category,)
                ).fetchone()

                if not result:
                    logger.error(
                        f"The parent category: {parent_category} does not exist in category table, setting it to None."
                    )
                    parent_category = None

            try:
                self.cursor.execute(
                    """INSERT INTO category (name, parent_category)
                                        VALUES (?,?)""",
                    (name, parent_category),
                )
                logger.info(f"Inserted {name} into a category table.")
            except sqlite3.IntegrityError:
                logger.error(
                    f"The category: {name} is already present in category table."
                )

    def insert_offer(
        self, id: int, name: str, description: str, category_name: str, parameters: dict
    ) -> bool:
        with self.connection:
            result = self.cursor.execute(
                """SELECT name FROM category WHERE name=?""", (category_name,)
            ).fetchone()

            if not result:
                logger.error(
                    f"The category: {category_name} does not exist in category table."
                )
                return False

            try:
                self.cursor.execute(
                    """INSERT INTO offer (id, name, description, category_name, parameters)
                                        VALUES (?,?,?,?,?)""",
                    (id, name, description, category_name, parameters),
                )
                logger.info(f"Inserted offer with id: {id} into a offer table.")
                return True
            except sqlite3.IntegrityError:
                logger.error(f"The id: {id} is already present in offer table.")
                return False

    def insert_product(self, offer_id, match_id, differences, commonalities):
        with self.connection:
            self.cursor.execute(
                """
                INSERT INTO product (offer_id, match_id, differences, commonalities)
                VALUES (?, ?, ?, ?)
                """,
                (offer_id, match_id, differences, commonalities)
            )
            logger.info(f"Inserted product with for offers: {offer_id}:{match_id} into a product table.")

    def get_categories(self) -> list:
        self.cursor.execute("SELECT * FROM category")
        categories = self.cursor.fetchall()
        return categories

    def get_offers(self) -> list:
        self.cursor.execute("SELECT id, name, description, category_name, parameters FROM offer")
        offers = self.cursor.fetchall()
        offers_with_parameters = []
        for offer in offers:
            offer_id, name, description, category_name, parameters_json = offer
            parameters = json.loads(parameters_json)
            offer_dict = {"id": offer_id, "name": name, "description": description, "category_name": category_name, "parameters": parameters}
            offers_with_parameters.append(offer_dict)
        return offers_with_parameters


    def get_products(self) -> list:
        self.cursor.execute("SELECT * FROM product")
        products = self.cursor.fetchall()
        return products


    def get_offer_by_id(self, offer_id: int) -> dict:
        self.cursor.execute("SELECT id, parameters FROM offer WHERE id=?", (offer_id,))
        offer = self.cursor.fetchone()
        if offer:
            offer_id, parameters_json = offer
            parameters = json.loads(parameters_json)
            offer_dict = {"id": offer_id, "parameters": parameters}
            return offer_dict
        else:
            logger.warning(f'The offer with id: {offer_id} is not stored in the database.')
            return None
