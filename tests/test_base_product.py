import pytest

from src.product.base_product import BaseProduct


def test_base_product_cannot_instantiate():
    # Тест невозможности инициализации
    with pytest.raises(TypeError):
        BaseProduct()


def test_missing_abstract_method():
    # Тест абстрактных методов
    class IncompleteProduct(BaseProduct):
        def __str__(self):
            return ""

        def __add__(self, other):
            return 0

    with pytest.raises(TypeError):
        IncompleteProduct()
