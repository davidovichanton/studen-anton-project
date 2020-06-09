"""
Написать функцию которая принимает два списка и возвращает список из элементов
которые есть в первом и во втором списке
>>> inner_join([1, 2, 3], [2, 3, 4])
[2, 3]
>>> inner_join([1, 2, 3], [5, 10, 11])
[]
>>> inner_join([7, 4, 10], [5, 10, 11])
[10]
"""
from typing import List, Any


def inner_join(l1, l2):
    result = []
    for i1 in l1:
        if find(l2, i1):
            result.append(i1)
    return result

def find(l, x):
    return x in l

print(inner_join([1, 2, 3], [2, 3, 4]))
