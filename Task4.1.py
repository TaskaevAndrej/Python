#Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
# необходимо использовать формулу: (выработка в часах*ставка в час) + премия. Для выполнения расчета для конкретных
# значений необходимо запускать скрипт с параметрами.
import sys
from HomeTask4 import calc_salary
print(sys.argv)

_, hours, money_per_hour, bonus = sys.argv

salary = ((float(hours) * float(money_per_hour)) + float(bonus))

print(f"Заработная плата = {salary}")
