import sys
from my_shop.baza import DataSQL
from my_shop.koszyk import Cart
from my_shop.klient import Customer
from my_shop.ui import UserInterface

# import os

class Menu:
    def __init__(self, db_file):
        self.ui = UserInterface()
        self.db_file = db_file
        self.switch = {'-1': self.ui.error_message,
                        '1': self.products_list,
                        '2': self.add_to_cart,
                        '3': self.show_cart,
                        '4': self.edit_cart,
                        '5': self.finish,
                        '6': self.help_shop,
                        '7': self.end
                       }
        self.cart = Cart()


    def products_list(self):
        print('Lista produktów: ')
        with DataSQL(self.db_file) as db:
            products = db.product_list_string()
            print(products)

    def show_cart(self):
        content = self.cart.get_cart_content()
        print(content)

    def add_to_cart(self):
        print('Dodawanie produktu do koszyka.')
        prod_id = self.ui.cart_product_id()#input('Podaj id produktu: ')
        with DataSQL(self.db_file) as db:
            try:
                prod = db.get_product(prod_id)
            except Exception:
                self.ui.error_index()
                return '-1'
        quantity = self.ui.cart_product_quantity()#input('Podaj ilosc produktow: ')
        quantity = int(quantity)
        self.cart.add_product(prod, quantity)

    def edit_cart(self):
        print('Edycja koszyka.')
        prod_name = input('Podaj nazwe produktu do edycji: ')
        print('1. Usuń produkt\n2. Zmień ilosc produktu')
        choice = input('Wybierz czynnosc edycji: ')
        if choice == '1':
            self.cart.remove_product(prod_name)
        elif choice == '2':
            self.cart.update_product(prod_name)

    def user_input(self):
        choice_id = self.ui.input_main_menu()
        if choice_id not in self.switch.keys():
            return '-1'
        return choice_id

    def finish(self):
        print('Koniec zamoweinia.')
        c = Customer(self.db_file, self.ui)
        cust = c.get_customer()
        print('uzytkownik to: ', cust)

    def end(self):
        sys.exit(0)

    def help_shop(self):
        print(self.ui.options)

    def run(self):
        print(self.ui.hello)
        print(self.ui.options)

        while True:
            self.main_proggramm()

    def main_proggramm(self):
        # os.system('clear')
        # może dodamy czyszczenie ekranu
        choice_id = self.user_input()
        choice = self.switch[choice_id]
        choice()

if __name__ == '__main__':
    m = Menu('shop_data_base.db')
    m.run()