from dataclasses import dataclass

from banker.data.category import Category
from banker.data.transaction import Transaction
from logging import getLogger

analyze_logger = getLogger("Analyze")


@dataclass(frozen=True)
class AnalyzeResult:
    unmatched_transactions: list[Transaction]
    matched_categories: list[Category]


def analyze_transactions(transactions: list[Transaction], supported_categories: list[Category]) -> AnalyzeResult:
    unmatched_transactions = []
    matched_categories = {}
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
