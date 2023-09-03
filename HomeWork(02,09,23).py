import datetime
year = int(input("Введите год рождения "))
mounth = int(input("Введите месяц рождения "))
day = int(input("Введите день рождения "))
x = str(datetime.datetime.now() - datetime.datetime(year,mounth,day))
print(x[0:9])