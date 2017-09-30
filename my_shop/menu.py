from my_shop.baza import DataSQL
from my_shop.koszyk import Cart

import os

class Menu:
    def __init__(self, db_file):
        self.db_file = db_file
        self.hello = 'Witaj w sklepie Magdordy i Tomka!'
        self.options = """Wybierz co chcesz zrobić. Menu:
        1. Lista dostępnych produktów
        2. Dodaj produkt do koszyka
        3. Podgląd koszyka
        4. Edycja koszyka
        5. Zakończ zamówienie
        6. Pomoc"""
        self.switch = {'-1': self.error_message,
                        '1': self.products_list,
                        '2': self.add_to_cart,
                        '3': self.show_cart,
                        '4': self.edit_cart,
                        '5': self.finish,
                        '6': self.help_shop
                       }
        self.cart = Cart()

    def error_message(self):
        print('Niedozwolona operacja! Spróbuj jeszcze raz.')

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
        prod_id = input('Podaj id produktu: ')
        with DataSQL(self.db_file) as db:
            prod = db.get_product(prod_id)
        if not prod:
            return  #TODO obsluga gdy nie ma takiego produktu
        quantity = input('Podaj ilosc produktow: ')
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
        choice_id = str(input('Wybierz czynnosc: ')).strip()
        if choice_id not in self.switch.keys():
            return '-1'
        return choice_id

    def finish(self):
        pass

    def help_shop(self):
        print(self.options)

    def run(self):
        print(self.hello)
        print(self.options)

        while True:
            # os.system('clear')
            # może dodamy czyszczenie ekranu
            choice_id = self.user_input()
            choice = self.switch[choice_id]
            choice()

            # break


if __name__ == '__main__':
    m = Menu('shop_data_base.db')
    m.run()