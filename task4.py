#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
chetv=int(input('Введите четверть:'))

if (chetv==1):
    print('X > 0 и Y > 0')
if (chetv==2):
    print('X < 0 и Y > 0')
if (chetv==3):
    print('X < 0 и Y < 0')
if (chetv==4):
    print('X > 0 и Y < 0')