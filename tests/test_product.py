import pytest

from src.product.product import Product


def test_product_correct_initialization():
    # Тест корректной инициализации
    product = Product("Name", "Description", 1.0, 1)

    assert isinstance(product, Product)
    assert product.name == "Name"
    assert product.description == "Description"
    assert product.price == 1.0
    assert product.quantity == 1


def test_product_negative_price():
    # Тест с отрицательной стоимостью
    with pytest.raises(ValueError):
        Product("Name", "Description", -1.0, 1)


def test_product_negative_quantity():
    # Тест с отрицательным количеством
    with pytest.raises(ValueError):
        Product("Name", "Description", 1.0, -1)


def test_product_invalid_data_type_name():
    # Тест с неверными типами данных
    with pytest.raises(TypeError):
        Product(0, "Description", 1.0, 1)

    with pytest.raises(TypeError):
        Product("Name", 0, 1.0, 1)

    with pytest.raises(TypeError):
        Product("Name", "Description", "1.0", 1)

    with pytest.raises(TypeError):
        Product("Name", "Description", 1.0, "1")


def test_product_initialization_from_dictionary():
    # Тест инициализации объекта по данным словаря
    data = {"name": "Name", "description": "Description", "price": 1.0, "quantity": 1}
    product = Product.new_product(data)

    assert isinstance(product, Product)
    assert product.name == "Name"
    assert product.description == "Description"
    assert product.price == 1.0
    assert product.quantity == 1


def test_product_initialization_from_dictionary_with_error():
    # Тест инициализации объекта по данным словаря с ошибкой
    data = {"name": 0, "description": "Description", "price": 1.0, "quantity": 1}
    with pytest.raises(TypeError):
        Product.new_product(data)

    data = {"description": "Description", "price": 1.0, "quantity": 1}
    with pytest.raises(ValueError):
        Product.new_product(data)


def test_product_change_in_value():
    # Тест изменения стоимости
    product = Product("Name", "Description", 1.0, 1)
    assert product.price == 1.0

    product.price = -1.0
    assert product.price == 1.0

    product.price = 5.0
    assert product.price == 5.0


def test_product_str(simple_products):
    # Тест проверки магического метода str
    text = str(simple_products[0])

    assert "Name1, 1.0 руб. Остаток: 1 шт." == text


def test_product_add(simple_products):
    # Тест проверки магического метода add
    assert simple_products[0] + simple_products[1] == 5.0


def test_product_add_different_products(different_products):
    # Тест на сложение разных пар продуктов
    assert different_products[0] + different_products[1] == 5
    assert different_products[2] + different_products[3] == 5
    assert different_products[4] + different_products[5] == 5

    with pytest.raises(TypeError):
        different_products[0] + different_products[2]

    with pytest.raises(TypeError):
        different_products[0] + different_products[4]

    with pytest.raises(TypeError):
        different_products[2] + different_products[4]
