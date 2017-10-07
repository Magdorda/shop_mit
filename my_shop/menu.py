'''
Menu for shop client.
'''

import sys
from my_shop.baza import DataSQL
from my_shop.koszyk import Cart
from my_shop.klient import Customer
from my_shop.ui import UserInterface

import os

class Menu:
    def __init__(self, filename_db):
        self.ui = UserInterface()
        self.filename_db = filename_db
        self.customer = Customer(self.filename_db, self.ui)
        self.switch = {'-1': {'fun': self.ui.error_message, 'args_number': 0, 'message': None, 'prompt': None},
                       '1': {'fun': self.products_list, 'args_number': 0, 'message': None, 'prompt': None},
                       '2': {'fun': self.add_to_cart, 'args_number': 2, 'message': self.ui.messages['add_to_cart'], 'prompt': ['id_produktu>', 'ilość>']},
                       '3': {'fun': self.show_cart, 'args_number': 0, 'message': None, 'prompt': None},
                       '4': {'fun': self.edit_cart, 'args_number': 2, 'message': self.ui.messages['edit_cart_choose'], 'prompt': ['polecenie>', 'id>']},
                       '5': {'fun': self.finish, 'args_number': 3, 'message': self.ui.messages['end_or_order'], 'prompt': ['kończymy?>','login>','pass>']},
                       '6': {'fun': self.help_shop, 'args_number': 0, 'message': None, 'prompt': None},
                       '7': {'fun': self.register, 'args_number': 2, 'message': self.ui.messages['register'], 'prompt': ['nazwa użytkownika>', 'hasło>']},
                       '8': {'fun': self.end, 'args_number': 0, 'message': None, 'prompt': None}
                       }
        self.cart = Cart(self.ui)

    def products_list(self):
        print(self.ui.messages['products_list'])
        with DataSQL(self.filename_db) as db:
            products = db.product_list_string()
            print(products)
            return 0

    def show_cart(self, customer=None):
        content = self.cart.show_cart_content()
        print(content)
        return 0

    def add_to_cart(self, prod_id, quantity):
        print(self.ui.messages['add_to_cart'])
        if prod_id == '0' or not prod_id.isdigit() or not quantity.isdigit():
            self.ui.error_message('no_such_index')
            return '-1'
        with DataSQL(self.filename_db) as db:
            try:
                prod = db.get_product(prod_id)
            except Exception:
                self.ui.error_message('no_such_index')
                return '-1'
        self.cart.add_product(prod, quantity)
        return 0

    def edit_cart(self, prod_name, choice):
        if choice not in ['1', '2']:
            self.ui.error_message('no_such_index')
            return '-1'

        if choice == '1':
            self.cart.remove_product(prod_name)
        elif choice == '2':
            self.cart.update_product(prod_name)
        return 0

    def register(self, name, password):
        self.customer.register(name, password)
        return 0

    def finish(self, want_to_finish, name=None, password=None):
        self.cart.show_cart_content()
        if want_to_finish != 'Tak':
            print('kontynuuj zakupy...')
            return 0
        cust = self.customer.login(name, password)
        if cust is None:  # add only if customer exists
            print('Nie ma takiego użytkownika, Zarejestruj się w skelpie M&T!')
        else:
            with DataSQL(self.filename_db) as db:
                db.add_cart_to_order(cust['user_name'], self.cart.get_cart_content())
                self.cart.content = []  # clear cart content
            print('Zamówienie gotowe, produkty powinny dotrzeć do Ciebie w ciągu 10dni.')
        return 0

    def help_shop(self):
        print(self.ui.messages['user_options_help_message'])
        return 0

    def run(self):
        while True:
            os.system('cls')  # TODO, windows->cls, unix->clear
            print(self.ui.messages['hello'])
            print(self.ui.messages['user_options_help_message'])
            self.main_proggramm()
            input("ENTER")

    def main_proggramm(self):
        command = self.ui.input_main_menu()
        choice_id = self.ui.validate_input(command, self.switch.keys())

        prompt = 'wybierz polecenie>'
        choice = self.switch[choice_id]
        func = choice['fun']
        args_number = choice['args_number']
        if choice['message']:
            print(choice['message'])
        if choice['prompt']:
            prompt = choice['prompt']

        ret=0
        while True:
            args = self.ui.get_arguments(args_number, prompt)
            ret = func(*args)
            if ret == 0:
                break
            if ret == '-1':
                self.ui.error_message()
                break

    def end(self):
        print(self.ui.messages['end'])
        sys.exit(0)
        return 0


def main(path):
    m = Menu(path)
    m.run()


if __name__ == '__main__':
    main('shop_data_base.db')
