# update this value in case supported version by parser is changed
CURRENTLY_SUPPORTED_VERSION_BY_PARSER = "1.0.0"

MISSING_VERSION_JSON_CATEGORIES_LITERAL = """{"categories": []}"""
INVALID_VERSION_JSON_CATEGORIES_LITERAL_1 = """{"version": "1", "categories": []}"""
INVALID_VERSION_JSON_CATEGORIES_LITERAL_2 = """{"version": "one", "categories": []}"""
INVALID_VERSION_JSON_CATEGORIES_LITERAL_3 = """{"version": "alpha", "categories": []}"""
INCOMPATIBLE_VERSION_JSON_CATEGORIES_LITERAL = """{"version": "0.1.0", "categories": []}"""

ONE_CATEGORY_JSON_CATEGORIES_LITERAL = f"""{{
"version": "{CURRENTLY_SUPPORTED_VERSION_BY_PARSER}", 
"categories": [
{{"name": "Kaufland", "payment_type": "household", "matching_regexes": ["KAUFLAND PL"]}}
]}}"""

MANY_CATEGORIES_JSON_CATEGORIES_LITERAL = f"""{{
"version": "{CURRENTLY_SUPPORTED_VERSION_BY_PARSER}", 
"categories": [
{{"name": "Kaufland", "payment_type": "household", "matching_regexes": ["KAUFLAND PL"]}},
{{"name": "Internet", "payment_type": "recurring", "matching_regexes": ["(?i)vectra"]}},
{{"name": "Shoes", "payment_type": "occasional", "matching_regexes": ["shoes", "adidas"]}},
{{"name": "Cafe", "payment_type": "optional", "matching_regexes": ["Klar", "Starbucks"]}},
{{"name": "Empty", "payment_type": "optional", "matching_regexes": []}}
]}}"""

SOME_INVALID_CATEGORIES_JSON_CATEGORIES_LITERAL = f"""{{
"version": "{CURRENTLY_SUPPORTED_VERSION_BY_PARSER}", 
"categories": [
{{"name": "Kaufland", "payment_type": "household", "matching_regexes": ["KAUFLAND PL"]}},
{{"noname": "Internet", "payment_type": "recurring", "matching_regexes": ["(?i)vectra"]}},
{{"name": "Shoes", "bad_payment": "occasional", "matching_regexes": ["shoes", "adidas"]}},
{{"name": "Cafe", "payment_type": "optional", "regxs": ["Klar", "Starbucks"]}}
]}}"""

INVALID_PAYMENT_TYPE_JSON_CATEGORIES_LITERAL = f"""{{
"version": "{CURRENTLY_SUPPORTED_VERSION_BY_PARSER}", 
"categories": [
{{"name": "Kaufland", "payment_type": "household", "matching_regexes": ["KAUFLAND PL"]}},
{{"name": "Internet", "payment_type": "unknown", "matching_regexes": ["(?i)vectra"]}},
{{"name": "Shoes", "payment_type": "", "matching_regexes": ["(?i)vectra"]}},
{{"name": "Cafe", "payment_type": "bad", "matching_regexes": ["(?i)vectra"]}}
]}}"""

DUPLICATE_NAMES_JSON_CATEGORIES_LITERAL = f"""{{
"version": "{CURRENTLY_SUPPORTED_VERSION_BY_PARSER}", 
"categories": [
{{"name": "Kaufland", "payment_type": "household", "matching_regexes": ["KAUFLAND PL"]}},
{{"name": "Internet", "payment_type": "recurring", "matching_regexes": ["(?i)vectra"]}},
{{"name": "Kaufland", "payment_type": "optional", "matching_regexes": ["Starbucks"]}}
]}}"""
