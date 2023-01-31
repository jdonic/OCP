import sqlite3

import logging

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
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT NOT NULL,
                category_name TEXT NOT NULL,
                FOREIGN KEY (category_name) REFERENCES category(name)
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
        self, id: int, name: str, description: str, category_name: str
    ) -> None:
        with self.connection:
            result = self.cursor.execute(
                """SELECT name FROM category WHERE name=?""", (category_name,)
            ).fetchone()

            if not result:
                logger.error(
                    f"The category: {category_name} does not exist in category table."
                )
                return

            try:
                self.cursor.execute(
                    """INSERT INTO offer (id, name, description, category_name)
                                        VALUES (?,?,?,?)""",
                    (id, name, description, category_name),
                )
                logger.info(f"Inserted offer with id: {id} into a offer table.")
            except sqlite3.IntegrityError:
                logger.error(f"The id: {id} is already present in offer table.")

    def get_categories(self) -> list:
        self.cursor.execute("SELECT * FROM category")
        categories = self.cursor.fetchall()
        return categories

    def get_offers(self) -> list:
        self.cursor.execute("SELECT * FROM offer")
        offers = self.cursor.fetchall()
        return offers
