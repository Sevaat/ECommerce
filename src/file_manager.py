import json
import os
from pathlib import Path
from typing import Union

from src.category import Category
from src.product import Product

file_dir = Path(__file__).resolve().parent.parent / "data"
os.makedirs(file_dir, exist_ok=True)
file_handler = f"{file_dir}/products.json"


def file_upload(filename: str = file_handler) -> Union[None, list]:
    """
    Загрузить данные категорий с файла json
    :param filename: путь к файлу json
    :return: список категорий
    """
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            categories = []
            for dt in data:
                name = dt["name"]
                description = dt["description"]
                products = [Product.new_product(prd) for prd in dt["products"]]
                categories.append(Category(name, description, products))
            return categories
    except Exception as e:
        print(f"Ошибка: {e}")
        return []
