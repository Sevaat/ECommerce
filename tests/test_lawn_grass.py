import pytest

from src.product.lawn_grass import LawnGrass
from src.product.product import Product


def test_laws_grass_correct_initialization(laws_grass_data):
    # Тест корректной инициализации
    laws_grass = LawnGrass(*laws_grass_data)

    assert isinstance(laws_grass, LawnGrass)
    assert isinstance(laws_grass, Product)
    assert laws_grass.name == laws_grass_data[0]
    assert laws_grass.description == laws_grass_data[1]
    assert laws_grass.price == laws_grass_data[2]
    assert laws_grass.quantity == laws_grass_data[3]
    assert laws_grass.country == laws_grass_data[4]
    assert laws_grass.germination_period == laws_grass_data[5]
    assert laws_grass.color == laws_grass_data[6]


def test_laws_grass_invalid_data_type_name(laws_grass_data):
    # Тест с неверными типами данных
    lgd = laws_grass_data

    with pytest.raises(TypeError):
        LawnGrass(lgd[0], lgd[1], lgd[2], lgd[3], float("inf"), lgd[5], lgd[6])

    with pytest.raises(TypeError):
        LawnGrass(lgd[0], lgd[1], lgd[2], lgd[3], lgd[4], float("inf"), lgd[6])

    with pytest.raises(TypeError):
        LawnGrass(lgd[0], lgd[1], lgd[2], lgd[3], lgd[4], lgd[5], float("inf"))


def test_laws_grass_initialization_from_dictionary(laws_grass_data, laws_grass_data_dict):
    # Тест инициализации объекта по данным словаря
    laws_grass = LawnGrass.new_product(laws_grass_data_dict)

    assert isinstance(laws_grass, LawnGrass)
    assert isinstance(laws_grass, Product)
    assert laws_grass.name == laws_grass_data[0]
    assert laws_grass.description == laws_grass_data[1]
    assert laws_grass.price == laws_grass_data[2]
    assert laws_grass.quantity == laws_grass_data[3]
    assert laws_grass.country == laws_grass_data[4]
    assert laws_grass.germination_period == laws_grass_data[5]
    assert laws_grass.color == laws_grass_data[6]


def test_laws_grass_initialization_from_dictionary_with_error(laws_grass_data_dict):
    # Тест инициализации объекта по данным словаря с ошибкой
    dict_with_error = laws_grass_data_dict
    dict_with_error["country"] = float("inf")
    with pytest.raises(TypeError):
        LawnGrass.new_product(dict_with_error)

    dict_with_error = laws_grass_data_dict
    dict_with_error["germination_period"] = float("inf")
    with pytest.raises(TypeError):
        LawnGrass.new_product(dict_with_error)

    dict_with_error = laws_grass_data_dict
    dict_with_error["color"] = float("inf")
    with pytest.raises(TypeError):
        LawnGrass.new_product(dict_with_error)

    dict_with_error = laws_grass_data_dict
    del dict_with_error["color"]
    with pytest.raises(ValueError):
        LawnGrass.new_product(dict_with_error)
