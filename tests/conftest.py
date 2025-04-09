import pytest

from src.category import Category
from src.product import Product


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
