"""
Написать функцию которая принимает число и возвращает максимальную цифру из
этого числа
>>> max_digit(10)
1
>>> max_digit(41339)
9
>>> max_digit(658456000)
8
"""

def max_digit(n):
    result = []
    for i in n:
        result.append(i)
    return max(result)

print(max_digit(str(10)))
