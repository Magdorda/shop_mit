import sqlite3

class DataSQL:
    def __init__(self, file_name):
        self.file_name = file_name
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.file_name)
        self.cursor = self.connection.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

    def get_product_list(self):
        result = []
        for row in self.cursor.execute('SELECT * FROM product'):
            result.append(row)
        return result

    def product_list_string(self):
        result = ''
        prod_list = self.get_product_list()
        for element in prod_list:
            element = list(element)
            for i, el in enumerate(element):
                if not el:
                    element[i] = ''
            result += '{}\t{}\t{}\t{}\n'.format(*element)
        return result

    def get_product(self, id):
        self.cursor.execute('SELECT * FROM product WHERE id = ?', id)
        result = self.cursor.fetchone()
        return result

    def get_customer(self, name):
        self.cursor.execute("SELECT * FROM customer WHERE user_name = ?", (name,))
        result = self.cursor.fetchone()
        return result

    def add_new_customer(self, name, password):
        self.cursor.execute('INSERT INTO customer (user_name, password) values (?, ?)', (name, password))
        self.connection.commit()

    def add_cart_to_order(self,username, password, cart):
        #TODO get customer, insert to db user id, order id for each item
        for item in cart:
            print(item)

####temporary tests

def _display_user():
    with DataSQL('shop_data_base.db') as db:
        prod = db.get_product('2')
        print(prod)

        cust = db.get_customer('tomek')
        print(cust)

def _sample_cart_content():
    content=[{'id': 1, 'name': 'krówki', 'price': 22, 'description': 'to sa krowki', 'quantity': 12}, {'id': 1, 'name': 'serniczek', 'price': 224, 'description': 'to sa ser', 'quantity': 12}]
    with DataSQL('shop_data_base.db') as db:
        db.add_cart_to_order('tomek', 'tomek',content)

    dsq = DataSQL('')
if __name__ == '__main__':
    # _display_user()
    _sample_cart_content()