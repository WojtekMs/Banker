import logging
import semver
import json

from banker.common.naming import CATEGORIES_KEY_NAME_VERSION, CATEGORIES_KEY_NAME_CATEGORIES, \
    CATEGORIES_KEY_NAME_CATEGORY_NAME, CATEGORIES_KEY_NAME_CATEGORY_PAYMENT_TYPE, CATEGORIES_KEY_NAME_CATEGORY_REGEXES
from banker.data.category import Category
from banker.parser.interfaces.categories_parser import ICategoriesParser
from banker.parser.payment_type_parser import parse_payment_type


class CategoriesVersionMissing(Exception):
    def __str__(self):
        return f"Key {CATEGORIES_KEY_NAME_VERSION} is missing in categories JSON file"


class CategoriesVersionInvalid(Exception):
    def __init__(self, version: str):
        self.__version = version

    def __str__(self):
        return f"Categories version has invalid format, " \
               f"expected semantic versioning e.g: 1.0.0, actual: {self.__version}"


class CategoriesVersionUnsupported(Exception):
    def __init__(self, supported_version: semver.Version, current_version: semver.Version):
        self.__supported_version = supported_version
        self.__current_version = current_version

    def __str__(self):
        return f"Categories version is unsupported by application, " \
               f"supported version: {self.__supported_version}, current version: {self.__current_version}"


class CategoryNameDuplicate(Exception):
    def __init__(self, name: str):
        self.__name = name

    def __str__(self):
        return f"Categories names must be unique, but this category name is used multiple times: {self.__name}"


class JsonCategoriesParser(ICategoriesParser):
    def __init__(self):
        self.__supported_version = semver.Version(major=1, minor=0, patch=0)
        self.__logger = logging.getLogger("JsonCategoriesParser")

    def __validate_version(self, json_dict: dict):
        version = json_dict.get(CATEGORIES_KEY_NAME_VERSION)
        if version is None:
            raise CategoriesVersionMissing()
        if not semver.Version.is_valid(version):
            raise CategoriesVersionInvalid(version)
        version = semver.Version.parse(version)
        if not self.__supported_version.is_compatible(version):
            raise CategoriesVersionUnsupported(self.__supported_version, version)

    def __contains_required_keys(self, category: dict) -> bool:
        required_keys = [CATEGORIES_KEY_NAME_CATEGORY_NAME, CATEGORIES_KEY_NAME_CATEGORY_PAYMENT_TYPE,
                         CATEGORIES_KEY_NAME_CATEGORY_REGEXES]
        for required_key in required_keys:
            if required_key not in category:
                self.__logger.info(f"Category object key missing: {required_key}")
                return False
        return True

    def __valid_payment_type(self, category: dict) -> bool:
        if parse_payment_type(category[CATEGORIES_KEY_NAME_CATEGORY_PAYMENT_TYPE]) is None:
            self.__logger.info("Invalid payment type")
            return False
        return True

    def parse_categories(self, content: str) -> list[Category]:
        json_dict = json.loads(content)
        self.__validate_version(json_dict)

        result = {}
        for category in json_dict.get(CATEGORIES_KEY_NAME_CATEGORIES, []):
            if not self.__contains_required_keys(category):
                continue
            if not self.__valid_payment_type(category):
                continue
            name = category[CATEGORIES_KEY_NAME_CATEGORY_NAME]
            if name in result:
                raise CategoryNameDuplicate(name)
            payment_type = parse_payment_type(category[CATEGORIES_KEY_NAME_CATEGORY_PAYMENT_TYPE])
            matching_regexes = category[CATEGORIES_KEY_NAME_CATEGORY_REGEXES]
            result[name] = Category(name, payment_type, matching_regexes)
        return list(result.values())
