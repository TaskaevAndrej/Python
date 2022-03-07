def int_func(слово: str):
    первая_буква = слово[:1]
    заглавная_первая_буква = первая_буква.upper()
    остаток = слово[1:]
    return заглавная_первая_буква + остаток


def int_func_ext(строка: str):
    result = []
    предложение = строка.split(' ')
    for item in предложение:
        result.append(int_func(item))
    return ' '.join(result)


s = input("Введите строку для преобразования:\n")
print(f"{int_func_ext(s)}")
