import utility.math
from shopping.cart import *
from shopping.categories.category import get_categories, get_category_items

if __name__ == '__main__':
    print('PyCharm')


# print(utility.math.multiply(10,20))
# print(utility.math.divide(10,20))
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
#
# add_item("apple")
# add_item("orange")
# add_item("banana")
# print(cart_items())
#
# remove_item("apple")
# print(cart_items())
#
# for category in get_categories():
#     print(f"Items in {category} Category are...")
#     print(get_category_items(category))


def do_stuff(num):
    try:
        return int(num) + 5
    except ValueError as err:
        return err


def guess_game(num, guess):
    if num == guess:
        return True
    return False
