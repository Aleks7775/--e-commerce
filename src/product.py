class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        """Отображает название цену и остаток"""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """функция для получения всех товаров на складе"""
        return self.__price * self.quantity + other.__price * other.quantity

    @classmethod
    def new_product(cls, product_data):
        """класс-метод, который будет принимать на вход параметры товара
         в словаре и возвращать созданный объект класса Product"""
        return cls(**product_data)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        """Проверка в случае если цена равна или ниже нуля, выводите сообщение в консоль"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = new_price
