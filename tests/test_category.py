
def test_product_init(first_category, second_category):
    assert first_category.name == "Смартфоны"
    assert first_category.description == ("Смартфоны, как средство не только коммуникации, "
                                          "но и получение дополнительных функций для удобства жизни")
    assert len(first_category.products_in_list) == 2

    assert first_category.category_count == 2
    assert second_category.category_count == 2

    assert first_category.product_count == 3
    assert second_category.product_count == 3


def test_product_list_property(first_category):
    assert first_category.products == ("Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт."
                                       "\nIphone 15, 210000.0 руб. Остаток: 14 шт.\n")


def test_category_str(first_category):
    """Тест для проверки отображения правильного название и общее количество продуктов"""
    assert str(first_category) == "Смартфоны, количество продуктов: 2 шт."
