"""
    Задайте список из N элементов, заполненных числами из промежутка [-N, N].
    Найдите произведение элементов на указанных позициях.
    Позиции хранятся в файле file.txt в одной строке одно число.
    (для продвинутых - с файлом, вариант минимум - ввести позиции в консоли) -2 -1 0 1 2 Позиции: 0,1 -> 2
"""

value = int(input('Введите число больше нуля: '))

if value > 0:
    file = open('file.txt')
    indexes = file.read().split('\n')
    result = []
    product = 1
    flag = 0

    for i in range(-value, value + 1):
        result.append(i)

    for i, d in enumerate(indexes):
        if d.isnumeric() and int(d) < len(result):
            product *= result[int(d)]
        else:
            flag = 1
            break

    if flag == 0:
        print(product)
    else:
        print('Не удалось посчитать, т.к. один из индексов в файле больше чем длина списка или индекс указан не цифрами!')
else:
    print('Вы ввели неверное число!')
