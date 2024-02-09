import pytest
from moneyed import format_money

from banker.common.locale import get_numeric_locale
from banker.formatter.html_transactions_formatter import HtmlTransactionsFormatter


@pytest.fixture
def html_transactions_formatter_sut():
    return HtmlTransactionsFormatter()


def test_given_empty_transactions_when_format_transactions_then_return_empty_table_with_headers(
        html_transactions_formatter_sut):
    expected_result = ('<table border="1" class="dataframe">\n'
                       '  <thead>\n'
                       '    <tr style="text-align: right;">\n'
                       '      <th></th>\n'
                       '      <th>Data operacji</th>\n'
                       '      <th>Typ transakcji</th>\n'
                       '      <th>Opis</th>\n'
                       '      <th>Kwota</th>\n'
                       '    </tr>\n'
                       '  </thead>\n'
                       '  <tbody>\n'
                       '  </tbody>\n'
                       '</table>')

    actual_result = html_transactions_formatter_sut.format_transactions([])

    assert actual_result == expected_result


def test_given_transactions_when_format_transactions_then_return_html_table_with_headers_and_rows(
        html_transactions_formatter_sut, transaction1, transaction2):
    expected_transaction_1_value = format_money(transaction1.value, locale=get_numeric_locale())
    expected_transaction_2_value = format_money(transaction2.value, locale=get_numeric_locale())
    expected_result = ('<table border="1" class="dataframe">\n'
                       '  <thead>\n'
                       '    <tr style="text-align: right;">\n'
                       '      <th></th>\n'
                       '      <th>Data operacji</th>\n'
                       '      <th>Typ transakcji</th>\n'
                       '      <th>Opis</th>\n'
                       '      <th>Kwota</th>\n'
                       '    </tr>\n'
                       '  </thead>\n'
                       '  <tbody>\n'
                       '    <tr>\n'
                       '      <th>0</th>\n'
                       f'      <td>{transaction1.date}</td>\n'
                       f'      <td>{transaction1.type}</td>\n'
                       f'      <td>{transaction1.description}</td>\n'
                       f'      <td>{expected_transaction_1_value}</td>\n'
                       '    </tr>\n'
                       '    <tr>\n'
                       '      <th>1</th>\n'
                       f'      <td>{transaction2.date}</td>\n'
                       f'      <td>{transaction2.type}</td>\n'
                       f'      <td>{transaction2.description}</td>\n'
                       f'      <td>{expected_transaction_2_value}</td>\n'
                       '    </tr>\n'
                       '  </tbody>\n'
                       '</table>')

    actual_result = html_transactions_formatter_sut.format_transactions([transaction1, transaction2])

    assert actual_result == expected_result
    # exact format is dependent on locale; try to make tests locale-independent
    assert "37" in expected_transaction_1_value
    assert "-" in expected_transaction_1_value
    assert "200" in expected_transaction_2_value
    assert "-" in expected_transaction_2_value
