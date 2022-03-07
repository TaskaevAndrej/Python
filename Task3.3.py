def my_func(a, b, c):
    if (a + b) >= (a + c) and (a + b) >= (b + c):
        return a + b
    if (a + c) >= (a + b) and (a + c) >= (b + c):
        return a + c
    if (b + c) >= (a + b) and (b + c) >= (a + c):
        return b + c


try:
    a1 = int(input("a = "))
    b1 = int(input("b = "))
    c1 = int(input("c = "))
    print(f"Вернуть сумму двух наибольших элементов:  {my_func(a1, b1, c1)}")
except ValueError as d:
    print(f"{d}")
