from my_shop.baza import DataSQL


class DataSQLAdmin(DataSQL):
    def __init__(self, file_name):
        DataSQL.__init__(self, file_name)

    def get_all_orders(self):
        result = self.cursor.execute('''
        select
        customer.id as id_customer,
        customer.user_name,
        product.name as product_name,
        order_details.quantity
        from ((customer, "order"
        inner join
        order_details on "order".id = order_details.order_id)
        inner join product on order_details.product_id = product.id
        )
        order by id_customer;    
        ''')

        for el in result:
            print(el)
