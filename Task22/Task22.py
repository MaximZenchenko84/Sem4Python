# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями)
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - количество элементов первого множества. m - количество элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input('Введите количество элементов первого множества n = '))
m = int(input('Введите количество элементов второго множества m = '))

firstArrayUnset = []
for i in range(0,n):
    currentNumber = int(input(f'Введите {i}-й элемент первого множества '))
    firstArrayUnset.append(currentNumber)

secondArrayUnset = []
for i in range(0,m):
    currentNumber = int(input(f'Введите {i}-й элемент второго множества '))
    secondArrayUnset.append(currentNumber)

# фильтрация от повторений и нахождение пересечения множеств
def cross(arr1, arr2):
    return list(set(arr1) & set(arr2))

# вывод результата
print(cross(firstArrayUnset, secondArrayUnset))