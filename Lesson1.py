# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
from random import randint

N = int(input("Введите колличество элементов в первом массиве: "))
M = int(input("Введите колличество элементов во втором массиве: "))

sp1 = [randint(1,10) for _ in range(N)]
sp2 = [randint(1,10) for _ in range(M)]

print(sp1)
print(sp2)

result = [item for item in sp1 if item not in sp2]
print(result)