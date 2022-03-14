def calс_salary(hours_, money_per_hour_, bonus_):
    try:
        result = (int(hours_) * float(money_per_hour_)) + float(bonus_)
    except ValueError:
        return
