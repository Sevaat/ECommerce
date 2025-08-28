
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

product = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

#### Класс категории

products = [
        Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
        Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
        Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
    ]  
category = Category("Name", "Description", products)