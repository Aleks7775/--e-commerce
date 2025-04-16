import pytest


def test_lawnGrass(prod_lawnGrass):
    """Проверка передачи параметров"""
    assert prod_lawnGrass.name == "Газонная трава"
    assert prod_lawnGrass.description == "Элитная трава для газона"
    assert prod_lawnGrass.price == 500.0
    assert prod_lawnGrass.quantity == 20
    assert prod_lawnGrass.country == "Россия"
    assert prod_lawnGrass.germination_period == "7 дней"
    assert prod_lawnGrass.color == "Зеленый"


def test_add_lawnGrass(prod_lawnGrass, prod_lawnGrass2):
    """Проверка суммы общего количества продуктов"""
    assert prod_lawnGrass + prod_lawnGrass2 == 16750.0


def test_add_lawnGrass_error(prod_lawnGrass):
    """Проверка при сложении разных объектов"""
    with pytest.raises(TypeError):
        assert prod_lawnGrass + 1
