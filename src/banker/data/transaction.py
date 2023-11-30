from dataclasses import dataclass

from banker.data.category import Category
from moneyed import Money, PLN


@dataclass(frozen=True)
class Transaction:
    date: str
    value: Money
    description: str

    def __post_init__(self):
        if self.value.currency != PLN:
            raise ValueError("The only accepted transaction currency is PLN")

    def count_matching(self, categories: list[Category]) -> int:
        # TODO: implement
        return 0
