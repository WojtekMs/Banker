import datetime
from dataclasses import dataclass

from banker.data.category import Category
from moneyed import Money, PLN


@dataclass(frozen=True)
class Transaction:
    date: datetime.date
    value: Money
    type: str
    description: str

    def __post_init__(self):
        if self.value.currency != PLN:
            raise ValueError("The only accepted transaction currency is PLN")

    def find_matching(self, categories: list[Category]) -> list[Category]:
        result = []
        for category in categories:
            if any([True for pattern in category.get_matching_regexes() if
                    pattern.search(self.description) is not None]):
                result.append(category)
        return result
