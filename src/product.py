class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        if not (
            isinstance(name, str)
            and isinstance(description, str)
            and isinstance(price, float)
            and isinstance(quantity, int)
        ):
            raise ValueError("Недопустимое значение: неверный тип данных")
        if price < 0 or quantity < 0:
            raise ValueError("Недопустимое значение: отрицательная величина")
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
