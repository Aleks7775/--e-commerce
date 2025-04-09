class Category:
    name: str
    description: str
    product: list
    quantity_categories = 0
    quantity_product = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.quantity_categories += 1
        Category.quantity_product += len(products)
