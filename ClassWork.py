# import math
# weight_moon = 7.347 * math.pow(10,22)
# g = 6.6743 * math.pow(10,-11)
# weight_second = float(input("adaad"))*math.pow(int(input("dsdafa")),int(input("adad")))
# distance = int(input("Введите расстояние желаемой планеты до Луны в метрах"))
# f = (g * weight_moon * weight_second) / (math.pow(distance, 2))
# print(f)

import math
weight_moon = 7.347 * math.pow(10,22)
g = 6.6743 * math.pow(10,-11)
weight_second = input("Введите массу второй планеты")
weight_second1 = list(weight_second.split("*"))
weight_second1.remove(min(weight_second1))
weight_second3 = float(weight_second1[0])*int(weight_second1[1])**int(weight_second1[2])
distance = int(input("Введите расстояние желаемой планеты до Луны в метрах"))
f = (g * weight_moon * weight_second3) / (math.pow(distance, 2))
print(f)