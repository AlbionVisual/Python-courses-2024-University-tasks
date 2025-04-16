print("0.1+0.2"+str(0.1+0.2)) # считается некоректно, с погрешностью

'stroke'=="stroke" # но предпочтительнее первый вариант

print('here are some useless text \nhere are too...') # \ - работает

print(str(1)+'\n'+str(2)+' 3\n4 5 6')

a,b,c=1,2,3
# a,b,c=1,2. # a = 1, b = 2. but c = ? error
print ('a,b,c=1,2,3: ', str(a),str(b),str(c))

a,b = b,a
print('a,b = b,a: ',str(a),str(b))

# сравнивать можно не только числа, но и строки:
print("'2'> ' ': ", str('2'>' ')) # пустая строка всегда меньше любой другой

exp = True

if exp == True:
    print('when expresion true')
elif exp == False:
    print('when expresion false')
else:
    print('otherwise')

x = 1283
# you also can make it oneline:
sgn = 1 if x > 0 else -1 if x < 0 else 0

f = 0
while(f < 10):
    print(f)
    f += 1

for i in range(10, 2, -1):
    print(i)