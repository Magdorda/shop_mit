from my_shop.baza import DataSQL

class Customer:
    def __init__(self, db_file):
        self.db_file = db_file

    def login(self):
        name = input('Podaj nazwe uzytkownika')
        with DataSQL(self.db_file) as db:
            custom = db.get_customer(name)
            return custom

    def register(self):
        pass

    def get_customer(self):
        while True:
            print('1. Zaloguj \n2.Zarejestruj')
            choice = input('Wybierz opcje: ')
            if choice == '1':
                custom = self.login()
                if custom:
                    break
            elif choice == '2':
                self.register()
        customer_id = 5
        return customer_id


if __name__ == '__main__':
    c = Customer('shop_data_base.db')

