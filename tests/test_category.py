import pytest

from src.category import Category


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
