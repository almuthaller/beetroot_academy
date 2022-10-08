"""
Product Store

Write a class Product that has three attributes:

    type
    name
    price

Then create a class ProductStore, which will have some Products and will operate with all products in the store. 
All methods, in case they can't perform its action, should raise ValueError with appropriate error information.

Tips: Use aggregation/composition concepts while implementing the ProductStore class. 
You can also implement additional classes to operate on a certain type of product, etc.

Also, the ProductStore class must have the following methods:

    add(product, amount) - adds a specified quantity of a single product with a predefined price premium for your store(30 percent)
    set_discount(identifier, percent, identifier_type='name') - adds a discount for all products specified by input identifiers 
                                                                (type or name). The discount must be specified in percentage
    sell_product(product_name, amount) - removes a particular amount of products from the store if available, in other case raises an error. 
                                         It also increments income if the sell_product method succeeds.
    get_income() - returns amount of many earned by ProductStore instance.
    get_all_products() - returns information about all available products in the store.
    get_product_info(product_name) - returns a tuple with product name and amount of items in the store.

class Product:
    pass

class ProductStore:
	pass

p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product(Food, 'Ramen, 1.5)
s = ProductStore()
s.add(p, 10)
s.add(p2, 300)
s.sell('Ramen', 10)

assert s.get_product_info('Ramen') == ('Ramen', 290)
"""

import pprint


class AvailabilityError(Exception):
    pass


class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Type: {self.type}, Name: {self.name}, Price: {self.price}€"


class ProductInfo:
    def __init__(self, product, amount, discount):
        self.product = product
        self.amount = amount
        self.discount = discount

    def __repr__(self):
        return f"{self.product}, Discount: {self.discount}%, Amount: {self.amount}"


class ProductStore:
    def __init__(self):
        self.infos = {}
        self.income = 0

    def add(self, product, amount):
        try:
            self.infos[product.name].amount += amount
        except KeyError:
            self.infos[product.name] = ProductInfo(product, amount, 30)

    def set_discount(self, identifier, percent, identifier_type="name"):
        if identifier_type == "name":
            self.infos[identifier].discount = percent
        elif identifier_type == "type":
            for p in self.infos.values():
                if p.product.type == identifier:
                    p.discount = percent
        else:
            raise ValueError("Identifier type must be 'name' or 'type'.")

    def sell_product(self, product_name, amount):
        try:
            info = self.infos[product_name]
        except KeyError:
            raise AvailabilityError("This product does not exist.")

        if info.amount < amount:
            raise AvailabilityError("There are not enough products of this type.")

        info.amount -= amount
        self.income += info.product.price * amount * (info.discount / 100)

    def get_income(self):
        return self.income

    def get_all_products(self):
        return list(self.infos.values())

    def get_product_info(self, product_name):
        return (product_name, self.infos[product_name].amount)


p = Product("Sport", "Football T-Shirt", 100)
p2 = Product("Food", "Ramen", 1.5)
s = ProductStore()
s.add(p, 10)
s.add(p2, 300)
s.sell_product("Ramen", 10)

assert s.get_product_info("Ramen") == ("Ramen", 290)

pprint.pprint(s.get_all_products())
