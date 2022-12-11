# Вычислить число π c заданной точностью d
# Пример: при d = 0.001, π = 3.141
# Ввод: 0.01
# Вывод: 3.14
# Ввод: 0.001
# Вывод: 3.141

def pi_leib(num: str) -> float:
    den = 1
    sum = 0
    for item in range(1000000):
        if item % 2 == 0:
            sum += 4 / den
        else:
            sum -= 4/den
        den += 2
    return round(sum, len(num)-2)


a = input("Точность числа π: ")
print(pi_leib(a))
