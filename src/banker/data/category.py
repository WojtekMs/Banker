from enum import Enum, auto
import re

from moneyed import Money, PLN


class PaymentType(Enum):
    household = auto()
    recurring = auto()
    optional = auto()
    occasional = auto()


class Category:
    def __init__(self, name: str, payment_type: PaymentType, matching_regexes: list[str]):
        self.__name = name
        self.__payment_type = payment_type
        self.__matching_regexes: list[re.Pattern] = [re.compile(pattern) for pattern in matching_regexes]
        self.value = Money(amount='0', currency=PLN)

    def get_name(self) -> str:
        return self.__name

    def get_payment_type(self) -> PaymentType:
        return self.__payment_type

    def get_matching_regexes(self) -> list[re.Pattern]:
        return self.__matching_regexes
