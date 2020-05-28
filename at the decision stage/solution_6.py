"""
Написать функцию которая принимает строку и возвращает количество уникальные
символы в этой строке и их количество
>>> unique_symbols_with_count("aaab") == {"a": 3, "b": 1}
>>> unique_symbols_with_count("abc") == {"a": 1, "b": 1, "c": 1}
"""

from typing import Dict

def unique_symbols_with_count(s):
    result = {}
    for symbol in s:
        if symbol not in result:
            count = count_symbol(s, symbol)
            result[symbol] = count
    return result

def count_symbol(s, symbol):
    count = 0
    for i in s:
        if i == symbol:
            count += 1

    return count

print(unique_symbols_with_count("aaabb"))
print(unique_symbols_with_count("acccc"))
