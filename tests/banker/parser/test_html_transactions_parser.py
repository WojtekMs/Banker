import pytest

from banker.parser.html_transactions_parser import HtmlTransactionsParser
from tests.banker.parser.test_data.html_transactions import HTML_TRANSACTIONS_LITERAL, ONE_HTML_TRANSACTION_LITERAL, \
    BROKEN_HTML_TRANSACTIONS_LITERAL, TABLE_HEADERS_MISSING_HTML_TRANSACTIONS_LITERAL, \
    TRANSACTIONS_TABLE_MISSING_HTML_TRANSACTIONS_LITERAL


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
