from typing import Self, Union

from src.product.product import Product


class Smartphone(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: Union[int, float],
        quantity: int,
        efficiency: Union[int, float],
        model: str,
        memory: Union[int, float],
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        if not (
            (isinstance(efficiency, int) or isinstance(efficiency, float))
            and isinstance(model, str)
            and (isinstance(memory, int) or isinstance(memory, float))
            and isinstance(color, str)
        ):
            raise ValueError("Недопустимое значение: неверный тип данных")
        if price < 0 or quantity < 0:
            raise ValueError("Недопустимое значение: отрицательная величина")
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    @classmethod
    def new_product(cls, product: dict) -> Union[None, Self]:
        """
        Метод преобразования словаря в объект класса
        :param product: словарь с данными
        :return: объект класса Smartphone
        """
        attributes = ["name", "description", "price", "quantity", "efficiency", "model", "memory", "color"]
        if all(attribute in product for attribute in attributes):
            name = product["name"]
            description = product["description"]
            price = product["price"]
            quantity = product["quantity"]
            efficiency = product["efficiency"]
            model = product["model"]
            memory = product["memory"]
            color = product["color"]
            return cls(name, description, price, quantity, efficiency, model, memory, color)
        else:
            raise ValueError("Недопустимое значение: неверные данные словаря")
