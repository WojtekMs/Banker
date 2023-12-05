import pytest

from banker.data.category import PaymentType
from banker.parser.payment_type_parser import parse_payment_type


@pytest.mark.parametrize('invalid_payment_type_str', ["invalid", "HOUSEHOLD", "duck", "213979", "", '', "Household"])
def test_given_invalid_payment_type_str_when_parse_payment_type_then_return_none(invalid_payment_type_str):
    assert parse_payment_type(invalid_payment_type_str) is None


@pytest.mark.parametrize('payment_type_str, expected_result', [("household", PaymentType.Household),
                                                               ("recurring", PaymentType.Recurring),
                                                               ("occasional", PaymentType.Occasional),
                                                               ("optional", PaymentType.Optional)])
def test_given_valid_payment_type_str_when_parse_payment_type_then_return_payment_type(payment_type_str,
                                                                                       expected_result):
    actual_result = parse_payment_type(payment_type_str)

    assert actual_result == expected_result
