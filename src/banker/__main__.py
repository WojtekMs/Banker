import argparse
import os.path

from importlib_resources import files

from banker.analyzer.analyze import analyze_transactions, deduce_month_year
from banker.data.category import Category

from banker.data.transaction import Transaction
from banker.formatter.month_year_formatter import format_month_year
from banker.parser.html_transactions_parser import HtmlTransactionsParser
from banker.formatter.html_transactions_formatter import HtmlTransactionsFormatter
from banker.parser.interfaces.categories_parser import ICategoriesParser
from banker.parser.interfaces.transactions_parser import ITransactionsParser
from banker.parser.json_categories_parser import JsonCategoriesParser
from banker.writer.excel_categories_writer import ExcelCategoriesWriter


def get_supported_categories(categories_parser: ICategoriesParser, categories_filepath: str) -> list[Category]:
    with open(categories_filepath, "r") as file:
        return categories_parser.parse_categories(file.read())


def get_transactions(transactions_parser: ITransactionsParser, transactions_filepath: str) -> list[Transaction]:
    with open(transactions_filepath, "r") as transactions_file:
        return transactions_parser.parse_transactions(transactions_file.read())


def save_to_file(filepath: str, content: str):
    with open(filepath, "w") as file:
        file.write(content)


def main():
    transactions_parser = HtmlTransactionsParser()
    categories_parser = JsonCategoriesParser()
    transactions_formatter = HtmlTransactionsFormatter()
    categories_writer = ExcelCategoriesWriter()

    parser = argparse.ArgumentParser()
    parser.add_argument("html_file")
    parser.add_argument("--categories_file", default=files('banker.resources').joinpath('categories.json'))
    parser.add_argument("--output_directory", default=files('banker.resources').joinpath('output'))
    args = parser.parse_args()

    os.makedirs(args.output_directory, exist_ok=True)
    output_unmatched_transactions_filepath = os.path.join(args.output_directory, "unmatched_transactions.html")
    output_matched_categories_filepath = os.path.join(args.output_directory, "autogen_budget.xlsx")

    all_transactions = get_transactions(transactions_parser, args.html_file)
    month_year = deduce_month_year(all_transactions)
    supported_categories = get_supported_categories(categories_parser, args.categories_file)
    analyze_result = analyze_transactions(all_transactions, supported_categories)
    formatted_transactions = transactions_formatter.format_transactions(analyze_result.unmatched_transactions)

    save_to_file(output_unmatched_transactions_filepath, formatted_transactions)
    categories_writer.write_categories(analyze_result.matched_categories, output_matched_categories_filepath,
                                       format_month_year(month_year))
