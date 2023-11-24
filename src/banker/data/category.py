from dataclasses import dataclass
from enum import Enum, auto


class PaymentType(Enum):
    household = auto()
    recurring = auto()
    optional = auto()
    occasional = auto()


@dataclass
class Category:
    _name: str
    _payment_type: PaymentType
    _matching_regexes: str
    _value: float

    def add(self, transaction):
        pass
