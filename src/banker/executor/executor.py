import os

from banker.analyzer.analyze import deduce_month_year, analyze_transactions
from banker.common.filesystem import get_parsed_categories, get_parsed_transactions, save_to_file
from banker.formatter.interfaces.transactions_formatter import ITransactionsFormatter
from banker.formatter.month_year_formatter import format_month_year
from banker.parser.interfaces.categories_parser import ICategoriesParser
from banker.parser.interfaces.transactions_parser import ITransactionsParser
from banker.writer.interfaces.categories_writer import ICategoriesWriter


class Executor:
    def __init__(self, transactions_parser: ITransactionsParser, categories_parser: ICategoriesParser,
                 transactions_formatter: ITransactionsFormatter, categories_writer: ICategoriesWriter):
        self.__transactions_parser = transactions_parser
        self.__categories_parser = categories_parser
        self.__transactions_formatter = transactions_formatter
        self.__categories_writer = categories_writer

    def execute(self, transactions_filepath: str, categories_filepath: str, output_directory: str):
        os.makedirs(output_directory, exist_ok=True)
        output_unmatched_transactions_filepath = os.path.join(output_directory, "unmatched_transactions.html")
        output_matched_categories_filepath = os.path.join(output_directory, "autogen_budget.xlsx")

        all_transactions = get_parsed_transactions(self.__transactions_parser, transactions_filepath)
        month_year = deduce_month_year(all_transactions)
        supported_categories = get_parsed_categories(self.__categories_parser, categories_filepath)
        analyze_result = analyze_transactions(all_transactions, supported_categories)
        formatted_transactions = self.__transactions_formatter.format_transactions(
            analyze_result.unmatched_transactions)

        save_to_file(output_unmatched_transactions_filepath, formatted_transactions)
        self.__categories_writer.write_categories(analyze_result.matched_categories, output_matched_categories_filepath,
                                                  format_month_year(month_year))
