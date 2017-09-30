
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

# def test_update_product():
#     from my_shop.koszyk import Cart
#     cr = Cart()
#     cr.add_product([1,'krówki',22,'to sa krowki'], 12)
#     cr.add_product([2, 'serniczek', 224, 'to sa ser'], 3)
#
#     assert False #function not testable must be correct
#     #cr.update_product(2)