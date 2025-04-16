import pytest


def test_smartphone(prod_smartphone):
    """Проверка передачи параметров"""
    assert prod_smartphone.name == "Samsung Galaxy S23 Ultra"
    assert prod_smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert prod_smartphone.price == 180000.0
    assert prod_smartphone.quantity == 5
    assert prod_smartphone.efficiency == 95.5
    assert prod_smartphone.model == "S23 Ultra"
    assert prod_smartphone.memory == 256
    assert prod_smartphone.color == "Серый"


def test_add_smartphone(prod_smartphone, prod_smartphone2):
    """Проверка суммы общего количества продуктов"""
    assert prod_smartphone + prod_smartphone2 == 2580000.0


def test_add_smartphone_error(prod_smartphone):
    """Проверка при сложении разных объектов"""
    with pytest.raises(TypeError):
        assert prod_smartphone + 1
