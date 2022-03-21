# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

import random

with open('Task5.5.data', 'w', encoding='UTF-8') as file:
    пробел = ''
    for _ in range(7):
        file.write(пробел + str(random.randint(0, 10)))
        пробел = ' '

with open('Task5.5.data', 'r', encoding='UTF-8') as file:
    numbers_str = file.read()
    numbers_lst = numbers_str.split(' ')
    print(f"Содержимое файла:\n{numbers_str}")
    print(f"Сумма чисел:\n{sum([int(n) for n in numbers_lst])}")
