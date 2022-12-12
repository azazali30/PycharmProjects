categories = ("Electronics", "Apparel", "Fashion", "Stationary")
category_items = {
    "Electronics": ["Computer", "Mobile Phones", "Camara", "Smart Watch", "Television"],
    "Apparel": ["Levis", "Puma", "Reebok"],
    "Fashion": ["Lakme", "Loreal", "Shahnaz"],
    "Stationary": ["Books", "Pencils", "Rubber"]
}


def get_categories():
    return list(categories)


def get_category_items(category):
    return category_items[category]
