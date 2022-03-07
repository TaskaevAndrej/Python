def divvy(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return
    return result


try:
    a1 = float(input("a = "))
    b1 = float(input("b = "))
    print(f"a / b = {divvy(a1, b1)}")
except ValueError:
    print("На ноль делить нельзя")
