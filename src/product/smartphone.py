from typing import Union

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
        if not all(
            [
                (isinstance(efficiency, int) or isinstance(efficiency, float)),
                isinstance(model, str),
                (isinstance(memory, int) or isinstance(memory, float)),
                isinstance(color, str),
            ]
        ):
            raise TypeError("Недопустимое значение: неверный тип данных")
        if price < 0 or quantity < 0:
            raise ValueError("Недопустимое значение: отрицательная величина")
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
