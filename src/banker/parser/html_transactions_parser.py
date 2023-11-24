from banker.data.transaction import Transaction
from banker.parser.interfaces.transactions_parser import ITransactionsParser

class HtmlTransactionsParser(ITransactionsParser):
    def parse_transactions(self, content: str) -> list[Transaction]:
        # TODO: parse HTML
        return []