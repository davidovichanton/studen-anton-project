"""
Написать функцию которая принимает список l и возвращает список
из элементов l которые больше чем количество элементов в списке l
>>> filter_list([1, 2])
[]
>>> filter_list([1, 10, 7, 2])
[10, 7]
"""
from typing import List


def filter_list(l: List[int]) -> List[int]:
    result = []
    n = len(l)
    for i in l:
        if i > n:
            result.append(i)
    return result


print(filter_list([1, 2]))
print(filter_list([1, 10, 7, 2]))


def foo(l):
    result = []
    for i in l:
        if i > 3:
            result.append(i)
        return result

print(foo([1, 2, 3, 4])) # -> 4


def bar(l): #l = [1, 2]
    result = []
    for i in l:
        result.append(i)
    return result

bar([1, 2])
"""посмотреть для двух функций что происходит. и потом модифицировать так что
будут добавлять в список элементы больше 3
"""
