from typing import Union

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
        if not all([isinstance(country, str), isinstance(germination_period, str), isinstance(color, str)]):
            raise TypeError("Недопустимое значение: неверный тип данных")
        if price < 0 or quantity <= 0:
            raise ValueError("Недопустимое значение: отрицательная или нулевая величина")
        self.country = country
        self.germination_period = germination_period
        self.color = color
