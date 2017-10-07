import my_shop.big_fonts as big_fonts
class UserInterface:
    def __init__(self):
        self.messages = {
            'hello': big_fonts.welcome,
            'user_options_help_message': """Wybierz co chcesz zrobić. Menu:
        1. Lista dostępnych produktów
        2. Dodaj produkt do koszyka
        3. Podgląd koszyka
        4. Edycja koszyka
        5. Zakończ zamówienie
        6. Pomoc
        7. Rejestracja
        8. Koniec""",

            'products_list': 'Lista produktów: ',
            'add_to_cart': 'Dodawanie produktu do koszyka. Podaj id a następnie ilość.',
            'edit_cart_choose': 'Edycja koszyka.\n1. Usuń produkt\n2. Zmień ilosc produktu',
            'end_or_order': 'Koniec zamówienia, aby kupić podaj login i hasło.\nCzy chcesz zakończyć zamówienie??? (Tak/Nie)',
            'register': 'Rejestracja użytkownika: ',
            'end':big_fonts.bye
        }

        self.messages_custromer = {
            'name_exists': 'Taka nazwa uzytkownika istnieje juz w systemie.',
            'no_such_customer': 'Nie ma tkiego uzytkownika.',
            'incorect_pass':'Haslo niepoprawne!',
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
        return 0

    def input_main_menu(self):
        choice_id = str(input('Wybierz czynnosc>')).strip()
        return choice_id

    def get_arguments(self, arg_number, prompt_text):
        '''
        :param arg_number:
        :param prompt_text:
        :return: arguments list
        '''
        args=[]
        for i in range(arg_number):
            if type(prompt_text) == list:
                var = input(prompt_text[i%len(prompt_text)])
            else:
                var = input(prompt_text)
            if var == 'Nie' or var == 'exit' or var == -1:
                return '-1'
            args.append(var)
        return args

    def validate_input(self, choice_id, menu_keys):
        '''

        :param choice_id: input from user
        :param menu_keys: all possible choices
        :return: choice id if is ok, if not return '-1', '-1' is error
        '''
        if choice_id not in menu_keys:
            return '-1'
        return choice_id


if __name__ == '__main__':
    ui = UserInterface()
    print(ui.messages_cart['products_in_cart'])