import pytest

from src.product.lawn_grass import LawnGrass
from src.product.product import Product
from src.product.smartphone import Smartphone


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


@pytest.fixture
def different_products():
    product1 = Product("P1", "DP1", 1.0, 1)
    product2 = Product("P2", "DP2", 2.0, 2)
    smartphone1 = Smartphone("S1", "DS1", 1.0, 1, 1, "M1", 1, "C1")
    smartphone2 = Smartphone("S2", "DS2", 2.0, 2, 2, "M2", 2, "C2")
    lawn_grass1 = LawnGrass("LG1", "DLG1", 1.0, 1, "C1", "GP1", "C1")
    lawn_grass2 = LawnGrass("LG2", "DLG2", 2.0, 2, "C2", "GP2", "C2")
    return [product1, product2, smartphone1, smartphone2, lawn_grass1, lawn_grass2]


@pytest.fixture
def smartphone_data():
    name = "S1"
    description = "DS1"
    price = 1.0
    quantity = 1
    efficiency = 1
    model = "M1"
    memory = 1
    color = "C1"
    return name, description, price, quantity, efficiency, model, memory, color


@pytest.fixture
def smartphone_data_dict():
    data = {
        "name": "S1",
        "description": "DS1",
        "price": 1.0,
        "quantity": 1,
        "efficiency": 1,
        "model": "M1",
        "memory": 1,
        "color": "C1",
    }
    return data


@pytest.fixture
def laws_grass_data():
    name = "S1"
    description = "DS1"
    price = 1.0
    quantity = 1
    country = "C1"
    germination_period = "GP1"
    color = "C1"
    return name, description, price, quantity, country, germination_period, color


@pytest.fixture
def laws_grass_data_dict():
    data = {
        "name": "S1",
        "description": "DS1",
        "price": 1.0,
        "quantity": 1,
        "country": "C1",
        "germination_period": "GP1",
        "color": "C1",
    }
    return data
