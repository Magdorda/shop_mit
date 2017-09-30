class Cart:
    def __init__(self):
        self.content = []

    def add_product(self, prod, quantity):
        id, name, price, description = prod
        product = {'id': id, 'name': name, 'price': price, 'description': description, 'quantity': quantity}
        self.content.append(product)
        # print(self.content)

    def remove_product(self, prod_id):
        for product in self.content:
            if product['id'] == int(prod_id):
                self.content.remove(product)
                print('Produkt zostal usuniety.')

    def update_product(self, prod_id):
        quantity = input('Podaj nową ilość produktu: ')
        if not quantity:
            self.remove_product(prod_id)
            return
        for product in self.content:
            if product['id'] == prod_id:
                product['quantity'] = quantity

    def get_cart_content(self):
        text ='\nProdukty w koszyku: \n'
        cart_sum=0
        for el in self.content:
            # suma= lambda: float(el['price'])*float(el['quantity'])
            cart_sum += el['price']*float(el['quantity'])
            text += '{name} \t {quantity} \tcena:{price} \t suma:{suma}\n'.format(name=el['name'],
                                                           quantity='ilość:'+str(el['quantity']),
                                                           price=el['price'],
                                                           suma=float(el['price'])*float(el['quantity']))
        text += 'SUMA ZAMÓWIENIA {0:40}'.format(cart_sum)
        return text

    def __str__(self):
        #drukuj ładnie produkty
        return self.get_cart_content()



if __name__ == '__main__':
    cr = Cart()
    cr.add_product([1,'krówki',22,'to sa krowki'], 12)
    cr.add_product([1, 'serniczek', 224, 'to sa ser'], 12)
    print(str(cr))