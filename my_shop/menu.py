from my_shop.baza import DataSQL
from my_shop.koszyk import Cart

class Menu:
    def __init__(self, db_file):
        self.db_file = db_file
        self.hello = 'Witaj w sklepie Magdordy i Tomka!'
        self.options = """Wybierz co chcesz zrobić. Menu:
        1. Lista dostępnych produktów
        2. Dodaj produkt do koszyka
        3. Podgląd koszyka
        4. Zakończ zamówienie
        5. Pomoc"""
        self.switch = {'1': self.products_list, '2': self.add_to_cart}
        self.cart = Cart()

    def hello(self):
        pass

    def products_list(self):
        print('Lista produktów: ')
        with DataSQL(self.db_file) as db:
            products = db.product_list_string()
            print(products)

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




    def run(self):
        print(self.hello)
        print(self.options)

        while True:
            # może dodamy czyszczenie ekranu
            choice_id = input('Wybierz czynnosc: ')
            print('Wybrano: ', choice_id)
            choice = self.switch[choice_id]
            choice()

            # break


if __name__ == '__main__':
    m = Menu('shop_data_base.db')
    m.run()