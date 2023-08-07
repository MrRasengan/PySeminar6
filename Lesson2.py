# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
from random import randint

def check_neigbours(index, array):
    if array[(index + 1) % len(array)] < array[index] and array[index - 1] < array[index]:
        return True


N = int(input("Введите колличество элементов в первом массиве: "))
sp = [randint(1,5) for _ in range(N)]
print(sp)

result = [1 for index in range(len(sp)) if check_neigbours(index, sp)]
print(sum(result))