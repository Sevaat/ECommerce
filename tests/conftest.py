import pytest

from src.product import Product


@pytest.fixture
def get_products():
    products = [
        Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
        Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
        Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
    ]
    return products


@pytest.fixture
def simple_products():
    product1 = Product("Name1", "Description1", 1.0, 1)
    product2 = Product("Name2", "Description2", 2.0, 2)
    return [product1, product2]
