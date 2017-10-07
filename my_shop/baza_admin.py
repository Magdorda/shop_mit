from my_shop.baza import DataSQL


class DataSQLAdmin(DataSQL):
    def __init__(self, file_name):
        DataSQL.__init__(self, file_name)

    def get_all_orders(self):
        result = self.cursor.execute('''
select a.id as customer_ID, customer.user_name as name, order_id, b.name as product_name, quantity from customer,
(select * from "order", order_details where "order".id = order_details.order_id) as a,
(select * from product) as b
where
a.customer_id = customer.id and a.product_id = b.id
order by
customer.id;
        ''')

        print('ORDERS')
        # for el in result:
        #     print(el)

        for dictionary in result:
            for key in dictionary.keys():
                print('{} {} \t\t'.format(key, dictionary[key]), end='')
            print()