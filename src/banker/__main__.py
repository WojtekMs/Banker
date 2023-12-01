from banker.analyzer.analyze import analyze_transactions
from banker.data.category import Category, PaymentType
import argparse

from banker.parser.html_transactions_parser import HtmlTransactionsParser


def main():
    supported_categories = [
        Category(name="Kaufland", payment_type=PaymentType.Household, matching_regexes=[r"KAUFLAND PL"])]
    transactions_parser = HtmlTransactionsParser()

    parser = argparse.ArgumentParser()
    parser.add_argument("html_file")
    args = parser.parse_args()

    with open(args.html_file, "rb") as file:
        all_transactions = transactions_parser.parse_transactions(file.read().decode('utf-8'))
        analyze_result = analyze_transactions(all_transactions, supported_categories)
        print(analyze_result)
    #     TODO: format output
