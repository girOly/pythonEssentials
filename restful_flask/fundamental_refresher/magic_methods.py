class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Person: {self.name}, {self.age} years old"

    def __repr__(self):
        return f"<Person({self.name}, {self.age})>"
joe = Person("Joe", 35)

print(joe)


class Store:
    def __init__(self, name):
        self.name = name
        self.items = []
    
    def add_item(self, name, price):
        # Create a dictionary with keys name and price, and append that to self.items.
        item = {
            "name": name,
            "price": price
        }
        self.items.append(item)

    def stock_price(self):
        # total = 0
        # for item in self.items:
        #     total += item["price"]
        # return total
        return sum([item['price'] for item in self.items])

        # Add together all item prices in self.items and return the total.
