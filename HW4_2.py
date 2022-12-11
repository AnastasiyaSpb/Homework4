# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def prime_factor(num: int) -> list:
    if num == 1:
        return [1]
    res = []
    while num >= 2:
        if num % 2 == 0:
            res.append(2)
            num //= 2
        else:
            k = 3
            while num >= k:
                if num % k == 0:
                    res.append(k)
                    num //= k
                else:
                    k += 2
    return res


a = int(input("N = "))
print(f"{a} = {prime_factor(a)}")
