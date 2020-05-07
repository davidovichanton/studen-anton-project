def monkey_count(n) -> int:
    result = 0
    for x in range(1, n + 1):  # [1]
        result = result + x
    return result


monkey_count(1)  # -> 1
monkey_count(2)
# |  range(start, stop[, step]) -> range object
range(1, 5)  # -> [1, 2]
# [1 2 3 4 5 6]
#  ^ ^ ^ ^
# n => stop=n+1
# 4 => stop=5
# 3 => stop=4
# 2 => stop=3
# 1 => stop=2
# range(1, 4) -> [1, 2, 3]
# [1 2 3 4 5 6]
#  ^ ^

# range(1, 2) -> [1]
# [1 2 3 4 5 6]
#  ^

# range(1, 1) -> []
# [1 2 3 4 5 6]
#
list(range(3))  # -> [0, 1, 2]
list(range(1, 4)) # -> [1, 2, 3]
list(range(5, 20, 3))  # -> [5, 8, 11, 14, 17]
list(range(2, 10))

# class range(object)
# |  range(stop) -> range object
# |  range(start, stop[, step]) -> range object


print(monkey_count(3))


result = 0
x = [1, 2, 3]
for y in x:
	result = result + y


def foo():
  return 42

def bar():
  return "bar"

def foobar():
  # функция вернет результат вызова функции print()
  return print()

def foobar():
  # функция вернет результат вызова функции foo()
  return foo()

foobar()  # -> 42
foo()
bar()
