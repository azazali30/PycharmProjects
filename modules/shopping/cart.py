items = []


def add_item(item):
    return items.append(item)


def remove_item(item):
    if item is None:
        raise Exception("Please provide an item to remove")
    if items.count(item) == 0:
        raise Exception("Please provide an item to remove")
    return items.remove(item)


def cart_items():
    return items;
