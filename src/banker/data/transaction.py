from dataclasses import dataclass 

@dataclass
class Transaction:
    _date: str 
    _value: float 
    _description: str
    
    @property
    def date(self) -> str:
        return self._date
    
    @property
    def value(self) -> float:
        return self._value
    
    @property
    def description(self) -> str:
        return self._description
    
    def count_matching(self, categories) -> int:
        return 0