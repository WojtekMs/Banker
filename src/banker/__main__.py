from banker.analyzer.analyze import analyze_transactions, deduce_month_year
from banker.data.category import Category, PaymentType
import argparse

from banker.formatter.month_year_formatter import format_month_year
from banker.parser.html_transactions_parser import HtmlTransactionsParser
from banker.formatter.html_transactions_formatter import HtmlTransactionsFormatter
from banker.writer.excel_categories_writer import ExcelCategoriesWriter


def main():
    supported_categories = [
        Category(name="Kaufland", payment_type=PaymentType.Household, matching_regexes=[r"KAUFLAND PL"])]
    transactions_parser = HtmlTransactionsParser()
    transactions_formatter = HtmlTransactionsFormatter()
    categories_writer = ExcelCategoriesWriter()

    parser = argparse.ArgumentParser()
    parser.add_argument("html_file")
    args = parser.parse_args()

    with open(args.html_file, "rb") as input_file:
        all_transactions = transactions_parser.parse_transactions(input_file.read().decode('utf-8'))
        analyze_result = analyze_transactions(all_transactions, supported_categories)
        formatted_transactions = transactions_formatter.format_transactions(analyze_result.unmatched_transactions)
        with open("unmatched_transactions.html", "w") as transactions_file:
            transactions_file.write(formatted_transactions)
        month_year = deduce_month_year(all_transactions)
        categories_writer.write_categories(analyze_result.matched_categories, "autogen_budget.xlsx",
                                           format_month_year(month_year))
