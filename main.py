from random import randint


def square(sp):
    rezult = []
    for item in sp:
        rezult.append(item**2)
        return rezult

def find4_and_square(sp):
    rezult = []
    for item in sp:
        if item > 4:
            rezult.append(item**2)
    return rezult


sp = [1, 2, 3, 8, 10, 5]
print(5 in sp)
print(5 not in sp)
# print(square(sp))
# print([item**2 for item in sp])
# print([randint(0,10) for _ in range(10)])
# print(find4_and_square(sp))
# print([item**2 for item in sp if item > 4])