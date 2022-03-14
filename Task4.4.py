#Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел,
# соответствующих требованию. Элементы вывести в порядке их следования в исходном списке. Для выполнения задания
# обязательно использовать генератор.

def my_items(lst: list) -> dict:
    result = {}
    for key, value in enumerate(lst):
        if result.get(value) is None:
            result[value] = 1
        else:
            result[value] += 1
    return result


list_src = [3, 3, 7, 7, 23, 5, 1, 44, 44, 3, 5, 10, 1, 4, 11, 8]
counter = my_items(list_src)
list_res = [x for x, n in counter.items() if n == 1]
print(list_res)
