from abc import ABC, abstractmethod

from banker.data.category import Category


class ICategoriesParser(ABC):
    @abstractmethod
    def parse_categories(self, content: str) -> list[Category]:
        raise NotImplementedError("Method not implemented in subclass")
