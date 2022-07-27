# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

path = '3.txt'
with open(path, 'r') as my_file:
    spisok_1 = my_file.read()
spisok_1 = spisok_1.split(', ')
print(spisok_1)

spisok_2 = []

for item in spisok_1:
    count = 0
    for x in spisok_1:
        if x == item:
            count += 1
    spisok_2.append(count)

spisok_3 = []

for i in range(0, len(spisok_1)):
    if spisok_2[i] < 2 :
        spisok_3.append(spisok_1[i])   
    i+= 1
    
print(spisok_3)
