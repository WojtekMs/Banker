ONE_HTML_TRANSACTION_LITERAL = """<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<meta name="Author" content="PKOInteligo (www.pkointeligo.pl)">
</head>
<body>
<h3>Kryteria wyszukiwania</h3>
<table id="search_criteria"><tbody>
<tr>
<td>Numer rachunku</td>
<td>00000000000000000000000</td>
</tr>
<tr>
<td>Od dnia</td>
<td>2023-10-01</td>
</tr>
<tr>
<td>Do dnia</td>
<td>2023-11-01</td>
</tr>
<tr>
<td>Rodzaj operacji</td>
<td>Wszystkie</td>
</tr>
</tbody></table>
<table id="lista_transakcji"><tbody>
<tr>
<th>Data operacji<br>
</th>
<th>Data waluty<br>
</th>
<th>Typ transakcji<br>
</th>
<th>Opis<br>
</th>
<th>Kwota<br>
</th>
<th>Waluta<br>
</th>
</tr>
<tr>
<td>2023-11-01</td>
<td>2023-10-30</td>
<td>Płatność kartą</td>
<td>000015792<br>05272423303314705681107<br>Lokalizacja :<br>Adres : KAUFLAND PL 6663<br>Miasto : Gliwice<br>Kraj : POLSKA<br>Data i czas operacji : 2023-10-30<br>Oryginalna kwota operacji : 37.35<br>Numer karty : 516931******3943<br>
</td>
<td>-37.35</td>
<td>PLN</td>
</tr>
</tbody></table>
</body>
</html>"""

HTML_TRANSACTIONS_LITERAL = """<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<meta name="Author" content="PKOInteligo (www.pkointeligo.pl)">
</head>
<body>
<h3>Kryteria wyszukiwania</h3>
<table id="search_criteria"><tbody>
<tr>
<td>Numer rachunku</td>
<td>00000000000000000000000</td>
</tr>
<tr>
<td>Od dnia</td>
<td>2023-10-01</td>
</tr>
<tr>
<td>Do dnia</td>
<td>2023-11-01</td>
</tr>
<tr>
<td>Rodzaj operacji</td>
<td>Wszystkie</td>
</tr>
</tbody></table>
<table id="lista_transakcji"><tbody>
<tr>
<th>Data operacji<br>
</th>
<th>Data waluty<br>
</th>
<th>Typ transakcji<br>
</th>
<th>Opis<br>
</th>
<th>Kwota<br>
</th>
<th>Waluta<br>
</th>
</tr>
<tr>
<td>2023-11-01</td>
<td>2023-10-30</td>
<td>Płatność kartą</td>
<td>000015792<br>05272423303314705681107<br>Lokalizacja :<br>Adres : KAUFLAND PL 6663<br>Miasto : Gliwice<br>Kraj : POLSKA<br>Data i czas operacji : 2023-10-30<br>Oryginalna kwota operacji : 37.35<br>Numer karty : 516931******3943<br>
</td>
<td>-37.35</td>
<td>PLN</td>
</tr>
<tr>
<td>2023-11-01</td>
<td>2023-10-30</td>
<td>Wypłata z bankomatu</td>
<td>PKO BP<br>10202498S1KA0767N6623C2783<br>Lokalizacja :<br>Adres : UL. DWORCOWA 25<br>Miasto : GLIWICE<br>Kraj : POLSKA<br>Data i czas operacji : 2023-10-30<br>Oryginalna kwota operacji : 200.00<br>Numer karty : 516931******3943<br>
</td>
<td>-200.00</td>
<td>PLN</td>
</tr>
<tr>
<td>2023-10-31</td>
<td>2023-10-28</td>
<td>Płatność web - kod mobilny</td>
<td>00000076965444780<br>Numer telefonu : 48001002003<br>Lokalizacja :<br>Adres : intercity.pl<br>'Operacja : 00000076965444780<br>Numer referencyjny : 00000076965444780<br>
</td>
<td>-49.02</td>
<td>PLN</td>
</tr>
<tr>
<td>2023-10-31</td>
<td>2023-10-31</td>
<td>Wpłata gotówkowa w kasie</td>
<td>Nazwa nadawcy : <br>JAN KOWALSKI<br>Adres nadawcy : <br>UL.GULASZOWA 0<br>00-001 WROCŁAW POL<br>Tytuł : <br>WPŁATA<br>
</td>
<td>+800.00</td>
<td>PLN</td>
</tr>
<tr>
<td>2023-10-08</td>
<td>2023-10-08</td>
<td>Zlecenie stałe</td>
<td>Rachunek odbiorcy : <br>000000000000000000000<br>Nazwa odbiorcy : <br>Alicja<br>Tytuł : <br>Na korki<br>
</td>
<td>-50.00</td>
<td>PLN</td>
</tr>
</tbody></table>
</body>
</html>"""

BROKEN_HTML_TRANSACTIONS_LITERAL = """<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<meta name="Author" content="PKOInteligo (www.pkointeligo.pl)">
</head>
<body>
<h3>Kryteria wyszukiwania</h3>
<table id="search_criteria"><tbody>
<tr>
<td>Numer rachunku</td>
<td>00000000000000000000000</td>
</tr>
<tr>
<td>Od dnia</td>
<td>2023-10-01</td>
</tr>
<tr>
<td>Do dnia</td>
<td>2023-11-01</td>
</tr>
<tr>
<td>Rodzaj operacji</td>
<td>Wszystkie</td>
</tr>
</tbody></table>
<table id="lista_transakcji"><tbody>
<tr>
<th>Data operacji<br>
</th>
<th>Data waluty<br>
</th>
<th>Typ transakcji<br>
</th>
<th>Opis<br>
</th>
<th>Kwota<br>
</th>
<th>Waluta<br>
</th>
</tr>
<tr>
<td>2023-11-01</td>
<td>2023-10-30</td>
<td>Płatność kartą</td>
<td>000015792<br>05272423303314705681107<br>Lokalizacja :<br>Adres : KAUFLAND PL 6663<br>Miasto : Gliwice<br>Kraj : POLSKA<br>Data i czas operacji : 2023-10-30<br>Oryginalna kwota operacji : 37.35<br>Numer karty : 516931******3943<br>
</td>
<td>-37.35</td>
<td>PLN</td>
</tr>
<tr>
<td>2023-10-30</td>
<td>Wypłata z bankomatu</td>
<td>PKO BP<br>10202498S1KA0767N6623C2783<br>Lokalizacja :<br>Adres : UL. DWORCOWA 25<br>Miasto : GLIWICE<br>Kraj : POLSKA<br>Data i czas operacji : 2023-10-30<br>Oryginalna kwota operacji : 200.00<br>Numer karty : 516931******3943<br>
</td>
<td>-200.00</td>
<td>PLN</td>
</tr>
<tr>
<td>2023-10-31</td>
<td>2023-10-28</td>
<td>Płatność web - kod mobilny</td>
</td>
<td>-49.02</td>
<td>PLN</td>
</tr>
<tr>
<td>2023-10-31</td>
<td>2023-10-31</td>
<td>Wpłata gotówkowa w kasie</td>
<td>Nazwa nadawcy : <br>JAN KOWALSKI<br>Adres nadawcy : <br>UL.GULASZOWA 0<br>00-001 WROCŁAW POL<br>Tytuł : <br>WPŁATA<br>
</td>
<td>PLN</td>
</tr>
<tr>
<td>2023-10-08</td>
<td>2023-10-08</td>
<td>Zlecenie stałe</td>
<td>Rachunek odbiorcy : <br>000000000000000000000<br>Nazwa odbiorcy : <br>Alicja<br>Tytuł : <br>Na korki<br>
</td>
<td>-50.00</td>
</tr>
</tbody></table>
</body>
</html>"""

TABLE_HEADERS_MISSING_HTML_TRANSACTIONS_LITERAL = """<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<meta name="Author" content="PKOInteligo (www.pkointeligo.pl)">
</head>
<body>
<h3>Kryteria wyszukiwania</h3>
<table id="search_criteria"><tbody>
<tr>
<td>Numer rachunku</td>
<td>00000000000000000000000</td>
</tr>
<tr>
<td>Od dnia</td>
<td>2023-10-01</td>
</tr>
<tr>
<td>Do dnia</td>
<td>2023-11-01</td>
</tr>
<tr>
<td>Rodzaj operacji</td>
<td>Wszystkie</td>
</tr>
</tbody></table>
<table id="lista_transakcji"><tbody>
<tr>
<th>Data waluty<br>
</th>
<th>Typ transakcji<br>
</th>
<th>Opis<br>
</th>
<th>Waluta<br>
</th>
</tr>
<tr>
<td>2023-11-01</td>
<td>2023-10-30</td>
<td>Płatność kartą</td>
<td>000015792<br>05272423303314705681107<br>Lokalizacja :<br>Adres : KAUFLAND PL 6663<br>Miasto : Gliwice<br>Kraj : POLSKA<br>Data i czas operacji : 2023-10-30<br>Oryginalna kwota operacji : 37.35<br>Numer karty : 516931******3943<br>
</td>
<td>-37.35</td>
<td>PLN</td>
</tr>
<tr>
<td>2023-11-01</td>
<td>2023-10-30</td>
<td>Wypłata z bankomatu</td>
<td>PKO BP<br>10202498S1KA0767N6623C2783<br>Lokalizacja :<br>Adres : UL. DWORCOWA 25<br>Miasto : GLIWICE<br>Kraj : POLSKA<br>Data i czas operacji : 2023-10-30<br>Oryginalna kwota operacji : 200.00<br>Numer karty : 516931******3943<br>
</td>
<td>-200.00</td>
<td>PLN</td>
</tr>
<tr>
<td>2023-10-31</td>
<td>2023-10-28</td>
<td>Płatność web - kod mobilny</td>
<td>00000076965444780<br>Numer telefonu : 48001002003<br>Lokalizacja :<br>Adres : intercity.pl<br>'Operacja : 00000076965444780<br>Numer referencyjny : 00000076965444780<br>
</td>
<td>-49.02</td>
<td>PLN</td>
</tr>
<tr>
<td>2023-10-31</td>
<td>2023-10-31</td>
<td>Wpłata gotówkowa w kasie</td>
<td>Nazwa nadawcy : <br>JAN KOWALSKI<br>Adres nadawcy : <br>UL.GULASZOWA 0<br>00-001 WROCŁAW POL<br>Tytuł : <br>WPŁATA<br>
</td>
<td>+800.00</td>
<td>PLN</td>
</tr>
<tr>
<td>2023-10-08</td>
<td>2023-10-08</td>
<td>Zlecenie stałe</td>
<td>Rachunek odbiorcy : <br>000000000000000000000<br>Nazwa odbiorcy : <br>Alicja<br>Tytuł : <br>Na korki<br>
</td>
<td>-50.00</td>
<td>PLN</td>
</tr>
</tbody></table>
</body>
</html>"""

TRANSACTIONS_TABLE_MISSING_HTML_TRANSACTIONS_LITERAL = """<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<meta name="Author" content="PKOInteligo (www.pkointeligo.pl)">
</head>
<body>
<h3>Kryteria wyszukiwania</h3>
<table id="search_criteria"><tbody>
<tr>
<td>Numer rachunku</td>
<td>00000000000000000000000</td>
</tr>
<tr>
<td>Od dnia</td>
<td>2023-10-01</td>
</tr>
<tr>
<td>Do dnia</td>
<td>2023-11-01</td>
</tr>
<tr>
<td>Rodzaj operacji</td>
<td>Wszystkie</td>
</tr>
</tbody></table>
</body>
</html>"""

DATE_INVALID_FORMAT_HTML_TRANSACTION_LITERAL_1 = """<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<meta name="Author" content="PKOInteligo (www.pkointeligo.pl)">
</head>
<body>
<h3>Kryteria wyszukiwania</h3>
<table id="search_criteria"><tbody>
<tr>
<td>Numer rachunku</td>
<td>00000000000000000000000</td>
</tr>
<tr>
<td>Od dnia</td>
<td>2023-10-01</td>
</tr>
<tr>
<td>Do dnia</td>
<td>2023-11-01</td>
</tr>
<tr>
<td>Rodzaj operacji</td>
<td>Wszystkie</td>
</tr>
</tbody></table>
<table id="lista_transakcji"><tbody>
<tr>
<th>Data operacji<br>
</th>
<th>Data waluty<br>
</th>
<th>Typ transakcji<br>
</th>
<th>Opis<br>
</th>
<th>Kwota<br>
</th>
<th>Waluta<br>
</th>
</tr>
<tr>
<td>2023-11</td>
<td>2023-10-30</td>
<td>Płatność kartą</td>
<td>000015792<br>05272423303314705681107<br>Lokalizacja :<br>Adres : KAUFLAND PL 6663<br>Miasto : Gliwice<br>Kraj : POLSKA<br>Data i czas operacji : 2023-10-30<br>Oryginalna kwota operacji : 37.35<br>Numer karty : 516931******3943<br>
</td>
<td>-37.35</td>
<td>PLN</td>
</tr>
</tbody></table>
</body>
</html>"""

DATE_INVALID_FORMAT_HTML_TRANSACTION_LITERAL_2 = """<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<meta name="Author" content="PKOInteligo (www.pkointeligo.pl)">
</head>
<body>
<h3>Kryteria wyszukiwania</h3>
<table id="search_criteria"><tbody>
<tr>
<td>Numer rachunku</td>
<td>00000000000000000000000</td>
</tr>
<tr>
<td>Od dnia</td>
<td>2023-10-01</td>
</tr>
<tr>
<td>Do dnia</td>
<td>2023-11-01</td>
</tr>
<tr>
<td>Rodzaj operacji</td>
<td>Wszystkie</td>
</tr>
</tbody></table>
<table id="lista_transakcji"><tbody>
<tr>
<th>Data operacji<br>
</th>
<th>Data waluty<br>
</th>
<th>Typ transakcji<br>
</th>
<th>Opis<br>
</th>
<th>Kwota<br>
</th>
<th>Waluta<br>
</th>
</tr>
<tr>
<td>2023-11-01-05</td>
<td>2023-10-30</td>
<td>Płatność kartą</td>
<td>000015792<br>05272423303314705681107<br>Lokalizacja :<br>Adres : KAUFLAND PL 6663<br>Miasto : Gliwice<br>Kraj : POLSKA<br>Data i czas operacji : 2023-10-30<br>Oryginalna kwota operacji : 37.35<br>Numer karty : 516931******3943<br>
</td>
<td>-37.35</td>
<td>PLN</td>
</tr>
</tbody></table>
</body>
</html>"""
