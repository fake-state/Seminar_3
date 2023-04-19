#  Требуется найти в массиве A[1..N] самый близкий по величине
# элемент к заданному числу X. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X

A = list()
N = int(input('Введите N > '))

# Заполняем список:
for i in range(N):
    A.append(i + 1)

print(f'Ваш список {A}')

X = int(input('Введите X > '))

difference = X - A[0]
close_Number = A[0]
for i in range(len(A)):
    if X - A[i] < difference:
        difference = X - A[i]
    close_Number = A[i]

print(f'Ближайшее к X число:  {close_Number}')
