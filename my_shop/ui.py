
class UserInterface:
    def __init__(self):
        self.hello = 'Witaj w sklepie Magdordy i Tomka!'
        self.options = """Wybierz co chcesz zrobić. Menu:
        1. Lista dostępnych produktów
        2. Dodaj produkt do koszyka
        3. Podgląd koszyka
        4. Edycja koszyka
        5. Zakończ zamówienie
        6. Pomoc"""


    def error_message(self):
        print('Niedozwolona operacja! Spróbuj jeszcze raz.')

    def error_index(self):
        print('Nie ma przedmiotu o takim indeksie.')

    def input_main_menu(self):
        choice_id = str(input('Wybierz czynnosc: ')).strip()
        return choice_id

    def cart_product_id(self):
        val = input('Podaj id produktu: ')
        # if val in self.
        #     pass
        return val

    def cart_product_quantity(self):
        val=input('Podaj ilosc produktow: ')
        return val

    def input_product_quantity():
        quantity = int(input('Podaj nową ilość produktu: '))
        return quantity

    @staticmethod
    def print_output(message):
        print(message)

