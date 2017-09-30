class Cart:
    def __init__(self):
        self.content = []

    def add_product(self, prod, quantity):
        id, name, price, description = prod
        product = {'id': id, 'name': name, 'price': price, 'description': description, 'quantity': quantity}
        self.content.append(product)

    def delete_product(self):
        pass

    def update_product(self):
        pass

    def display(self):
        pass