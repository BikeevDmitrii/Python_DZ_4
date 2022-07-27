# 4. Задана натуральная степень k. Сформировать случайным образом список 
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#     *Пример:* 
#     - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

k = int(input("Задайте коофициент k в диапазоне от 1 до 9 => "))
kooficient = ["(1)", "(x)", "(x**2)", "(x**3)", "(x**4)", "(x**5)", "(x**6)", "(x**7)", "(x**8)", "(x**9)", "(x**10)" ]
kooficient = kooficient[:k+1]

from random import randint
spisok_2 = [randint(0,100) for i in range(k+1)]

spisok_3 = list(zip(spisok_2, kooficient))

import functools
spisok_end = functools.reduce(lambda x,y: y+x, spisok_3)

with open('4.txt', 'w') as data:
    if k== 1:
        print(f'{spisok_end[0]}*{spisok_end[1]} + {spisok_end[2]}*{spisok_end[3]} = 0')
        data.write(f'{spisok_end[0]}*{spisok_end[1]} + {spisok_end[2]}*{spisok_end[3]} = 0')
    elif k== 2:
        print(f'{spisok_end[0]}*{spisok_end[1]} + {spisok_end[2]}*{spisok_end[3]} + {spisok_end[4]}*{spisok_end[5]} = 0')
        data.write(f'{spisok_end[0]}*{spisok_end[1]} + {spisok_end[2]}*{spisok_end[3]} + {spisok_end[4]}*{spisok_end[5]} = 0')
    elif k== 3:
        print(f'{spisok_end[0]}*{spisok_end[1]} + {spisok_end[2]}*{spisok_end[3]} + {spisok_end[4]}*{spisok_end[5]} + {spisok_end[6]}*{spisok_end[7]} = 0')
        data.write(f'{spisok_end[0]}*{spisok_end[1]} + {spisok_end[2]}*{spisok_end[3]} + {spisok_end[4]}*{spisok_end[5]} + {spisok_end[6]}*{spisok_end[7]} = 0')
    elif k== 4:
        print(f'{spisok_end[0]}*{spisok_end[1]} + {spisok_end[2]}*{spisok_end[3]} + {spisok_end[4]}*{spisok_end[5]} + {spisok_end[6]}*{spisok_end[7]} + {spisok_end[8]}*{spisok_end[9]} = 0')      
        data.write(f'{spisok_end[0]}*{spisok_end[1]} + {spisok_end[2]}*{spisok_end[3]} + {spisok_end[4]}*{spisok_end[5]} + {spisok_end[6]}*{spisok_end[7]} + {spisok_end[8]}*{spisok_end[9]} = 0')      
    elif k== 5:
        print(f'{spisok_end[0]}*{spisok_end[1]} + {spisok_end[2]}*{spisok_end[3]} + {spisok_end[4]}*{spisok_end[5]} + {spisok_end[6]}*{spisok_end[7]} + {spisok_end[8]}*{spisok_end[9]} + {spisok_end[10]}*{spisok_end[11]} = 0')
        data.write(f'{spisok_end[0]}*{spisok_end[1]} + {spisok_end[2]}*{spisok_end[3]} + {spisok_end[4]}*{spisok_end[5]} + {spisok_end[6]}*{spisok_end[7]} + {spisok_end[8]}*{spisok_end[9]} + {spisok_end[10]}*{spisok_end[11]} = 0')
    elif k== 6:
        print(f'{spisok_end[0]}*{spisok_end[1]} + {spisok_end[2]}*{spisok_end[3]} + {spisok_end[4]}*{spisok_end[5]} + {spisok_end[6]}*{spisok_end[7]} + {spisok_end[8]}*{spisok_end[9]} + {spisok_end[10]}*{spisok_end[11]} +{spisok_end[12]}*{spisok_end[13]} = 0')
        data.write(f'{spisok_end[0]}*{spisok_end[1]} + {spisok_end[2]}*{spisok_end[3]} + {spisok_end[4]}*{spisok_end[5]} + {spisok_end[6]}*{spisok_end[7]} + {spisok_end[8]}*{spisok_end[9]} + {spisok_end[10]}*{spisok_end[11]} +{spisok_end[12]}*{spisok_end[13]} = 0')
    elif k== 7:
        print(f'{spisok_end[0]}*{spisok_end[1]} + {spisok_end[2]}*{spisok_end[3]} + {spisok_end[4]}*{spisok_end[5]} + {spisok_end[6]}*{spisok_end[7]} + {spisok_end[8]}*{spisok_end[9]} + {spisok_end[10]}*{spisok_end[11]} + {spisok_end[12]}*{spisok_end[13]} + {spisok_end[14]}*{spisok_end[15]} = 0')
        data.write(f'{spisok_end[0]}*{spisok_end[1]} + {spisok_end[2]}*{spisok_end[3]} + {spisok_end[4]}*{spisok_end[5]} + {spisok_end[6]}*{spisok_end[7]} + {spisok_end[8]}*{spisok_end[9]} + {spisok_end[10]}*{spisok_end[11]} + {spisok_end[12]}*{spisok_end[13]} + {spisok_end[14]}*{spisok_end[15]} = 0')
    elif k== 8:
        print(f'{spisok_end[0]}*{spisok_end[1]} + {spisok_end[2]}*{spisok_end[3]} + {spisok_end[4]}*{spisok_end[5]} + {spisok_end[6]}*{spisok_end[7]} + {spisok_end[8]}*{spisok_end[9]} + {spisok_end[10]}*{spisok_end[11]} + {spisok_end[12]}*{spisok_end[13]} + {spisok_end[14]}*{spisok_end[15]} + {spisok_end[16]}*{spisok_end[17]} = 0 ')
        data.write(f'{spisok_end[0]}*{spisok_end[1]} + {spisok_end[2]}*{spisok_end[3]} + {spisok_end[4]}*{spisok_end[5]} + {spisok_end[6]}*{spisok_end[7]} + {spisok_end[8]}*{spisok_end[9]} + {spisok_end[10]}*{spisok_end[11]} + {spisok_end[12]}*{spisok_end[13]} + {spisok_end[14]}*{spisok_end[15]} + {spisok_end[16]}*{spisok_end[17]} = 0 ')
    elif k== 9:
        print(f'{spisok_end[0]}*{spisok_end[1]} + {spisok_end[2]}*{spisok_end[3]} + {spisok_end[4]}*{spisok_end[5]} + {spisok_end[6]}*{spisok_end[7]} + {spisok_end[8]}*{spisok_end[9]} + {spisok_end[10]}*{spisok_end[11]} + {spisok_end[12]}*{spisok_end[13]} + {spisok_end[14]}*{spisok_end[15]} + {spisok_end[16]}*{spisok_end[17]} + {spisok_end[18]}*{spisok_end[19]} = 0 ')
        data.write(f'{spisok_end[0]}*{spisok_end[1]} + {spisok_end[2]}*{spisok_end[3]} + {spisok_end[4]}*{spisok_end[5]} + {spisok_end[6]}*{spisok_end[7]} + {spisok_end[8]}*{spisok_end[9]} + {spisok_end[10]}*{spisok_end[11]} + {spisok_end[12]}*{spisok_end[13]} + {spisok_end[14]}*{spisok_end[15]} + {spisok_end[16]}*{spisok_end[17]} + {spisok_end[18]}*{spisok_end[19]} = 0 ')
data.close()








