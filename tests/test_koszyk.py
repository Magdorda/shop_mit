from unittest.mock import patch
from unittest import mock

#TODO ALL Unittests need correction

def test_add_product():
    from my_shop.koszyk import Cart
    cr = Cart()
    cr.add_product([1,'krówki',22,'to sa krowki'], 12)
    cr.add_product([2, 'serniczek', 224, 'to sa ser'], 3)
    prodA = cr.content[0]
    assert prodA['id'] == 1
    assert prodA['name'] == 'krówki'
    assert prodA['price'] == 22
    assert prodA['quantity'] ==12

    prodB = cr.content[1]
    assert prodB['id'] == 2
    assert prodB['name'] == 'serniczek'
    assert prodB['price'] == 224
    assert prodB['quantity'] == 3

def test_remove_product():
    from my_shop.koszyk import Cart
    cr = Cart()
    cr.add_product([1,'krówki',22,'to sa krowki'], 12)
    cr.add_product([2, 'serniczek', 224, 'to sa ser'], 3)

    assert len(cr.content) == 2
    cr.remove_product(1)
    assert len(cr.content) == 1

def test_products_list_menu():
    from my_shop.menu import Menu

    m = Menu('shop_data_base.db')
    with patch('builtins.input', return_value='1'):
        m.main_proggramm()
    assert True


#using mock instead input
def test_add_to_cart():
    from my_shop.menu import Menu
    with patch('my_shop.ui.UserInterface.cart_product_id', return_value='1'):
        with patch('my_shop.ui.UserInterface.cart_product_quantity', return_value='10'):
            # import my_shop.ui.Cart
            m = Menu('shop_data_base.db')
            m.add_to_cart()
        with patch('my_shop.ui.UserInterface.input_main_menu', return_value='3'):
            m.main_proggramm()

def test_not_proper_add_to_cart():
    from my_shop.menu import Menu
    with patch('my_shop.ui.UserInterface.input_main_menu', return_value='2'):
        with patch('my_shop.ui.UserInterface.cart_product_id', return_value='21'):
            m = Menu('shop_data_base.db')
            m.main_proggramm()
            m.main_proggramm()
