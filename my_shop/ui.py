
class UserInterface:
    def __init__(self):
        self.hello = 'Witaj w sklepie Magdordy i Tomka!'
        self.options = """Wybierz co chcesz zrobić. Menu:
        1. Lista dostępnych produktów
        2. Dodaj produkt do koszyka
        3. Podgląd koszyka
        4. Edycja koszyka
        5. Zakończ zamówienie
        6. Pomoc
        7. Koniec"""


    def error_message(self):
        print('Niedozwolona operacja! Spróbuj jeszcze raz.')

    def error_index(self):
        print('Nie ma przedmiotu o takim indeksie.')

    def input_main_menu(self):
        choice_id = str(input('Wybierz czynnosc: ')).strip()
        return choice_id

    def custom_input(self):
        while True:
            print('1. Zaloguj \n2.Zarejestruj')
            choice = input('Wybierz opcje: ')
            if choice == '1' or choice == '2':
                return choice
            print('Wybierz 1 lub 2.')

    def login_name(self):
        name = input('Podaj nazwe uzytkownika')
        return name

    def login_pass(self):
        pass_in = input('Podaj haslo')
        return pass_in

    def no_custom(self):
        print('Nie ma tkiego uzytkownika.')

    def incorrect_pass(self):
        print('Haslo niepoprawne!')

    def register_name(self):
        user_name = input('Podaj unikalną nazwę użytkownika: ')
        return user_name

    def register_pass(self):
        password = input('Wybierz haslo: ')
        return password

    def existing_name(self):
        print('Taka nazwa uzytkownika istnieje juz w systemie.')



    def print_output(self):
        pass
    def cart_product_id(self):
        val = input('Podaj id produktu: ')
        # if val in self.
        #     pass
        return val

    def cart_product_quantity(self):
        val=input('Podaj ilosc produktow: ')
        return val

    def input_product_quantity(self):
        quantity = int(input('Podaj nową ilość produktu: '))
        return quantity

    @staticmethod
    def print_output(message):
        print(message)

