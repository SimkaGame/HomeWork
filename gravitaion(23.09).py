import requests
from math import pow
import json


url = requests.get("https://api.wheretheiss.at/v1/satellites/25544")
grav = 6.6743 * pow(10, -11)
m1 = 5.976 * pow(10, 24)
m2 = float(input("Введите Масса в кг без степени")) * pow(10,int(input("степень")))
m3 = 42 * pow(10,7)
distanse = int(input("Расстояние в км")) * 1000
altitude = url.json()['altitude']

def f(x,y,z):
    return (grav * m1 * m2) * (z**2)

print("Притяжение от Земли до МКС ",f(m1,m3,altitude))
print("Притяжение от земли до другой планеты", f(m1,m2,distanse))