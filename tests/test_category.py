import pytest

from src.category import Category
from src.product import Product


def test_category_correct_initialization(get_products):
    # Тест корректной инициализации
    category = Category("Name", "Description", get_products)

    assert isinstance(category, Category)
    assert category.name == "Name"
    assert category.description == "Description"
    assert category.products == get_products
    assert category.category_count == 1
    assert category.product_count == 3


def test_category_invalid_data_type_name(get_products):
    # Тест с неверными типами данных
    with pytest.raises(ValueError):
        Category(0, "Description", get_products)

    with pytest.raises(ValueError):
        Category("Name", 0, get_products)

    with pytest.raises(ValueError):
        Category("Name", "Description", 0)


def test_category_adding_product(get_products):
    category = Category("Name", "Description", get_products)
    assert isinstance(category, Category)
    assert category.name == "Name"
    assert category.description == "Description"
    assert category.products == get_products
    assert category.category_count == 2
    assert category.product_count == 6

    product = Product("Name", "Description", 1.0, 1)

    category.add_product(product)
    assert isinstance(category, Category)
    assert category.name == "Name"
    assert category.description == "Description"
    assert product in category.products
    assert category.category_count == 2
    assert category.product_count == 7

    with pytest.raises(ValueError):
        category.add_product(0)


def test_category_product_output(simple_products):
    # Тест вывода списка продуктов
    text = """Name1, 1.0 руб. Остаток: 1 шт.
Name2, 2.0 руб. Остаток: 2 шт."""
    category = Category("Name", "Description", simple_products)

    assert text == category.output_product_list()
