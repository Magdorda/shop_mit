class Cart:
    def __init__(self, ui):
        self.ui = ui
        self.content = []

    def add_product(self, prod, quantity):
        product = {'id': prod['id'], 'name': prod['name'], 'price': prod['price'], 'description': prod['description'], 'quantity': quantity}
        self.content.append(product)

    def remove_product(self, prod_id):
        for product in self.content:
            if product['id'] == int(prod_id):
                self.content.remove(product)
                print('Produkt zostal usuniety.')

    def update_product(self, prod_id, quantity=None):
        if not quantity:
            self.remove_product(prod_id)
            return
        for product in self.content:
            if product['id'] == prod_id:
                product['quantity'] = quantity

    def get_cart_content(self):
        return self.content

    def show_cart_content(self):
        # TODO show cart content
        text = self.ui.messages_cart['products_in_cart']
        cart_sum = 0
        for el in self.content:
            cart_sum += el['price'] * float(el['quantity'])
            text += self.ui.messages_cart['cart_products'].format(name=el['name'],
                                                                  quantity=el['quantity'],
                                                                  price=el['price'],
                                                                  suma=float(el['price']) * float(
                                                                      el['quantity']))
        text += self.ui.messages_cart['total_order'].format(cart_sum)
        return text

    def __str__(self):
        return self.show_cart_content()

'''
temporary tests
'''
def _test_add_products():
    from my_shop.ui import UserInterface

    ui = UserInterface()
    cr = Cart(ui)
    cr.add_product([1, 'krówki', 22, 'to sa krowki'], 12)
    cr.add_product([1, 'serniczek', 224, 'to sa ser'], 12)
    print(str(cr))
    print(cr.get_cart_content())

def _test_add_products2():
    from my_shop.ui import UserInterface

    content=[{'id': 1, 'name': 'krówki', 'price': 22, 'description': 'to sa krowki', 'quantity': 12}, {'id': 1, 'name': 'serniczek', 'price': 224, 'description': 'to sa ser', 'quantity': 12}]


    ui = UserInterface()
    cr = Cart(ui)
    cr.add_product(content[0],22)
    cr.add_product(content[1],33)
    print(str(cr))
    print(cr.show_cart_content())

def _test_print_ccontent():
    pass

if __name__ == '__main__':
    _test_add_products2()