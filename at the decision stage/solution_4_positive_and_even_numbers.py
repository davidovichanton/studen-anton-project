"""
Написать функцию которая принимает число и возвращает True если число
положительное и делиться на два и False в противном случае
>>> is_positive_and_even(3) == False
>>> is_positive_and_even(42) == True
>>> is_positive_and_even(-1) == False
"""

def is_positive(n):
    """Функция находит положительное число"""
    if n > 0:
        return True
    return False

def is_even(n):
    """Функция находит четное число"""
    if n % 2 == 0:
        return True
    return False

def is_positive_and_even(n):
    """Функция возращает результат двух функций: is_positive и is_even"""
    return is_positive(n) and is_even(n)

print(is_positive_and_even(-1))
