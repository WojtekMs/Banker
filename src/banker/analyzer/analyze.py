import datetime
from dataclasses import dataclass

from moneyed import Money, PLN

from banker.data.category import Category
from banker.data.transaction import Transaction
from logging import getLogger

analyze_logger = getLogger("Analyze")


@dataclass(frozen=True)
class AnalyzeResult:
    unmatched_transactions: list[Transaction]
    matched_categories: list[Category]


@dataclass(frozen=True)
class MonthYear:
    month: int
    year: int


def deduce_month_year(transactions: list[Transaction]) -> MonthYear:
    year_count = {}
    month_count = {}
    for transaction in transactions:
        year_count.setdefault(transaction.date.year, 0)
        year_count[transaction.date.year] += 1
        month_count.setdefault(transaction.date.month, 0)
        month_count[transaction.date.month] += 1
    the_most_common_year = max(year_count, key=year_count.get)
    the_most_common_month = max(month_count, key=month_count.get)
    return MonthYear(year=the_most_common_year, month=the_most_common_month)


def analyze_transactions(transactions: list[Transaction], supported_categories: list[Category]) -> AnalyzeResult:
    unmatched_transactions = []
    matched_categories = {}
    transactions = [transaction for transaction in transactions if transaction.value < Money(amount='0', currency=PLN)]
    for transaction in transactions:
        matching_categories = transaction.find_matching(supported_categories)
        matching_categories_count = len(matching_categories)
        if matching_categories_count == 1:
            category_name = matching_categories[0].get_name()
            matched_category = matched_categories.setdefault(category_name, matching_categories[0])
            matched_category.value += transaction.value
        else:
            analyze_logger.info(f"Transaction: {transaction} matched to {matching_categories_count} categories")
            unmatched_transactions.append(transaction)
    return AnalyzeResult(unmatched_transactions=unmatched_transactions,
                         matched_categories=list(matched_categories.values()))
