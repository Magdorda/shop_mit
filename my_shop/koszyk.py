class Cart:
    def __init__(self):
        self.content = []

    def add_product(self, prod, quantity):
        id, name, price, description = prod
        product = {'id': id, 'name': name, 'price': price, 'description': description, 'quantity': quantity}
        self.content.append(product)
        print(self.content)

    def remove_product(self, prod_id):
        for product in self.content:
            if product['id'] == int(prod_id):
                self.content.remove(product)
                print('Produkt zostal usuniety.')
        print(self.content)

    def update_product(self, prod_id):
        quantity = input('Podaj nową ilość produktu: ')
        if not quantity:
            self.remove_product(prod_id)
            return
        for product in self.content:
            if product['id'] == prod_id:
                product['quantity'] = quantity

    def display(self):
        pass