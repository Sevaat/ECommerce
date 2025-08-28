import json
import os
import tempfile
from pathlib import Path

from src.category import Category
from src.file_manager import file_upload

file_dir = Path(__file__).resolve().parent.parent / "data"
os.makedirs(file_dir, exist_ok=True)
file_handler = f"{file_dir}/test_data.json"


def test_file_manager_correct_reading():
    # Тест корректной инициализации
    test_data = [
        {
            "name": "Электроника",
            "description": "Электронные устройства",
            "products": [
                {"name": "Телефон", "description": "Смартфон", "price": 500.0, "quantity": 10},
                {"name": "Ноутбук", "description": "Игровой ноутбук", "price": 1500.0, "quantity": 5},
            ],
        },
        {
            "name": "Книги",
            "description": "Печатная продукция",
            "products": [
                {"name": "Роман", "description": "Художественная литература", "price": 20.0, "quantity": 100}
            ],
        },
    ]

    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as file:
        json.dump(test_data, file)
        temp_filename = file.name

    result = file_upload(temp_filename)

    assert isinstance(result, list)
    assert len(result) == 2
    assert isinstance(result[0], Category)
    assert result[0].name == "Электроника"
    assert result[0].description == "Электронные устройства"
    assert len(result[0].products) == 2
    assert len(result[1].products) == 1
    assert result[0].products[0].name == "Телефон"
    assert result[0].products[1].price == 1500.0

    os.unlink(temp_filename)


def test_file_manager_file_not_found():
    # Тест загрузки несуществующего файла
    result = file_upload("nonexistent_file.json")
    assert result == []


def test_file_manager_invalid_json_format():
    # Тест обработки файла с невалидным json
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        f.write('{"invalid: json"}')
        temp_filename = f.name

    result = file_upload(temp_filename)
    assert result == []

    os.unlink(temp_filename)


def test_file_manager_required_fields():
    # Тест с отсутствующими полями в json
    test_data = [{"description": "Описание", "products": []}]

    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        json.dump(test_data, f)
        temp_filename = f.name

    result = file_upload(temp_filename)
    assert result == []

    os.unlink(temp_filename)
