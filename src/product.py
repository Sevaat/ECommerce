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
            and (isinstance(price, float) or isinstance(price, int))
            and isinstance(quantity, int)
        ):
            raise ValueError("Недопустимое значение: неверный тип данных")
        if price < 0 or quantity < 0:
            raise ValueError("Недопустимое значение: отрицательная величина")
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product: dict) -> Union[None, Self]:
        """
        Метод преобразования словаря в объект класса
        :param product: словарь с данными
        :return: объект класса Product
        """
        if "name" in product and "description" in product and "price" in product and "quantity" in product:
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
