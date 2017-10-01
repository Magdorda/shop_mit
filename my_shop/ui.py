class UserInterface:
    def __init__(self):
        self.messages = {
            'hello': 'Witaj w sklepie Magdordy i Tomka!',

            'user_options_help_message': """Wybierz co chcesz zrobić. Menu:
        1. Lista dostępnych produktów
        2. Dodaj produkt do koszyka
        3. Podgląd koszyka
        4. Edycja koszyka
        5. Zakończ zamówienie
        6. Pomoc
        7. Koniec""",

            'products_list': 'Lista produktów: ',
            'add_to_cart': 'Dodawanie produktu do koszyka.',
            'edit_cart': 'Edycja koszyka.',
            'edit_cart_choose': '1. Usuń produkt\n2. Zmień ilosc produktu',
            'end_or_order': 'Koniec zamówienia.'
        }

        self.messages_custromer = {
            'name_exists': 'Taka nazwa uzytkownika istnieje juz w systemie.'
        }

        self.messages_cart = {
            'products_in_cart': '\nProdukty w koszyku: \n',
            'total_order': 'SUMA ZAMÓWIENIA {0:40}',
            'cart_products': '{name} \t ilość: {quantity} \tcena:{price} \t suma:{suma}\n'
        }

        self.error_messages = {  # TODO
            'wrong_operation': 'Niedozwolona operacja! Spróbuj jeszcze raz.',
            'not_such_item': 'Nie ma przedmiotu o takim indeksie.',
            'no_such_index': 'Nie ma przedmiotu o takim indeksie.'
        }

    def error_message(self, error_message='wrong_operation'):
        print(self.error_messages[error_message])

    def input_main_menu(self):
        choice_id = str(input('Wybierz czynnosc: ')).strip()
        return choice_id

    # def user_input(self):  # TODO move this to ui
    #     choice_id = self.ui.input_main_menu()
    #     if choice_id not in self.switch.keys():
    #         return '-1'
    #     return choice_id

    def validate_input(self, choice_id, menu_keys):
        '''

        :param choice_id: input from user
        :param menu_keys: all possible choices
        :return: choice id if is ok, if not return '-1', '-1' is error
        '''
        if choice_id not in menu_keys:
            return '-1'
        return choice_id

    def in_customer(self):
        while True:
            print('1. Zaloguj \n2.Zarejestruj')
            choice = input('Wybierz opcje: ')
            if choice == '1' or choice == '2':
                return choice
            print('Wybierz 1 lub 2.')

    def in_login_name(self):
        name = input('Podaj nazwe uzytkownika')
        return name

    def in_login_password(self):
        pass_in = input('Podaj haslo')
        return pass_in

    def in_register_name(self):
        user_name = input('Podaj unikalną nazwę użytkownika: ')
        return user_name

    def in_register_password(self):
        password = input('Wybierz haslo: ')
        return password

    def in_product_name(self):
        prod_name = input('Podaj nazwe produktu do edycji: ')
        return prod_name

    def in_edit_cart(self):
        choice = str(input('Wybierz czynnosc edycji: '))
        return choice

    # def existing_name(self):
    #     print('Taka nazwa uzytkownika istnieje juz w systemie.')

    def no_custom(self):
        print('Nie ma tkiego uzytkownika.')

    def incorrect_pass(self):
        print('Haslo niepoprawne!')

    def cart_product_id(self):
        val = input('Podaj id produktu: ')
        # if val in self.
        #     pass
        return val

    def cart_product_quantity(self):
        val = input('Podaj ilosc produktow: ')
        return val

    def input_product_quantity(self):
        quantity = int(input('Podaj nową ilość produktu: '))
        return quantity


if __name__ == '__main__':
    ui = UserInterface()
    print(ui.messages_cart['products_in_cart'])