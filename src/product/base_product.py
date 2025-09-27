from abc import ABC, abstractmethod
from typing import Self, Union


class BaseProduct(ABC):
    @classmethod
    @abstractmethod
    def new_product(cls, product: dict) -> Union[None, Self]:
        """Создание продукта"""
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __add__(self, other: Self) -> float:
        pass
