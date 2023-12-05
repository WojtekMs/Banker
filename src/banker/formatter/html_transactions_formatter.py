import pandas

from banker.data.transaction import Transaction
from banker.formatter.interfaces.transactions_formatter import ITransactionsFormatter
from banker.common.naming import TRANSACTION_COL_NAME_DATE, TRANSACTION_COL_NAME_VALUE, \
    TRANSACTION_COL_NAME_DESCRIPTION, TRANSACTION_COL_NAME_TYPE


class HtmlTransactionsFormatter(ITransactionsFormatter):
    def format_transactions(self, transactions: list[Transaction]) -> str:
        data = {TRANSACTION_COL_NAME_DATE: [], TRANSACTION_COL_NAME_TYPE: [], TRANSACTION_COL_NAME_DESCRIPTION: [],
                TRANSACTION_COL_NAME_VALUE: []}
        for transaction in transactions:
            data[TRANSACTION_COL_NAME_DATE].append(transaction.date)
            data[TRANSACTION_COL_NAME_TYPE].append(transaction.type)
            data[TRANSACTION_COL_NAME_DESCRIPTION].append(transaction.description)
            data[TRANSACTION_COL_NAME_VALUE].append(str(transaction.value))
        df = pandas.DataFrame(data=data)
        return df.to_html()
