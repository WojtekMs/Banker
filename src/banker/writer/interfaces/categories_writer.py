from abc import ABC, abstractmethod

from banker.data.category import Category


class ICategoriesWriter(ABC):
    @abstractmethod
    def write_categories(self, categories: list[Category], output_filepath: str, title: str | None = None) -> None:
        raise NotImplementedError("Method not implemented in subclass")
