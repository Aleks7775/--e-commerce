from src.product import Product


class LawnGrass(Product):
    """Создан класс 'Трава газонная', наследник от исходного класса Продукт """
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        """функция для получения всех товаров на складе с проверкой type"""
        if type(other) is LawnGrass:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError
