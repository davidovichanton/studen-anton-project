"""
Написать функцию которая принимает строку и возвращает уникальные символы в
этой строке
>>> unique_symbols("aaab") == ["a", "b"]
>>> unique_symbols("abc") == ["a", "b", "c"]
"""
from typing import List

def unique_symbols_with_count(s):
"""функция возращает уникальные символы в строке
"""
    seen = []
    for i in s:
        if i not in seen:
            seen.append(i)
    return seen


print(unique_symbols_with_count("aaab"))
