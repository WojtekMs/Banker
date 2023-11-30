from banker.data.transaction import Transaction
import pytest
from moneyed import Money, PLN


@pytest.fixture
def transaction1():
    return Transaction(date="2023-11-01", description="000015792 05272423303314705681107 "
                                                      "Lokalizacja : "
                                                      "Adres : KAUFLAND PL 6663 "
                                                      "Miasto : Gliwice "
                                                      "Kraj : POLSKA "
                                                      "Data i czas operacji : 2023-10-30 "
                                                      "Oryginalna kwota operacji : 37.35 "
                                                      "Numer karty : 516931******3943",
                       value=Money(amount='-37.35', currency=PLN))


@pytest.fixture
def transaction2():
    return Transaction(date="2023-11-01", description="PKO BP 10202498S1KA0767N6623C2783 "
                                                      "Lokalizacja : "
                                                      "Adres : UL. DWORCOWA 25 "
                                                      "Miasto : GLIWICE "
                                                      "Kraj : POLSKA "
                                                      "Data i czas operacji : 2023-10-30 "
                                                      "Oryginalna kwota operacji : 200.00 "
                                                      "Numer karty : 516931******3943",
                       value=Money(amount='-200.00', currency=PLN))


@pytest.fixture
def transaction3():
    return Transaction(date="2023-10-31", description="00000076965444780 "
                                                      "Numer telefonu : 48001002003 "
                                                      "Lokalizacja : "
                                                      "Adres : intercity.pl "
                                                      "'Operacja : 00000076965444780 "
                                                      "Numer referencyjny : 00000076965444780",
                       value=Money(amount='-49.02', currency=PLN))


@pytest.fixture
def transaction4():
    return Transaction(date="2023-10-31", description="Nazwa nadawcy : JAN KOWALSKI "
                                                      "Adres nadawcy : "
                                                      "UL.GULASZOWA 0 "
                                                      "00-001 WROCŁAW POL "
                                                      "Tytuł : WPŁATA", value=Money(amount='800.00', currency=PLN))


@pytest.fixture
def transaction5():
    return Transaction(date="2023-10-08", description="Rachunek odbiorcy : 000000000000000000000 "
                                                      "Nazwa odbiorcy : Alicja "
                                                      "Tytuł : Na korki", value=Money(amount='-50.00', currency=PLN))
