
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


# еще пример

# Сортировка фруктов в два списка

favorite_fruits = []
not_favorite_fruits = []

while True:
    fruits = input('Название фрукта: ').lower()  # Приводим ввод к нижнему регистру

    if fruits in ['яблоко', 'груша', 'персик']:
        print('Вы угадали! Это я люблю ')
        favorite_fruits.append(fruits)
        print(f'Список любимых фруктов: \n{favorite_fruits}')
    else:
        print('Нет, спасибо - это не вкусно!')
        not_favorite_fruits.append(fruits)
        print(f'Список  не любимых фруктов: \n{not_favorite_fruits}')

    continue_game = input("Хотите ввести ещё один фрукт? (y/n)")
    if continue_game != 'y':
        break  # Выходим из цикла, если пользователь не хочет продолжать

print(f"Мои нелюбимые фрукты: {not_favorite_fruits}")




