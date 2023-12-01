from enum import Enum, auto
import re

from moneyed import Money, PLN


class PaymentType(Enum):
    Household = auto()
    Recurring = auto()
    Optional = auto()
    Occasional = auto()


class Category:
    def __init__(self, name: str, payment_type: PaymentType, matching_regexes: list[str]):
        self.__name = name
        self.__payment_type = payment_type
        self.__matching_regexes: list[re.Pattern] = [re.compile(pattern) for pattern in matching_regexes]
        self.value = Money(amount='0', currency=PLN)

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return False

    def __str__(self):
        return f"Category(name={self.__name}, payment_type={self.__payment_type}, " \
               f"matching_regexes={self.__matching_regexes}, value={self.value})"

    def __repr__(self):
        return self.__str__()

    def get_name(self) -> str:
        return self.__name

    def get_payment_type(self) -> PaymentType:
        return self.__payment_type

    def get_matching_regexes(self) -> list[re.Pattern]:
        return self.__matching_regexes
