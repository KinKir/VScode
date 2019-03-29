# DayDayUpQ2.py//百分之一的力量
dayfactor = 0.01
dayup = pow(1+dayfactor, 365)
daydown = pow(1-dayfactor, 365)
print("向上: {:.2f}\n向下: {:.2f}".format(dayup, daydown))