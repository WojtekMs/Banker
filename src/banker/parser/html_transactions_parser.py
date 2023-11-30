import io
import logging
import pandas

from moneyed import Money, PLN

from banker.data.transaction import Transaction
from banker.parser.interfaces.transactions_parser import ITransactionsParser


class HtmlTransactionsParser(ITransactionsParser):
    logger = logging.getLogger("HtmlTransactionsParser")

    def __parse_transactions_table(self, content: str) -> pandas.DataFrame | None:
        try:
            tables = pandas.read_html(io.StringIO(content), attrs={'id': 'lista_transakcji'})
            return tables[0]
        except ValueError:
            self.logger.warning(f"Invalid HTML literal, transactions table is missing")
            return None

    def parse_transactions(self, content: str) -> list[Transaction]:
        result = []
        transactions_table = self.__parse_transactions_table(content)
        if transactions_table is not None:
            for row_id, transaction in transactions_table.iterrows():
                if transaction.hasnans is True:
                    self.logger.warning(f"HTML Table data is probably corrupted - transaction {row_id} has NaN values")
                    continue
                date = transaction.get("Data operacji")
                if date is None or not isinstance(date, str):
                    self.logger.warning(f"Date not found in transaction {row_id}")
                    continue
                description = transaction.get("Opis")
                if description is None or not isinstance(description, str):
                    self.logger.warning(f"Description not found in transaction {row_id}")
                    continue
                value = transaction.get("Kwota")
                if value is None:
                    self.logger.warning(f"Value not found in transaction {row_id}")
                    continue
                result.append(
                    Transaction(date=date, description=description, value=Money(amount=str(value), currency=PLN)))
        return result
