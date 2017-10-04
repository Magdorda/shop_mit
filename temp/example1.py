import sqlite3

def print_last_element():
    connection = sqlite3.connect('./my_shop/shop_data_base.db')
    cursor = connection.cursor()

    cursor.execute('SELECT id from "order" ORDER BY id DESC')
    last = cursor.fetchone()
    print(last[0])
