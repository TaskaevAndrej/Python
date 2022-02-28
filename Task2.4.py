Предложение = input("Введите строку из нескольких слов: ")
строки = Предложение.split(' ')
counter = 1
for item in строки:
     print(f"{counter} {item[0:10]}")
     counter += 1
