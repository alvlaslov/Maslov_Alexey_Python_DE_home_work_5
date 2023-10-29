"""
Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
имена str, ставка int, премия str с указанием процентов вида “10.25%”.
В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии
"""

employees = ['Tom', 'Alex', 'Jack', '']
salary = [1_000, 2_000, 3_000]
bonus_rate = ['10.25%', '12.5%', '20%']


def employee_bonus(name: list[str], salary: list[int], rate: list[str]) -> dict:
    if len(name) == len(salary) == len(rate):
        result = {emp: sal * (float(bon.rstrip('%'))) / 100 for emp, sal, bon in zip(employees, salary, bonus_rate)}
        return result
    else:
        return print('Lists are different lengths')


print(employee_bonus(employees, salary, bonus_rate))
