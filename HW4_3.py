# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Ввод: [1, 1, 2, 3, 4, 4, 4]
# Вывод: [2, 3]

def not_rep(list_num: list[int]) -> list:
    return [num for num in list_num if list_num.count(num) == 1]


a = list(map(int, input("Задайте последовательность чисел через пробел: ").split()))
print(not_rep(a))
