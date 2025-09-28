from inspect import signature
from typing import Self, Union

from src.product.base_product import BaseProduct
from src.product.init_logger_mixin import InitLoggerMixin


class Product(InitLoggerMixin, BaseProduct):
    def __init__(self, name: str, description: str, price: Union[int, float], quantity: int):
        if not all(
            [
                isinstance(name, str),
                isinstance(description, str),
                isinstance(price, (int, float)),
                isinstance(quantity, int),
            ]
        ):
            raise TypeError("Недопустимое значение: неверный тип данных")
        if price < 0 or quantity < 0:
            raise ValueError("Недопустимое значение: отрицательная величина")
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        params = {k: v for k, v in locals().items() if k != "self"}
        super().__init__(**params)

    def __str__(self) -> str:
        return f"{self.name}, {float(self.__price)} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Self) -> float:
        if type(self) is type(other):
            return float(self.__price * self.quantity + other.__price * other.quantity)
        else:
            raise TypeError("Недопустимое значение: разные типы данных")

    @classmethod
    def new_product(cls, product: dict) -> Union[None, Self]:
        """
        Создание продукта из данных словаря
        :param product: данные словаря
        :return: продукт
        """
        init_params = list(signature(cls.__init__).parameters.keys())[1:]
        if all(param in product for param in init_params):
            return cls(**{param: product[param] for param in init_params})
        else:
            raise ValueError("Недопустимое значение: неверные данные словаря")

    @property
    def price(self) -> Union[int, float]:
        return self.__price

    @price.setter
    def price(self, new_price: Union[int, float]) -> None:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price
