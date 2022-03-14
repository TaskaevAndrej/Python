#Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего
# элемента.

list_original: list[int] = [235, 7, 16, 9, 3, 3, 4, 24, 8, 1, 85, 214, 65]
list_result = [a for b, c in enumerate(list_original) for a in list_original[b+1:b+2] if a > c]
print(list_result)
