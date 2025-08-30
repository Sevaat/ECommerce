from typing import Self, Union

from src.product.product import Product


class LawnGrass(Product):

    def __init__(
        self,
        name: str,
        description: str,
        price: Union[int, float],
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        if not (isinstance(country, str) and isinstance(germination_period, str) and isinstance(color, str)):
            raise TypeError("Недопустимое значение: неверный тип данных")
        if price < 0 or quantity < 0:
            raise ValueError("Недопустимое значение: отрицательная величина")
        self.country = country
        self.germination_period = germination_period
        self.color = color

    @classmethod
    def new_product(cls, product: dict) -> Union[None, Self]:
        """
        Метод преобразования словаря в объект класса
        :param product: словарь с данными
        :return: объект класса LawnGrass
        """
        attributes = ["name", "description", "price", "quantity", "country", "germination_period", "color"]
        if all(attribute in product for attribute in attributes):
            name = product["name"]
            description = product["description"]
            price = product["price"]
            quantity = product["quantity"]
            country = product["country"]
            germination_period = product["germination_period"]
            color = product["color"]
            return cls(name, description, price, quantity, country, germination_period, color)
        else:
            raise ValueError("Недопустимое значение: неверные данные словаря")
