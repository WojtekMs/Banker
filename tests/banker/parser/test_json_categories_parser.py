import pytest

from banker.data.category import Category, PaymentType
from banker.parser.json_categories_parser import JsonCategoriesParser, CategoriesVersionMissing, \
    CategoriesVersionInvalid, CategoriesVersionUnsupported, CategoryNameDuplicate
from tests.banker.parser.test_data.json_categories import MISSING_VERSION_JSON_CATEGORIES_LITERAL, \
    INCOMPATIBLE_VERSION_JSON_CATEGORIES_LITERAL, INVALID_VERSION_JSON_CATEGORIES_LITERAL_1, \
    INVALID_VERSION_JSON_CATEGORIES_LITERAL_2, INVALID_VERSION_JSON_CATEGORIES_LITERAL_3, \
    ONE_CATEGORY_JSON_CATEGORIES_LITERAL, MANY_CATEGORIES_JSON_CATEGORIES_LITERAL, \
    SOME_INVALID_CATEGORIES_JSON_CATEGORIES_LITERAL, INVALID_PAYMENT_TYPE_JSON_CATEGORIES_LITERAL, \
    DUPLICATE_NAMES_JSON_CATEGORIES_LITERAL


@pytest.fixture
def json_categories_parser_sut():
    return JsonCategoriesParser()


def test_given_json_file_without_version_when_parse_categories_then_raise_error(json_categories_parser_sut):
    with pytest.raises(CategoriesVersionMissing):
        json_categories_parser_sut.parse_categories(MISSING_VERSION_JSON_CATEGORIES_LITERAL)


@pytest.mark.parametrize('invalid_version',
                         [INVALID_VERSION_JSON_CATEGORIES_LITERAL_1, INVALID_VERSION_JSON_CATEGORIES_LITERAL_2,
                          INVALID_VERSION_JSON_CATEGORIES_LITERAL_3])
def test_given_json_file_with_invalid_version_when_parse_categories_then_raise_error(json_categories_parser_sut,
                                                                                     invalid_version):
    with pytest.raises(CategoriesVersionInvalid):
        json_categories_parser_sut.parse_categories(invalid_version)


def test_given_json_file_with_incompatible_version_when_parse_categories_then_raise_error(json_categories_parser_sut):
    with pytest.raises(CategoriesVersionUnsupported):
        json_categories_parser_sut.parse_categories(INCOMPATIBLE_VERSION_JSON_CATEGORIES_LITERAL)


def test_given_json_file_with_duplicate_category_names_when_parse_categories_then_raise_error(
        json_categories_parser_sut):
    with pytest.raises(CategoryNameDuplicate):
        json_categories_parser_sut.parse_categories(DUPLICATE_NAMES_JSON_CATEGORIES_LITERAL)


def test_given_json_file_with_one_category_when_parse_categories_then_return_category(json_categories_parser_sut):
    expected_result = [Category(name="Kaufland", payment_type=PaymentType.Household, matching_regexes=["KAUFLAND PL"])]

    actual_result = json_categories_parser_sut.parse_categories(ONE_CATEGORY_JSON_CATEGORIES_LITERAL)

    assert actual_result == expected_result


def test_given_json_file_with_many_categories_when_parse_categories_then_return_categories(json_categories_parser_sut):
    expected_result = [
        Category(name="Kaufland", payment_type=PaymentType.Household, matching_regexes=["KAUFLAND PL"]),
        Category(name="Internet", payment_type=PaymentType.Recurring, matching_regexes=["(?i)vectra"]),
        Category(name="Shoes", payment_type=PaymentType.Occasional, matching_regexes=["shoes", "adidas"]),
        Category(name="Cafe", payment_type=PaymentType.Optional, matching_regexes=["Klar", "Starbucks"]),
        Category(name="Empty", payment_type=PaymentType.Optional, matching_regexes=[]),
    ]

    actual_result = json_categories_parser_sut.parse_categories(MANY_CATEGORIES_JSON_CATEGORIES_LITERAL)

    assert actual_result == expected_result


def test_given_json_file_with_some_invalid_categories_when_parse_categories_then_return_valid_categories(
        json_categories_parser_sut):
    expected_result = [
        Category(name="Kaufland", payment_type=PaymentType.Household, matching_regexes=["KAUFLAND PL"]),
    ]

    actual_result = json_categories_parser_sut.parse_categories(SOME_INVALID_CATEGORIES_JSON_CATEGORIES_LITERAL)

    assert actual_result == expected_result


def test_given_json_file_with_invalid_payment_type_when_parse_categories_then_skip(
        json_categories_parser_sut):
    expected_result = [
        Category(name="Kaufland", payment_type=PaymentType.Household, matching_regexes=["KAUFLAND PL"]),
    ]

    actual_result = json_categories_parser_sut.parse_categories(INVALID_PAYMENT_TYPE_JSON_CATEGORIES_LITERAL)

    assert actual_result == expected_result
