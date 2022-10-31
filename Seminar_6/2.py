#Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# from random import randint


# number = int(input('Введите размер списка '))
# list = []
# list2 = []

# for i in range(number):
#     list.append(randint(0, 9))

# for i in range(len(list)):
#     while i < len(list)/2 and number > len(list)/2:
#         number = number - 1
#         a = list[i] * list[number]
#         list2.append(a)
#         i += 1

# print(list)
# print(list2)

from random import randint


number = int(input('Введите размер списка '))

list_in = []
list_out = []

for i in range(number):
    list_in.append(randint(0, 9))

len_count = len(list_in)
len_count = len_count//2

list_cut = list_in [0:len(list_in)-len_count:1]
list_cut_rev = list_in [-1:-(len(list_in)+1-2):-1]
list_out = list(map(lambda x, y: x*y, list_cut, list_cut_rev))

print (list_in)
print (list_out)