import math # корень (sqrt, cbrt), округление (ceil, floor, trunc), ц из н по к(comd, perm), модуль (fabs), факториал (factorial), нормальная сумма (fsum), проверка на число (isfinite), логарифм (log), степень (pow or **), тригонометрия, гиперболические фун-ции, константы

print("0.1+0.2 with math.fsum"+str(math.fsum([0.1,0.2])))
print("sqrt(10): "+str(math.sqrt(10))) 
# print("sqrt(-1): "+str(math.sqrt(-1))) # math domain error

import cmath # библиотека отсветсвенная за комплексные числа

print(cmath.sqrt(-1)) # returns complex number
