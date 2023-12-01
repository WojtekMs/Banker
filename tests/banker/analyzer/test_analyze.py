from copy import deepcopy

import pytest

from moneyed import Money, PLN

from banker.data.category import Category, PaymentType
from banker.data.transaction import Transaction
from banker.analyzer.analyze import analyze_transactions, AnalyzeResult


def make_category_with_value(category: Category, value: Money) -> Category:
    category_copy = deepcopy(category)
    category_copy.value = value
    return category_copy


@pytest.mark.parametrize(
    'transactions, supported_categories, expected_result',
    [
        (
                [
                    Transaction(date="2023-01-01", value=Money(amount="-11.27", currency=PLN), description="New shoes",
                                type="Card")
                ],
                [
                    Category(name="Shoes", payment_type=PaymentType.Optional, matching_regexes=[r"(?i)shoes"])
                ],
                AnalyzeResult(unmatched_transactions=[], matched_categories=[
                    make_category_with_value(
                        Category(name="Shoes", payment_type=PaymentType.Optional, matching_regexes=[r"(?i)shoes"]),
                        Money(amount="-11.27", currency=PLN))
                ])
        ),
        (
                [
                    Transaction(date="2023-01-01", value=Money(amount="-13.30", currency=PLN),
                                description="Amazing trekking shoes", type="Card"),
                    Transaction(date="2023-01-02", value=Money(amount="-16.70", currency=PLN),
                                description="Casual shoes", type="Card"),
                    Transaction(date="2023-01-03", value=Money(amount="-20.00", currency=PLN),
                                description="Dancing shoes", type="Card")
                ],
                [
                    Category(name="Shoes", payment_type=PaymentType.Optional, matching_regexes=[r"(?i)shoes"])
                ],
                AnalyzeResult(unmatched_transactions=[], matched_categories=[
                    make_category_with_value(
                        Category(name="Shoes", payment_type=PaymentType.Optional, matching_regexes=[r"(?i)shoes"]),
                        Money(amount="-50.00", currency=PLN))
                ])
        ),
        (
                [
                    Transaction(date="2023-01-01", value=Money(amount="-15.00", currency=PLN),
                                description="Amazing trekking shoes", type="Card"),
                    Transaction(date="2023-01-02", value=Money(amount="-33.00", currency=PLN),
                                description="Cheap shirts", type="Card"),
                    Transaction(date="2023-01-03", value=Money(amount="-50.00", currency=PLN),
                                description="Expensive sweets", type="Card")
                ],
                [
                    Category(name="Shoes", payment_type=PaymentType.Optional, matching_regexes=[r"(?i)shoes"]),
                    Category(name="Sweets", payment_type=PaymentType.Optional, matching_regexes=[r"(?i)sweets"]),
                    Category(name="Shirts", payment_type=PaymentType.Optional, matching_regexes=[r"(?i)shirts"])

                ],
                AnalyzeResult(unmatched_transactions=[], matched_categories=[
                    make_category_with_value(
                        Category(name="Shoes", payment_type=PaymentType.Optional, matching_regexes=[r"(?i)shoes"]),
                        Money(amount="-15.00", currency=PLN)),
                    make_category_with_value(
                        Category(name="Shirts", payment_type=PaymentType.Optional, matching_regexes=[r"(?i)shirts"]),
                        Money(amount="-33.00", currency=PLN)),
                    make_category_with_value(
                        Category(name="Sweets", payment_type=PaymentType.Optional, matching_regexes=[r"(?i)sweets"]),
                        Money(amount="-50.00", currency=PLN))
                ])
        ),
        (
                [
                    Transaction(date="2023-01-01", value=Money(amount="-11.27", currency=PLN), description="New shoes",
                                type="Card"),
                    Transaction(date="2023-01-02", value=Money(amount="-500.00", currency=PLN), description="New game",
                                type="Card")
                ],
                [
                    Category(name="Shoes", payment_type=PaymentType.Optional, matching_regexes=[r"(?i)shoes"])
                ],

                AnalyzeResult(
                    unmatched_transactions=[
                        Transaction(date="2023-01-02", value=Money(amount="-500.00", currency=PLN),
                                    description="New game", type="Card")],
                    matched_categories=[
                        make_category_with_value(
                            Category(name="Shoes", payment_type=PaymentType.Optional, matching_regexes=[r"(?i)shoes"]),
                            Money(amount="-11.27", currency=PLN))
                    ])
        ),
        (
                [
                    Transaction(date="2023-01-01", value=Money(amount="-11.27", currency=PLN), description="New shoes",
                                type="Card"),
                ],
                [
                    Category(name="Shoes", payment_type=PaymentType.Optional, matching_regexes=[r"(?i)shoes"]),
                    Category(name="New stuff", payment_type=PaymentType.Optional, matching_regexes=[r"(?i)new"])
                ],

                AnalyzeResult(
                    unmatched_transactions=[Transaction(date="2023-01-01", value=Money(amount="-11.27", currency=PLN),
                                                        description="New shoes", type="Card")],
                    matched_categories=[])
        ),
        (
                [
                    Transaction(date="2023-01-01", value=Money(amount="-11.27", currency=PLN), description="New shoes",
                                type="Card"),
                ],
                [
                    Category(name="Shoes", payment_type=PaymentType.Optional, matching_regexes=[r"(?i)shoes"]),
                    Category(name="Weirdo", payment_type=PaymentType.Optional, matching_regexes=[r"what?"])
                ],

                AnalyzeResult(
                    unmatched_transactions=[],
                    matched_categories=[
                        make_category_with_value(
                            Category(name="Shoes", payment_type=PaymentType.Optional, matching_regexes=[r"(?i)shoes"]),
                            Money(amount="-11.27", currency=PLN))
                    ])
        ),
        (
                [
                    Transaction(date="2023-01-01", value=Money(amount="-11.27", currency=PLN), description="New shoes",
                                type="Card"),
                ],
                [
                    Category(name="Weirdo", payment_type=PaymentType.Optional, matching_regexes=[r"what?"])
                ],

                AnalyzeResult(
                    unmatched_transactions=[Transaction(date="2023-01-01", value=Money(amount="-11.27", currency=PLN),
                                                        description="New shoes", type="Card")],
                    matched_categories=[])
        ),
        (
                [],
                [
                    Category(name="Shoes", payment_type=PaymentType.Optional, matching_regexes=[r"(?i)shoes"]),
                ],

                AnalyzeResult(
                    unmatched_transactions=[],
                    matched_categories=[])
        ),
        (
                [
                    Transaction(date="2023-01-01", value=Money(amount="-11.27", currency=PLN), description="New shoes",
                                type="Card"),
                    Transaction(date="2023-01-02", value=Money(amount="-500.00", currency=PLN), description="New game",
                                type="Card")
                ],
                [],

                AnalyzeResult(
                    unmatched_transactions=[Transaction(date="2023-01-01", value=Money(amount="-11.27", currency=PLN),
                                                        description="New shoes", type="Card"),
                                            Transaction(date="2023-01-02", value=Money(amount="-500.00", currency=PLN),
                                                        description="New game", type="Card")],
                    matched_categories=[])
        ),
        (
                [],
                [],

                AnalyzeResult(
                    unmatched_transactions=[],
                    matched_categories=[])
        ),
    ],
    ids=["given matching transaction to one category then return matched category with increased value",
         "given many matching transactions to one category then return matched category with increased value",
         "given many transactions and many categories then return all matched categories with increased values",
         "given transaction that does not match then return unmatched transaction",
         "given matching transaction to many categories then return unmatched transaction",
         "given category that was not matched then exclude it from matched categories",
         "given one transaction that does not match then return unmatched transaction and no categories",
         "given no transactions then return empty list of both transactions and categories",
         "given transactions and empty list of categories then return all transactions as unmatched",
         "given empty transactions and empty categories then return empty lists"]
)
def test_given_transactions_and_supported_categories_when_analyze_then_return_result(
        transactions, supported_categories, expected_result
):
    actual_result = analyze_transactions(transactions, supported_categories)

    assert actual_result == expected_result
