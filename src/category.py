from src.product.product import Product


class Category:
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list):
        if not (isinstance(name, str) and isinstance(description, str) and isinstance(products, list)):
            raise TypeError("Недопустимое значение: неверный тип данных")
        self.name = name  # имя категории
        self.description = description  # описание категории
        self.__products = products  # продукты в категории
        Category.category_count += 1  # общее количество категорий
        Category.product_count += len(products)  # общее количество видов товаров

    def __str__(self) -> str:
        quantity_of_products = sum([prd.quantity for prd in self.__products])
        return f"{self.name}, количество продуктов: {quantity_of_products} шт."

    @property
    def products(self) -> list:
        return self.__products

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
            raise TypeError("Недопустимое значение: неверный тип данных")

    def middle_price(self) -> float:
        """
        Подсчет среднего ценника всех товаров в категории
        :return: средняя цена товаров в категории
        """
        try:
            price = sum([product.price * product.quantity for product in self.__products])
            quantity = sum([product.quantity for product in self.__products])
            return float(price / quantity)
        except ZeroDivisionError:
            return 0

    def output_product_list(self) -> str:
        """
        Метод вывода списка продуктов
        :return: список продуктов в виде текста
        """
        text = [str(prd) for prd in self.__products]
        return "\n".join(text)
