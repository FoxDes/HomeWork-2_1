# 1. Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.

# a = int(input('Введите день недели от 1 до 7: '))
# if a > 0 and a < 6:
#     print('это рабочий день')
# else:
#     print('Ошибка! необходимо ввести число от 1 до 7')
# if a > 5 and a < 8:
#     print('это выходной день')



# 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# для всех значений предикат.

# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             a = not (x or y or z)
#             b = not x and not y and not z
#             result = a == b
#     print("True")
# else:
#     print("False")



# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и 
# выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# x = int(input('Введите координаты X: '))
# y = int(input('Введите координаты Y: '))
# if x > 0 and y > 0:
#     print('1 четверть')
# elif x < 0 and y < 0:
#     print('3 четверть')
# elif x > 0 and y < 0:
#     print('4 четверть')
# elif x < 0 and y > 0:
#     print('2 четверть')
# else:
#     print('Введены не правельные координаты')



# 4. Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

# quarter = int(input('Введите номер четверти: '))
# if quarter == 1:
#     print('+x, +y')
# elif quarter == 3:
#     print('-x, -y')
# elif quarter == 4:
#     print('+x, -y')
# elif quarter == 2:
#     print('-x, +y')
# else:
#     print('Введены не корректные данные')


# 5. Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.

# x_1 = int(input('Введите координаты точки А по Х: '))
# y_1 = int(input('Введите координаты точки А по Y: '))
# x_2 = int(input('Введите координаты точки В по Х: '))
# y_2 = int(input('Введите координаты точки В по Y: '))
# print(f"{((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2) **0.5:0.4}")



