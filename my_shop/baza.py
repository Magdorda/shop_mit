'''

all db methods return dictionaries

'''

import sqlite3

class DataSQL:
    '''
    all get methods return dictionaries with columnnames
    '''
    def __init__(self, file_name):
        self.file_name = file_name
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.file_name)
        self.cursor = self.connection.cursor()
        self.cursor.row_factory = self.dict_factory
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

    @staticmethod
    def dict_factory(cursor, row):
        '''
        method that create dictionary from sql column indexes
        '''
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def get_product_list(self):
        result = []
        names = ('id','name','price','description')
        for row in self.cursor.execute('SELECT * FROM product'):
            result.append(row)
        return result

    def product_list_string(self):
        result = ''
        prod_list = self.get_product_list()
        [print('\t'+name, end='\t') for name in (prod_list[0].keys())]
        print()
        for el in prod_list:
            for key in el.keys():
                # print(el[key])
                if not el[key]:
                    el[key] = ''
                result += '{0:10}'.format(str(el[key]))
            result +='\n'
        return result

    def get_product(self, id):
        self.cursor.execute('SELECT * FROM product WHERE id = ?', id)
        names = ('id', 'name', 'price', 'description')
        result = self.cursor.fetchone()
        return result

    def get_customer(self, name):
        self.cursor.execute("SELECT * FROM customer WHERE user_name=?", (str(name),))
        fields = ['id', 'name','password']
        result = self.cursor.fetchone()
        return result

    def add_new_customer(self, name, password):
        self.cursor.execute('INSERT INTO customer (user_name, password) values (?, ?)', (name, password))
        self.connection.commit()

    def add_cart_to_order(self, username, cart):
        '''
        :param username: string variable
        :param cart: list of dictionaries with id and quantity of products in cart
        :return: None
        '''
        customer = self.get_customer(username)
        id = customer['id']
        self.cursor.execute('INSERT INTO "order" (customer_id) values(?)', (str(id),))
        self.connection.commit()
        self.cursor.execute('SELECT id from "order" ORDER BY id DESC')
        last_order_id = self.cursor.fetchone()['id']

        for item in cart:
            print(item['id'], item['quantity'])
            self.cursor.execute("insert into  order_details (order_id, product_id, quantity) values (?, ?, ?)",\
                                (str(last_order_id), str(item['id']), str(item['quantity'])))
        self.connection.commit()

####temporary tests

def _tst_get_customer():
    with DataSQL('shop_data_base.db') as db:
        cust = db.get_customer('tomek')
        print(cust)

def _sample_cart_content():
    content=[{'id': 1, 'name': 'krówki', 'price': 22, 'description': 'to sa krowki', 'quantity': 12}, {'id': 1, 'name': 'serniczek', 'price': 224, 'description': 'to sa ser', 'quantity': 12}]
    with DataSQL('shop_data_base.db') as db:
        db.add_cart_to_order('Kuba', content)

def _tst_product_lits():
    with DataSQL('shop_data_base.db') as db:
        print(db.get_product_list())
    dsq = DataSQL('')

def _test_products_string():
    with DataSQL('shop_data_base.db') as db:
        print(db.product_list_string())
    dsq = DataSQL('')

def _test_get_customer():
    with DataSQL('shop_data_base.db') as db:
        print(db.get_customer('tomek'))
if __name__ == '__main__':
    # _tst_get_customer()
    # _sample_cart_content()
    # _tst_product_lits()
    # _test_products_string()
    _test_get_customer()