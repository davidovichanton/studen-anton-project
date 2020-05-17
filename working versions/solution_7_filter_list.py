"""
Написать функцию которая принимает список l и возвращает список
из элементов l которые больше чем количество элементов в списке l
>>> filter_list([1, 2])
[]
>>> filter_list([1, 10, 7, 2])
[10, 7]
"""
from typing import List


def filter_list(l):
"""функция принимает список и возращает список из элементов
которые больше чем количество элементов
"""
    result = []
    n = len(l)
    for i in l:
        if i > n:
            result.append(i)
    return result


print(filter_list([1, 2]))
print(filter_list([1, 10, 7, 2]))
