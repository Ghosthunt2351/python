from sys import argv

salary, hours, rate, bonus = argv
print('Зарплата работника равна:', (int(hours) * int(rate) + int(bonus)))
