from src.product import Product


class Smartphone(Product):
    """Создан класс 'Смартфон', наследник от исходного класса Продукт"""
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        """функция для получения всех товаров на складе с проверкой type"""
        if type(other) is Smartphone:
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError
