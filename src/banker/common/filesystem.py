from banker.data.category import Category
from banker.data.transaction import Transaction
from banker.parser.interfaces.categories_parser import ICategoriesParser
from banker.parser.interfaces.transactions_parser import ITransactionsParser


def get_parsed_categories(categories_parser: ICategoriesParser, categories_filepath: str) -> list[Category]:
    with open(categories_filepath, "r") as file:
        return categories_parser.parse_categories(file.read())


def get_parsed_transactions(transactions_parser: ITransactionsParser, transactions_filepath: str) -> list[Transaction]:
    with open(transactions_filepath, "r") as transactions_file:
        return transactions_parser.parse_transactions(transactions_file.read())


def save_to_file(filepath: str, content: str):
    with open(filepath, "w") as file:
        file.write(content)
