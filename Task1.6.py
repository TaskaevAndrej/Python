a = int(input("Введите результат пробежки первого дня в км >>>"))
b = int(input("Введите общий желаемый результат в км >>>"))
result_days = 1
result_km = a
while result_km < b:
        a = a + 0.1 * a
        result_days = result_days + 1
        result_km = result_km + a
print(f"Вы достигнете желаемый результат на %.d день" % result_days)
