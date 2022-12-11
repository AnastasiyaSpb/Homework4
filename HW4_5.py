# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов
# (складываются числа, у которых "х" в одинаковых степенях).
# Пример того, что будет в итогвом файле: 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0

import pathlib
from pathlib import Path

f_path1 = Path("Homework", "Homework4", "result.txt")
f_path2 = Path("Homework", "Homework4", "result2.txt")
f_path3 = Path("Homework", "Homework4", "result3.txt")

with open(f_path1, "r") as data1:
    a = data1.read()
with open(f_path2, "r") as data2:
    b = data2.read()

list_a = a.replace("=", "+").split(" + ")
list_b = b.replace("=", "+").split(" + ")

with open(f_path3, "a") as data:
    for item in list_a[:-1]:
        for i in list_b[:-1]:
            if ("x" in item) and ("x" in i):
                if item[-2] == i[-2]:
                    if i[-2] == "*":
                        sum = int(item.split('*')[0])+int(i.split('*')[0])
                        data.write(f"{sum} * x ")
                    else:
                        sum = int(item.split('*')[0])+int(i.split('*')[0])
                        data.write(f"{sum} * (x**{item[-2]}) + ")
            if ("x" in item) == ("x" in i) == False:
                sum = int(item)+int(i)
                data.write(f"+ {sum}")
    data.write(" = 0")
