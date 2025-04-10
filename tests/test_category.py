
def test_product_init(first_category, second_category):
    assert first_category.name == "Смартфоны"
    assert first_category.description == ("Смартфоны, как средство не только коммуникации, "
                                          "но и получение дополнительных функций для удобства жизни")
    assert len(first_category.products) == 2

    assert first_category.quantity_categories == 2
    assert second_category.quantity_categories == 2

    assert first_category.quantity_product == 3
    assert second_category.quantity_product == 3
