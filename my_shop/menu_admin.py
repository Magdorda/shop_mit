from my_shop.baza_admin import DataSQLAdmin

filename = None

def menu(comm):
    if comm == '1':
        with DataSQLAdmin(filename) as db:
            db.get_all_orders()
    if comm == '2':
        exit(0)

def start(fn):
    global filename
    filename = fn
    while 1:
        print('1.Drukuj zamówiena:')
        print('2.Koniec')
        comm = str(input('admin>'))
        menu(comm)


if __name__ == '__main__':
    filename = 'shop_data_base.db'
    start(filename)