# 1. Вычислить число c заданной точностью *d*    
#     *Пример:* 
#     - при d = 0.001, π = 3.141
    

import math
n = input("Введите заданную точность числа в виде десятичной дроби  => ")
c = int(len(n)-2)
print(round(math.pi, c))


