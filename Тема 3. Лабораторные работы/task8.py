money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
while money_capital >= spend:
    money_capital += salary
    spend *= 1 + increase
    money_capital -= spend
    month += 1

# TODO Оформить решение

print(month)
