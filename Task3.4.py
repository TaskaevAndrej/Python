def my_abs(x):
    return x if x >= 0 else x * -1


def raising_to_power(x, y):
    result = x
    for i in range(my_abs(y) - 1):
        result *= x
    if y < 0:
        result = 1 / result
    return result


try:
    basis = int(input("x = "))
    degree = int(input("y = "))
    print(f"x ** y =  {raising_to_power(basis, degree)}")
except ValueError as e:
    print(e)
