import datetime
import io
import logging
import pandas

from moneyed import Money, PLN

from banker.data.transaction import Transaction
from banker.parser.interfaces.transactions_parser import ITransactionsParser
from banker.common.naming import TRANSACTION_COL_NAME_VALUE, TRANSACTION_COL_NAME_DATE, TRANSACTION_COL_NAME_TYPE, \
    TRANSACTION_COL_NAME_DESCRIPTION


class RawDateInvalidFormat(Exception):
    def __init__(self, raw_date: str):
        self._raw_date = raw_date

    def __str__(self):
        return f"Raw date invalid format, expected year-month-day, e.g: 2023-11-01. Actual: {self._raw_date}"


class HtmlTransactionsParser(ITransactionsParser):
    logger = logging.getLogger("HtmlTransactionsParser")

    def __parse_transactions_table(self, content: str) -> pandas.DataFrame | None:
        try:
            tables = pandas.read_html(io.StringIO(content), attrs={'id': 'lista_transakcji'})
            return tables[0]
        except ValueError:
            self.logger.warning("Invalid HTML literal, transactions table is missing")
            return None

    def __parse_date(self, raw_date: str) -> datetime.date:
        raw_date_split = raw_date.split("-")
        if len(raw_date_split) != 3:
            raise RawDateInvalidFormat(raw_date)
        return datetime.date(year=int(raw_date_split[0]), month=int(raw_date_split[1]), day=int(raw_date_split[2]))

    def parse_transactions(self, content: str) -> list[Transaction]:
        result = []
        transactions_table = self.__parse_transactions_table(content)
        if transactions_table is not None:
            for row_id, transaction in transactions_table.iterrows():
                if transaction.hasnans is True:
                    self.logger.warning(f"HTML Table data is probably corrupted - transaction {row_id} has NaN values")
                    continue
                date = transaction.get(TRANSACTION_COL_NAME_DATE)
                if date is None or not isinstance(date, str):
                    self.logger.warning(f"Date not found in transaction {row_id}")
                    continue
                date = self.__parse_date(raw_date=date)
                description = transaction.get(TRANSACTION_COL_NAME_DESCRIPTION)
                if description is None or not isinstance(description, str):
                    self.logger.warning(f"Description not found in transaction {row_id}")
                    continue
                value = transaction.get(TRANSACTION_COL_NAME_VALUE)
                if value is None:
                    self.logger.warning(f"Value not found in transaction {row_id}")
                    continue
                transaction_type = transaction.get(TRANSACTION_COL_NAME_TYPE)
                if transaction_type is None:
                    self.logger.warning(f"Transaction type not found in transaction {row_id}")
                    continue
                result.append(
                    Transaction(date=date, description=description, value=Money(amount=str(value), currency=PLN),
                                type=transaction_type))
        return result
