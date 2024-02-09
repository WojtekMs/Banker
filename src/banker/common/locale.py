import logging

from babel import default_locale


def get_numeric_locale() -> str:
    if not get_numeric_locale.__numeric_locale:
        default_numeric_locale = "pl_PL"
        logging.getLogger().warning(
            f"Numeric locale could not be deduced from the environment, setting {default_numeric_locale} by default")
        get_numeric_locale.__numeric_locale = default_numeric_locale
    return get_numeric_locale.__numeric_locale


get_numeric_locale.__numeric_locale = default_locale('LC_NUMERIC')
