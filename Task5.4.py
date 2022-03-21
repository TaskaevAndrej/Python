# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

text_en = ''
with open('Task5.4.data', 'r', encoding='UTF-8') as file_en:
    text_en = file_en.read()

text_ru = text_en
for en, ru in dict.items():
    text_ru = text_ru.replace(en, ru)

with open('task04.tmp', 'w', encoding='UTF-8') as file_ru:
    file_ru.write(text_ru)
