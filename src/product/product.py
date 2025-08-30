from typing import Self, Union


class Product:
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: Union[int, float], quantity: int):
        if not (
            isinstance(name, str)
            and isinstance(description, str)
            and (isinstance(price, int) or isinstance(price, float))
            and isinstance(quantity, int)
        ):
            raise TypeError("Недопустимое значение: неверный тип данных")
        if price < 0 or quantity < 0:
            raise ValueError("Недопустимое значение: отрицательная величина")
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

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
        Метод преобразования словаря в объект класса
        :param product: словарь с данными
        :return: объект класса Product
        """
        attributes = ["name", "description", "price", "quantity"]
        if all(attribute in product for attribute in attributes):
            name = product["name"]
            description = product["description"]
            price = product["price"]
            quantity = product["quantity"]
            return cls(name, description, price, quantity)
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
