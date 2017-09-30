class Cart:
    def __init__(self):
        self.content = []

    def add_product(self, prod, quantity):
        id, name, price, description = prod
        product = {'id': id, 'name': name, 'price': price, 'description': description, 'quantity': quantity}
        self.content.append(product)
        # print(self.content)

    def remove_product(self, prod_name):
        for product in self.content:
            if product['name'] == prod_name:
                self.content.remove(product)
                print('Produkt zostal usuniety.')

    def update_product(self, prod_name):
        quantity = input('Podaj nową ilość produktu: ')
        if not quantity:
            self.remove_product(prod_name)
            return
        for product in self.content:
            if product['name'] == prod_name:
                product['quantity'] = quantity

    def get_cart_content(self):
        text = '\nProdukty w koszyku: \n'
        for el in self.content:
            text += '{} \t ilość: {}\n'.format(el['name'], el['quantity'])
        return text

    def __str__(self):
        #drukuj ładnie produkty
        return self.get_cart_content()



if __name__ == '__main__':
    cr = Cart()
    cr.add_product([1,'krówki',22,'to sa krowki'], 12)
    cr.add_product([1, 'serniczek', 224, 'to sa ser'], 12)
    print(str(cr))