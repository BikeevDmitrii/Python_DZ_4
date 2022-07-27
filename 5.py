# Задача №5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

path = '5_1.txt'
with open(path, 'r') as my_file:
    data = my_file.read()
data = data.split()
print(data)
data = [int(data[0][:-3]), int((data[1] + data[2])[:-1]), int(data[3] + data[4]), int(data[6]) ]

path = '5_2.txt'
with open(path, 'r') as my_file:
    data2 = my_file.read()
data2 = data2.split()
print(data2)
data2 = [int(data2[0][:-3]), int((data2[1] + data2[2])[:-1]), int(data2[3] + data2[4]), int(data2[6])]
data3= [int(data[0] + data2[0]), int(data[1] + data2[1]), int(data[2] + data2[2]),int(data[3] + data2[3])]

print(f'{data3[0]}x^2 + {data3[1]}x + {data3[2]} = {data3[3]}')

with open('5_3.txt', 'w') as data:
    data.write(f'{data3[0]}x^2 + {data3[1]}x + {data3[2]} = {data3[3]}')
data.close()
