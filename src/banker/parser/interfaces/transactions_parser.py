from abc import ABC, abstractmethod
from banker.data.transaction import Transaction

class ITransactionsParser(ABC):
    @abstractmethod
    def parse_transactions(self, content: str) -> list[Transaction]:
        raise NotImplementedError("Method not implemented in subclass")