from src.product import Product


class Category:
    name: str
    description: str
    __products: list
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list):
        if not (isinstance(name, str) and isinstance(description, str) and isinstance(products, list)):
            raise ValueError("Недопустимое значение: неверный тип данных")
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self) -> str:
        quantity_of_products = sum([prd.quantity for prd in self.__products])
        return f"{self.name}, количество продуктов: {quantity_of_products} шт."

    def add_product(self, product: Product) -> None:
        """
        Метод добавления продукта в список
        :param product: продукт
        :return:
        """
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise ValueError("Недопустимое значение: неверный тип данных")

    @property
    def products(self) -> list:
        return self.__products

    def output_product_list(self) -> str:
        """
        Метод вывода списка продуктов
        :return: список продуктов в виде текста
        """
        text = [str(prd) for prd in self.__products]
        return "\n".join(text)
