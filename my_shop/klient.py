from my_shop.baza import DataSQL

class Customer:
    def __init__(self, db_file, ui):
        self.db_file = db_file
        self.ui = ui

    def login(self):
        name = self.ui.in_login_name()
        custom = self.get_customer_from_db(name)
        if not custom:
            return None
        id, user_name, password = custom
        pass_in = self.ui.in_login_password()
        ok = (pass_in == password)
        if not ok:
            self.ui.incorrect_pass()
            return None
        return custom

    def get_customer_from_db(self, name):
        with DataSQL(self.db_file) as db:
            custom = db.get_customer(name)
            return custom

    def register(self):
        while True:
            try_name = self.ui.in_register_name()
            name_db = self.get_customer_from_db(try_name)
            ok = (try_name != name_db)
            if ok:
                name = try_name
                break
            self.ui.messages_customer['name_exists']
        password = self.ui.in_register_password()
        with DataSQL(self.db_file) as db:
            db.add_new_customer(name, password)
        custom = self.get_customer_from_db(name)
        return custom

    def get_customer(self):
        while True:
            choice = self.ui.in_customer()
            if choice == '1':
                custom = self.login()
                if custom:
                    break
                else:
                    self.ui.no_custom()
            elif choice == '2':
                self.register()
        return custom


if __name__ == '__main__':
    from my_shop.ui import UserInterface
    ui = UserInterface()
    c = Customer('shop_data_base.db', ui)
    cust = c.get_customer()
    print(cust)


