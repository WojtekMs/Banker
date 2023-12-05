import datetime
from copy import deepcopy

import pytest

from moneyed import Money, PLN

from banker.data.category import Category, PaymentType
from banker.analyzer.analyze import analyze_transactions, AnalyzeResult, deduce_month_year, MonthYear

from tests.banker.conftest import make_transaction


def make_category_with_value(category: Category, value: Money) -> Category:
    category_copy = deepcopy(category)
    category_copy.value = value
    return category_copy


@pytest.mark.parametrize(
    'transactions, supported_categories, expected_result',
    [
        (
                [
                    make_transaction(value="-11.27", description="New shoes")
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
                    make_transaction(value="-13.30", description="Amazing trekking shoes"),
                    make_transaction(value="-16.70", description="Casual shoes"),
                    make_transaction(value="-20.00", description="Dancing shoes")
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
                    make_transaction(value="-15.00", description="Amazing trekking shoes"),
                    make_transaction(value="-33.00", description="Cheap shirts"),
                    make_transaction(value="-50.00", description="Expensive sweets"),
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
                    make_transaction(value="-11.27", description="New shoes"),
                    make_transaction(value="-500.00", description="New game"),
                ],
                [
                    Category(name="Shoes", payment_type=PaymentType.Optional, matching_regexes=[r"(?i)shoes"])
                ],

                AnalyzeResult(
                    unmatched_transactions=[
                        make_transaction(value="-500.00", description="New game")],
                    matched_categories=[
                        make_category_with_value(
                            Category(name="Shoes", payment_type=PaymentType.Optional, matching_regexes=[r"(?i)shoes"]),
                            Money(amount="-11.27", currency=PLN))
                    ])
        ),
        (
                [
                    make_transaction(value="-11.27", description="New shoes"),
                ],
                [
                    Category(name="Shoes", payment_type=PaymentType.Optional, matching_regexes=[r"(?i)shoes"]),
                    Category(name="New stuff", payment_type=PaymentType.Optional, matching_regexes=[r"(?i)new"])
                ],

                AnalyzeResult(
                    unmatched_transactions=[
                        make_transaction(value="-11.27", description="New shoes")],
                    matched_categories=[])
        ),
        (
                [
                    make_transaction(value="-11.27", description="New shoes"),
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
                    make_transaction(value="-11.27", description="New shoes"),
                ],
                [
                    Category(name="Weirdo", payment_type=PaymentType.Optional, matching_regexes=[r"what?"])
                ],

                AnalyzeResult(
                    unmatched_transactions=[make_transaction(value="-11.27", description="New shoes")],
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
                    make_transaction(value="-11.27", description="New shoes"),
                    make_transaction(value="-500.00", description="New game"),
                ],
                [],

                AnalyzeResult(
                    unmatched_transactions=[
                        make_transaction(value="-11.27", description="New shoes"),
                        make_transaction(value="-500.00", description="New game"),
                    ],
                    matched_categories=[])
        ),
        (
                [],
                [],

                AnalyzeResult(
                    unmatched_transactions=[],
                    matched_categories=[])
        ),
        (
                [
                    make_transaction(value="-11.27", description="New shoes"),
                    make_transaction(value="500.00", description="Refund one"),
                    make_transaction(value="25.00", description="Refund two"),
                ],
                [
                    Category(name="Shoes", payment_type=PaymentType.Optional, matching_regexes=[r"(?i)shoes"]),
                    Category(name="Refund one", payment_type=PaymentType.Optional, matching_regexes=["Refund one"]),
                ],

                AnalyzeResult(
                    unmatched_transactions=[],
                    matched_categories=[make_category_with_value(
                        Category(name="Shoes", payment_type=PaymentType.Optional, matching_regexes=[r"(?i)shoes"]),
                        Money(amount="-11.27", currency=PLN))])
        )
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
         "given empty transactions and empty categories then return empty lists",
         "given transaction with positive value then ignore it"]
)
def test_given_transactions_and_supported_categories_when_analyze_then_return_result(
        transactions, supported_categories, expected_result
):
    actual_result = analyze_transactions(transactions, supported_categories)

    assert actual_result == expected_result


def test_given_chronologically_sorted_transactions_when_deduce_month_year_then_return_month_year():
    transactions = [make_transaction(date=datetime.date(year=2023, month=10, day=10)),
                    make_transaction(date=datetime.date(year=2023, month=11, day=1)),
                    make_transaction(date=datetime.date(year=2023, month=11, day=2)),
                    make_transaction(date=datetime.date(year=2023, month=11, day=3)),
                    make_transaction(date=datetime.date(year=2023, month=11, day=4)),
                    ]
    expected_result = MonthYear(year=2023, month=11)

    actual_result = deduce_month_year(transactions)

    assert actual_result == expected_result


def test_given_not_chronologically_sorted_transactions_when_deduce_month_year_then_return_month_year():
    transactions = [make_transaction(date=datetime.date(year=2023, month=10, day=10)),
                    make_transaction(date=datetime.date(year=2023, month=11, day=1)),
                    make_transaction(date=datetime.date(year=2023, month=11, day=2)),
                    make_transaction(date=datetime.date(year=2023, month=11, day=3)),
                    make_transaction(date=datetime.date(year=2023, month=10, day=15)),
                    ]
    expected_result = MonthYear(year=2023, month=11)

    actual_result = deduce_month_year(transactions)

    assert actual_result == expected_result
