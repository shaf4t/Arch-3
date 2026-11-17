class Product:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price

    def get_price(self, quantity):
        if quantity >= 100:
            discount = 0.20
        elif quantity >= 10:
            discount = 0.10
        else:
            discount = 0

        return quantity * self.price * (1 - discount)

    def make_purchase(self, quantity):
        self.amount -= quantity


if __name__ == "__main__":
    pass