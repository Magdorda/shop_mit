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

    def add_cart_to_order(self,client,cart):
        pass

if __name__ == '__main__':
    with DataSQL('shop_data_base.db') as db:
        prod = db.get_product('2')
        print(prod)

        cust = db.get_customer('Tomek')
        print(cust)
