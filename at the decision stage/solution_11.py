"""
Написать функцию которая принимает строку и возвращает количество уникальные
символы в этой строке и их количество
>>> unique_symbols_with_count("aaab") == {"a": 3, "b": 1}
>>> unique_symbols_with_count("abc") == {"a": 1, "b": 1, "c": 1}
"""
from typing import Dict


def unique_symbols_with_count(s: str) -> Dict[str, int]:
    ...
