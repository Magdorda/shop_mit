from my_shop.baza import DataSQL

class Customer:
    def __init__(self, db_file, ui):
        self.db_file = db_file
        self.ui = ui

    def login(self, name, pass_in): #TODO change all methods, istead in should have parameters
        custom = self.get_customer_from_db(name)
        if not custom:
            return None
        ok = (pass_in == custom['password'])
        if not ok:
            print(self.ui.messages_customer['incorect_pass'])
            return None
        return custom

    def register(self, try_name, password):
        name_db = self.get_customer_from_db(try_name)
        db_name = None
        if isinstance(name_db, dict):
            db_name = name_db['user_name']
        ok = (try_name != db_name)
        if not ok:
            print('taki użytkownik już istnieje')
            return '-1'
        with DataSQL(self.db_file) as db:
            db.add_new_customer(try_name, password)
        custom = self.get_customer_from_db(try_name)
        print('zarejestrowano użytkownika')
        return custom


    def get_customer_from_db(self, name):
        with DataSQL(self.db_file) as db:
            custom = db.get_customer(name)
            return custom

    def login_customer(self, choice):
        while True:
            if choice == '1':
                custom = self.login()
                if custom:
                    break
                else:
                    print(self.ui.messages_customer['no_such_customer'])
            elif choice == '2':
                self.register()
                return None
        return custom


if __name__ == '__main__':
    from my_shop.ui import UserInterface
    ui = UserInterface()
    c = Customer('shop_data_base.db', ui)
    cust = c.login_customer()
    print(cust)


