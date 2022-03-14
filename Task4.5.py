#Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти
#четные числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех
#элементов списка. Подсказка: использовать функцию reduce().

from functools import reduce


def multiplication(prev_el, el):
    return prev_el * el


print(reduce(multiplication, [n for n in range(100, 1001) if n % 2 == 0]))
