import pytest

from banker.parser.html_transactions_parser import HtmlTransactionsParser, RawDateInvalidFormat
from tests.banker.parser.test_data.html_transactions import HTML_TRANSACTIONS_LITERAL, ONE_HTML_TRANSACTION_LITERAL, \
    BROKEN_HTML_TRANSACTIONS_LITERAL, TABLE_HEADERS_MISSING_HTML_TRANSACTIONS_LITERAL, \
    TRANSACTIONS_TABLE_MISSING_HTML_TRANSACTIONS_LITERAL, \
    DATE_INVALID_FORMAT_HTML_TRANSACTION_LITERAL_1, DATE_INVALID_FORMAT_HTML_TRANSACTION_LITERAL_2


@pytest.fixture
def html_parser_sut():
    return HtmlTransactionsParser()


def test_given_one_html_transaction_literal_when_parse_transactions_then_return_list_of_transactions(transaction1,
                                                                                                     html_parser_sut):
    expected_transactions = [transaction1]

    actual_transactions = html_parser_sut.parse_transactions(ONE_HTML_TRANSACTION_LITERAL)

    assert actual_transactions == expected_transactions


def test_given_html_transactions_literal_when_parse_transactions_then_return_list_of_transactions(transaction1,
                                                                                                  transaction2,
                                                                                                  transaction3,
                                                                                                  transaction4,
                                                                                                  transaction5,
                                                                                                  html_parser_sut):
    expected_transactions = [transaction1, transaction2, transaction3, transaction4, transaction5]

    actual_transactions = html_parser_sut.parse_transactions(HTML_TRANSACTIONS_LITERAL)

    assert actual_transactions == expected_transactions


def test_given_broken_html_transactions_literal_when_parse_transactions_then_skip_broken_entries(transaction1,
                                                                                                 html_parser_sut):
    expected_transactions = [transaction1]

    actual_transactions = html_parser_sut.parse_transactions(BROKEN_HTML_TRANSACTIONS_LITERAL)

    assert actual_transactions == expected_transactions


def test_given_table_headers_missing_html_transactions_literal_when_parse_transactions_then_skip_broken_entries(
        html_parser_sut):
    expected_transactions = []

    actual_transactions = html_parser_sut.parse_transactions(TABLE_HEADERS_MISSING_HTML_TRANSACTIONS_LITERAL)

    assert actual_transactions == expected_transactions


def test_given_transactions_table_missing_html_transactions_literal_when_parse_transactions_then_return_empty_list(
        html_parser_sut):
    expected_transactions = []

    actual_transactions = html_parser_sut.parse_transactions(TRANSACTIONS_TABLE_MISSING_HTML_TRANSACTIONS_LITERAL)

    assert actual_transactions == expected_transactions


@pytest.mark.parametrize('date_invalid_format_html_literal', [DATE_INVALID_FORMAT_HTML_TRANSACTION_LITERAL_1,
                                                              DATE_INVALID_FORMAT_HTML_TRANSACTION_LITERAL_2],
                         ids=["date with only 2 elements: year and moth",
                              "date with more than 3 elements"])
def test_given_transactions_table_invalid_date_format_when_parse_transactions_then_raise_error(
        html_parser_sut, date_invalid_format_html_literal):
    with pytest.raises(RawDateInvalidFormat):
        html_parser_sut.parse_transactions(date_invalid_format_html_literal)
