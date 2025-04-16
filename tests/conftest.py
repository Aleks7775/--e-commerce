import pytest

from src.category import Category
from src.product import Product
from src.lawnGrass import LawnGrass
from src.smartphone import Smartphone


@pytest.fixture
def first_category():
    return Category (
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, "
                    "но и получение дополнительных функций для удобства жизни",
        products=[Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, "
                                                      "200MP камера", 180000.0, 5),
                  Product("Iphone 15", "2512GB, Gray space", 210000.0, 14)]
        )


@pytest.fixture
def second_category():
    return Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться просмотром, "
                    "станет вашим другом и помощником",
        products=[Product("55 QLED 4K", "Фоновая подсветка", 123000.0, 7)]

    )


@pytest.fixture
def product():
    return Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def product2():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def prod_smartphone():
    return Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                         "S23 Ultra", 256, "Серый")


@pytest.fixture
def prod_smartphone2():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def prod_lawnGrass():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def prod_lawnGrass2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
