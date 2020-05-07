"""
Написать функцию которая принимает список чисел и возвращает максимальное из
них
>>> max(1, 2, 3)
3
>>> max(-5, 4, 10)
10
"""
from typing import List


def max(l):
    m = float("-inf")
    for i in l:
        if i > m:
            m = i
    return m

l = [-5, 4, 10]
m = max(l)
print m
