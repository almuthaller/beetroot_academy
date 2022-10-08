"""
Create a function which takes as input two dicts with structure mentioned above, 
then computes and returns the total price of stock.
"""

stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}

prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}


def total_price(dict1, dict2):
    total_stock_price = 0

    for key in dict1:
        total_stock_price += dict1[key] * dict2[key]

    return total_stock_price


print(total_price(stock, prices))
