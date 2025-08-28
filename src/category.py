class Category:
    name: str
    description: str
    products: list
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name, description, products):
        if not (isinstance(name, str) and isinstance(description, str) and isinstance(products, list)):
            raise ValueError("Недопустимое значение: неверный тип данных")
        self.name = name
        self.description = description
        self.products = products
        Category.category_count += 1
        Category.product_count = len(products)
