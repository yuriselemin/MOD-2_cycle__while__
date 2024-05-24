
# Домашняя работа по уроку "Стиль кода часть II. Цикл While."




my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

num = 0

while num <= len(my_list):
    if my_list[num] > 0:
        print(my_list[num])
    num += 1
    if my_list[num] == 0:
        continue
    if my_list[num] < 0:
        break



# небольшая вариация задания для закрепления

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
positive_list = []

num = 0

while num <= len(my_list):
    if my_list[num] > 0:
        positive_list.append(my_list[num])
    num += 1
    if my_list[num] == 0:
        continue
    if my_list[num] < 0:
        break
print(f'Список положительных чисел: \n{positive_list}')