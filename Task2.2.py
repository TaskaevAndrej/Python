Elements = int(input("Введите размер списка: "))
list_original = []
list_mixed = []
for i in range(1, Elements + 1):
    item = input(f"Введите значение {i}-го элемента: ")
    list_original.append(item)
    if i % 2 == 0:
        list_mixed.append(item)
        list_mixed.append(list_original[i - 2])

if len(list_mixed) != Elements:
    list_mixed.append(list_original[Elements - 1])

print(f"Оригинальный список: {list_original}")
print(f"Смешаный список: {list_mixed}")
