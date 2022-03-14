#Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
# необходимо использовать формулу: (выработка в часах*ставка в час) + премия. Для выполнения расчета для конкретных
# значений необходимо запускать скрипт с параметрами.
import sys
from HomeTask4 import calc_salary
print(sys.argv)

try:
    script, hours, money_per_hour, bonus = sys.argv
except ValueError:
    print("Invalid args")
    exit()
print(f"{calс_salary(hours, money_per_hour, bonus)}")
