

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



    def input_main_menu(self):
        choice_id = str(input('Wybierz czynnosc: ')).strip()
        return choice_id

    def print_output(self):
        pass

