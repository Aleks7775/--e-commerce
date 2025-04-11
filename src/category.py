class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product):
        """Метод для добавления продуктов"""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Геттер, который выводит список товаров в виде строк в данном формат"""
        product_str = ""
        for prod in self.__products:
            product_str += f"{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт.\n"
        return product_str

    @property
    def products_in_list(self):
        return self.__products
