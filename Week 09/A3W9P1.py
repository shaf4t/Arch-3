class Customer:
    def __init__(self, name):
        self.name = name

    def print(self):
        print(f"Name: {self.name}")


class _Vehicle:
    def __init__(self, brand, model, color, price):
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price
        self.sold = False
        self.sold_to = None

    def sell(self, customer):
        self.sold = True
        self.sold_to = customer

    def print(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")
        print(f"Price: {self.price}")
        if self.sold:
            print(f"Sold to: {self.sold_to.name}")
        else:
            print("Not sold yet")


class Car(_Vehicle):
    pass


class Motorcycle(_Vehicle):
    pass


if __name__ == "__main__":
    pass