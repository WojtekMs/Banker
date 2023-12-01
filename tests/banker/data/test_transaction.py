import pytest

from moneyed import Money, PLN

from banker.data.category import Category, PaymentType
from banker.data.transaction import Transaction


@pytest.fixture
def transaction_sut():
    return Transaction(date="2023-11-01", value=Money(amount='-37.35', currency=PLN),
                       type="Card",
                       description="000015792 05272423303314705681107 "
                                   "Lokalizacja : "
                                   "Adres : KAUFLAND PL 6663 "
                                   "Miasto : Gliwice "
                                   "Kraj : POLSKA "
                                   "Data i czas operacji : 2023-10-30 "
                                   "Oryginalna kwota operacji : 37.35 "
                                   "Numer karty : 516931******3943")


@pytest.mark.parametrize(
    'categories, expected_result',
    [
        (
                [
                    Category(name="Kaufland", payment_type=PaymentType.Household, matching_regexes=[r"KAUFLAND PL"])
                ],
                [
                    Category(name="Kaufland", payment_type=PaymentType.Household, matching_regexes=[r"KAUFLAND PL"])
                ]
        ),
        (
                [
                    Category(name="Kaufland", payment_type=PaymentType.Household, matching_regexes=[r"KAUFLAND PL"]),
                    Category(name="Gliwice", payment_type=PaymentType.Optional, matching_regexes=[r"(?i)gliwice"]),
                    Category(name="Polska", payment_type=PaymentType.Occasional, matching_regexes=[r"P.L.KA"])
                ],
                [
                    Category(name="Kaufland", payment_type=PaymentType.Household, matching_regexes=[r"KAUFLAND PL"]),
                    Category(name="Gliwice", payment_type=PaymentType.Optional, matching_regexes=[r"(?i)gliwice"]),
                    Category(name="Polska", payment_type=PaymentType.Occasional, matching_regexes=[r"P.L.KA"])
                ],
        ),
        (
                [
                    Category(name="Kaufland", payment_type=PaymentType.Household, matching_regexes=[r"KAUFLAND PL"]),
                    Category(name="Bad category", payment_type=PaymentType.Optional, matching_regexes=[r"donald duck"]),
                    Category(name="Polska", payment_type=PaymentType.Occasional, matching_regexes=[r"P.L.KA"])
                ],
                [
                    Category(name="Kaufland", payment_type=PaymentType.Household, matching_regexes=[r"KAUFLAND PL"]),
                    Category(name="Polska", payment_type=PaymentType.Occasional, matching_regexes=[r"P.L.KA"])
                ],
        ),
        (
                [
                    Category(name="Bad category 0", payment_type=PaymentType.Household, matching_regexes=[r"rick"]),
                    Category(name="Bad category 1", payment_type=PaymentType.Optional, matching_regexes=[r"jack"]),
                    Category(name="Bad category 2", payment_type=PaymentType.Occasional, matching_regexes=[r"sack"])
                ],
                []
        ),
        (
                [],
                []
        ),
        (
                [
                    Category(name="Kaufland", payment_type=PaymentType.Household, matching_regexes=["KAUF"]),
                    Category(name="Gliwice", payment_type=PaymentType.Optional, matching_regexes=["(?i)gliwice"]),
                    Category(name="Polska", payment_type=PaymentType.Occasional, matching_regexes=["P.L.KA"])
                ],
                [
                    Category(name="Kaufland", payment_type=PaymentType.Household, matching_regexes=["KAUF"]),
                    Category(name="Gliwice", payment_type=PaymentType.Optional, matching_regexes=["(?i)gliwice"]),
                    Category(name="Polska", payment_type=PaymentType.Occasional, matching_regexes=["P.L.KA"])
                ],
        ),
        (
                [
                    Category(name="Kaufland", payment_type=PaymentType.Household,
                             matching_regexes=["KAUF", "KAUFLAND PL", "KAU.LAND"]),
                ],
                [
                    Category(name="Kaufland", payment_type=PaymentType.Household,
                             matching_regexes=["KAUF", "KAUFLAND PL", "KAU.LAND"]),
                ],
        ),
        (
                [
                    Category(name="Kaufland", payment_type=PaymentType.Household,
                             matching_regexes=["KAUF", "KAUFLAND PL", "KAU.LAND"]),
                    Category(name="Polska", payment_type=PaymentType.Household,
                             matching_regexes=["POL", "POLSKA", "PO.S"]),
                ],
                [
                    Category(name="Kaufland", payment_type=PaymentType.Household,
                             matching_regexes=["KAUF", "KAUFLAND PL", "KAU.LAND"]),
                    Category(name="Polska", payment_type=PaymentType.Household,
                             matching_regexes=["POL", "POLSKA", "PO.S"]),
                ],
        ),
        (
                [
                    Category(name="Empty patterns", payment_type=PaymentType.Household, matching_regexes=[]),
                ],
                []
        ),
        (
                [
                    Category(name="Longer pattern", payment_type=PaymentType.Household,
                             matching_regexes=["2023-10-30 Oryginalna kwota operacji"]),
                ],
                [
                    Category(name="Longer pattern", payment_type=PaymentType.Household,
                             matching_regexes=["2023-10-30 Oryginalna kwota operacji"]),
                ],
        ),
    ],
    ids=["one category is matching",
         "all categories are matching",
         "some categories are matching",
         "none categories are matching",
         "empty categories list",
         "regexes in regular string",
         "multiple matching regexes in one category",
         "multiple matching regexes in two categories",
         "one category with empty matching regexes list",
         "one category with longer regex"]
)
def test_given_categories_when_find_matching_then_return_list_of_matched_categories(transaction_sut, categories,
                                                                                    expected_result):
    actual_result = transaction_sut.find_matching(categories)

    assert actual_result == expected_result
