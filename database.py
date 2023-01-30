import sqlite3

class DatabaseHandler():
    
    def __init__(self):
        self.connection = sqlite3.connect("data.sqlite")
        self.cursor = self.connection.cursor()

    def create_tables(self):
        with self.connection:
            self.cursor.execute("""CREATE TABLE category (
                name TEXT PRIMARY KEY,
                parent_category TEXT,
                FOREIGN KEY (parent_category) REFERENCES category(name)
                )""")

            self.cursor.execute("""CREATE TABLE offer (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT NOT NULL,
                category_name TEXT NOT NULL,
                FOREIGN KEY (category_name) REFERENCES category(name)
                )""")

    def insert_category(self, name, parent_category=None):
        with self.connection:
            self.cursor.execute("""INSERT INTO category (name, parent_category)
                                    VALUES (?,?)""", (name, parent_category))

    def insert_offer(self, name, description, category_id):
        with self.connection:
            self.cursor.execute("""INSERT INTO offer (name, description, category_id)
                                    VALUES (?,?,?)""", (name, description, category_id))

    def get_categories(self):
        self.cursor.execute("SELECT * FROM category")
        categories = self.cursor.fetchall()
        return categories
