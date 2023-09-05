# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке,
# причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растёт N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сбора
# на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать
# за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

n = int(input('Введите количество кустов, высаженных кругом, n, n >= 3 '))
arrayBerries = []
# ввод количества ягод на каждом кусте
for i in range(0,n):
    currentNumber = int(input(f'Введите количество ягод на {i+1}-м кусте: '))
    arrayBerries.append(currentNumber)



# формирование массива количества ягод, которые можно собрать, находясь на каждом кусте, и поиск максимума
arrayBerriesFromThreeBushes = []
arrayBerriesFromThreeBushes.append(arrayBerries[n-1] + arrayBerries[0] + arrayBerries[1])
max = arrayBerriesFromThreeBushes[0]
for i in range(1,n-1):
    arrayBerriesFromThreeBushes.append(arrayBerries[i-1] + arrayBerries[i] + arrayBerries[i+1])
    if arrayBerriesFromThreeBushes[i] > max:
        max = arrayBerriesFromThreeBushes[i]
arrayBerriesFromThreeBushes.append(arrayBerries[n-2] + arrayBerries[n-1] + arrayBerries[0])
if (arrayBerriesFromThreeBushes[n-1] > max):
    max = arrayBerriesFromThreeBushes[n-1]

print(f'Максимальное количество ягод, которое можно собрать, находясь на каждом кусте, равно {max}')
