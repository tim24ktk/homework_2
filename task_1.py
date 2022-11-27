"""
    Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
    Пример:
    - 6782 -> 23
    - 0,56 -> 11
"""

# функция проверяет ли можно привести строку к вещественному числу,
# если нет то выбрасывает исключение
def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


while True:
    number = input('Введите вещественное число: ')
    if is_number(number):
        sum = 0
        exceptions = ['.', '-']
        for i in range(len(number)):
            if number[i] not in exceptions:
                sum += int(number[i])
        print(sum)
        break
    else:
        print('Вы ввели неверное значение! Попробуйте снова!')
