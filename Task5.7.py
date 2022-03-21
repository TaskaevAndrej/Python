# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма
# получила убытки, в расчет средней прибыли ее не включать. Далее реализовать список. Он должен содержать
# словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также
# добавить ее в словарь (со значением убытков).

import json

report = []
with open('Task5.7.data', 'r', encoding='UTF-8') as file:
    text = file.read()
    file.seek(0)
    profits = {}
    profit_sum = 0
    for row in file:
        items = row.split(' ')
        profit = int(items[2]) - int(items[3])
        if profit > 0:
            profits.update({items[0]: profit})
            profit_sum += profit
    report.append(profits)
    report.append({'average_profit': (profit_sum / len(profits))})

with open('Task5.7.data', 'w', encoding='UTF-8') as json_file:
    json.dump(report, json_file, ensure_ascii=False)

json_report = json.dumps(report, ensure_ascii=False)

print(f"Исходный файл:\n{text}\n")
print(f"Список:\n{report}\n")
print(f"json-объект:\n{json_report}")
