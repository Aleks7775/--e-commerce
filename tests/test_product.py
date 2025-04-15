from src.product import Product


def test_product_init(product):
    assert product.name == "Samsung Galaxy C23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_create(capsys):
    """Проверка инициализации атрибута ожидаемым значениям, так же проверка
    изменения цены и если цена равна или ниже нуля, выводите сообщение в консоль"""
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5
    product1.price = 10
    assert product1.price == 10
    product1.price = -100
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"


def test_str_product(product, product2):
    """Тест для проверки правильного отображения метода __str__"""
    assert str(product) == "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert str(product2) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."


def test_add_category(product, product2):
    """Тест для проверки сложения общего quantity"""
    assert product + product2 == 2580000.0



