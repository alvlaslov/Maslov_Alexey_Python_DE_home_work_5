"""
Создайте функцию генератор чисел Фибоначчи
"""


def fibonacci(number: int) -> int:
    if number > 0:
        result = [0, 1]
        while number > 0:
            yield result[-1]
            result.append(result[-1] + result[-2])
            number -= 1
    if number < 0:
        result_1 = [0, 1]
        while number < 0:
            yield result_1[-1]
            result_1.append(result_1[-2] - result_1[-1])
            number += 1


for num in fibonacci(-10):
    print(num)
