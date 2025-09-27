import pytest

from src.product.product import Product
from src.product.smartphone import Smartphone


def test_smartphone_correct_initialization(smartphone_data):
    # Тест корректной инициализации
    smartphone = Smartphone(*smartphone_data)

    assert isinstance(smartphone, Smartphone)
    assert isinstance(smartphone, Product)
    assert smartphone.name == smartphone_data[0]
    assert smartphone.description == smartphone_data[1]
    assert smartphone.price == smartphone_data[2]
    assert smartphone.quantity == smartphone_data[3]
    assert smartphone.efficiency == smartphone_data[4]
    assert smartphone.model == smartphone_data[5]
    assert smartphone.memory == smartphone_data[6]
    assert smartphone.color == smartphone_data[7]


def test_smartphone_negative_price(smartphone_data):
    # Тест с отрицательной стоимостью
    name, description, price, quantity, efficiency, model, memory, color = smartphone_data
    with pytest.raises(ValueError):
        Smartphone(name, description, -1, quantity, efficiency, model, memory, color)


def test_smartphone_incorrect_quantity(smartphone_data):
    # Тест с отрицательным и нулевым количеством
    name, description, price, quantity, efficiency, model, memory, color = smartphone_data
    with pytest.raises(ValueError):
        Smartphone(name, description, price, 0, efficiency, model, memory, color)
    with pytest.raises(ValueError):
        Smartphone(name, description, price, -1, efficiency, model, memory, color)


def test_smartphone_invalid_data_type_name(smartphone_data):
    # Тест с неверными типами данных
    sd = smartphone_data

    with pytest.raises(TypeError):
        Smartphone(sd[0], sd[1], sd[2], sd[3], "inf", sd[5], sd[6], sd[7])

    with pytest.raises(TypeError):
        Smartphone(sd[0], sd[1], sd[2], sd[3], sd[4], float("inf"), sd[6], sd[7])

    with pytest.raises(TypeError):
        Smartphone(sd[0], sd[1], sd[2], sd[3], sd[4], sd[5], "inf", sd[7])

    with pytest.raises(TypeError):
        Smartphone(sd[0], sd[1], sd[2], sd[3], sd[4], sd[5], sd[6], float("inf"))


def test_smartphone_initialization_from_dictionary(smartphone_data, smartphone_data_dict):
    # Тест инициализации объекта по данным словаря
    smartphone = Smartphone.new_product(smartphone_data_dict)

    assert isinstance(smartphone, Smartphone)
    assert isinstance(smartphone, Product)
    assert smartphone.name == smartphone_data[0]
    assert smartphone.description == smartphone_data[1]
    assert smartphone.price == smartphone_data[2]
    assert smartphone.quantity == smartphone_data[3]
    assert smartphone.efficiency == smartphone_data[4]
    assert smartphone.model == smartphone_data[5]
    assert smartphone.memory == smartphone_data[6]
    assert smartphone.color == smartphone_data[7]


def test_smartphone_initialization_from_dictionary_with_error(smartphone_data_dict):
    # Тест инициализации объекта по данным словаря с ошибкой
    dict_with_error = smartphone_data_dict
    dict_with_error["efficiency"] = "inf"
    with pytest.raises(TypeError):
        Smartphone.new_product(dict_with_error)

    dict_with_error = smartphone_data_dict
    dict_with_error["model"] = float("inf")
    with pytest.raises(TypeError):
        Smartphone.new_product(dict_with_error)

    dict_with_error = smartphone_data_dict
    dict_with_error["memory"] = "inf"
    with pytest.raises(TypeError):
        Smartphone.new_product(dict_with_error)

    dict_with_error = smartphone_data_dict
    dict_with_error["color"] = float("inf")
    with pytest.raises(TypeError):
        Smartphone.new_product(dict_with_error)

    dict_with_error = smartphone_data_dict
    del dict_with_error["color"]
    with pytest.raises(ValueError):
        Smartphone.new_product(dict_with_error)
