from abc import ABC, abstractmethod
from banker.data.transaction import Transaction


class ITransactionsFormatter(ABC):
    @abstractmethod
    def format_transactions(self, transactions: list[Transaction]) -> str:
        raise NotImplementedError("Method not implemented in subclass")
