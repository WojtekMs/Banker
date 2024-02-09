from typing import Optional

import pytest

from banker.common.locale import get_numeric_locale


@pytest.fixture
def numeric_locale_patch(mocker):
    def _numeric_locale_patch(locale: Optional[str]) -> str:
        return mocker.patch('banker.common.locale.get_numeric_locale.__numeric_locale', locale)

    return _numeric_locale_patch


def test_given_locale_read_from_environment_when_get_locale_then_return_environment_locale(numeric_locale_patch):
    numeric_locale_patch("en_US")
    assert get_numeric_locale() == "en_US"
    assert get_numeric_locale() == "en_US"
    assert get_numeric_locale() == "en_US"


def test_given_no_environment_locale_when_get_locale_then_return_default_locale(numeric_locale_patch):
    numeric_locale_patch(None)
    assert get_numeric_locale() == "pl_PL"
    assert get_numeric_locale() == "pl_PL"
    assert get_numeric_locale() == "pl_PL"
