выручка = float(input("Введите выручку фирмы >>>"))
издержки = float(input("Введите издержки фирмы >>>"))
if выручка > издержки:
    print(f"Фирма работает с прибылью. Рентабельность выручки составила {выручка / издержки:.2f}")
    сотрудники = int(input("Введите количество сотрудников фирмы >>>"))
    print(f"прибыль в расчете на одного сторудника сотавила {выручка / сотрудники:.2f}")
elif выручка == издержки:
    print("Фирма работает в ноль")
else:
    print("Фирма работает в убыток")