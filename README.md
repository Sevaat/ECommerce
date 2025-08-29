
# ECommerce

Обучающий проект Skypro: ядро для интернет-магазина.


## Благодарности

Благодарность ОАНО ДПО "СКАЕНГ".
## Авторы

tkachenko <sevaatmail@mail.com>


## Установка

Работа программы производится при запуске файла main.py, хранящегося в корне проекта.
    
## Выполнение тестов

В проекте использована библиотека pytest. Запуск тестов производится командой в терминале pytest.


## Использование/Примеры

#### Класс продукта

product = Product(name="Name", description="Description", price=1.0, quantity=1)  
product = Product.new_product({"name": "Name", "description": "Description", "price": 1.0, "quantity": 1})

#### Класс категории

product1 = Product("Name1", "Description1", 1.0, 1)  
product2 = Product("Name2", "Description2", 2.0, 2)  
product3 = Product("Name3", "Description3", 3.0, 3)  
products = [product1, product2]
category = Category("Name", "Description", products)  
category.add_product(product3)  
category.output_product_list()