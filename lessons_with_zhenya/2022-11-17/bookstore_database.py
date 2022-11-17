"""
Create an application for a small bookstore. 
Your application would store data about available items in stock - books, magazines and other related goods like notebooks, postcards etc. 
Main functionality of your application is to track sales and available items quantity. 
Make sure your application supports stock replenishment. 
Also it might be useful to have an easy way to calculate total cost of goods sold for some period (day, week, month).
For books application would keep some additional information like author, the genre of the book, year of publishing, optional short description.
For magazines we're interested to know the month of its publication and possible target audience (children, adults, scientists, gardeners etc.)
Use sqlite database for your data storage.
"""

import sqlite3


class Item:
    @classmethod
    def create_table(cls, connection):
        with connection:
            connection.cursor().execute(
                """CREATE TABLE IF NOT EXISTS items (
                name text,
                type text,
                price integer,
                quantity integer
                )"""
            )

    def __init__(self, name, item_type, price, quantity):
        self.name = name
        self.item_type = item_type
        self.price = price
        self.quantity = quantity

    def add_to_table(self, connection):
        with connection:
            cursor = connection.cursor()
            cursor.execute(
                "SELECT name, quantity FROM items WHERE name = :name and type = :type",
                {"name": self.name, "type": self.item_type},
            )
            matches = cursor.fetchall()
            if len(matches) > 0:
                assert len(matches) == 1
                match_name, match_quantity = matches[0]
                assert match_name == self.name

                cursor.execute(
                    """UPDATE items 
                    SET quantity = :quantity 
                    WHERE name = :name and type = :type""",
                    {
                        "quantity": int(match_quantity) + self.quantity,
                        "name": self.name,
                        "type": self.item_type,
                    },
                )
            else:
                cursor.execute(
                    f"""INSERT INTO items VALUES (:name, :item_type, :price, :quantity)""",
                    {
                        "name": self.name,
                        "item_type": self.item_type,
                        "price": self.price,
                        "quantity": self.quantity,
                    },
                )


if __name__ == "__main__":
    postcard1 = Item("Happy Birthday card", "postcard", 1, 1)
    postcard2 = Item("Happy Birthday card", "postcard", 1, 4)  # One problem is...
    notebook1 = Item("green notebook", "notebook", 6, 3)

    connection = sqlite3.connect("lessons_with_zhenya/2022-11-17/bookstore.db")
    cursor = connection.cursor()

    Item.create_table(connection)

    cursor.execute("DELETE FROM items")

    postcard1.add_to_table(connection)
    postcard2.add_to_table(connection)
    notebook1.add_to_table(connection)

    cursor.execute("SELECT * FROM items")
    print(cursor.fetchall())
