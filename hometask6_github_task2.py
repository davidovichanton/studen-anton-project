"""
Написать функцию которая принимает целое число n и отдает список и чисел 1..n
>>> monkey_job(3) == [1, 2, 3]
>>> monkey_job(1) == [1]
>>> monkey_job(-5) == []
"""

def monkey_job (n):
    x = list(range(1, n + 1))
    return x


print(monkey_job(3))
