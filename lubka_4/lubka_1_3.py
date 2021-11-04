"""
Дано чотири точки, що є вершинами чотирикутника A(x1,y1,z1),B(x2,y2,z2),C(x3,y3,z3),D(x4,y4,z4) .
З’ясувати, чи можуть вони бути вершинами прямокутника.

"""
# 0 позначення
'''
peak_A вершина 
peak_B вершина
peak_C вершина
peak_D вершина
X1,2,3;Y1,2,3;Z1,2,3-Змінні float 
vector_AB(i1,o1,p1) вектор
vector_BC(i2,o2,p2) вектор 
vector_СD(i3,o3,p3) вектор
vector_AD(i4,o4,p4) вектор 
'''
# введення
print('Введіть координати вершини А')
x1 = float(input('Введіть значення x1 :'))
y1 = float(input('Введіть значення y1 :'))
z1 = float(input('Введіть значення z1 :'))
print('Введіть координати вершини B')
x2 = float(input('Введіть значення x2 :'))
y2 = float(input('Введіть значення y2 :'))
z2 = float(input('Введіть значення z2 :'))
print('Введіть координати вершини C')
x3 = float(input('Введіть значення x3 :'))
y3 = float(input('Введіть значення y3 :'))
z3 = float(input('Введіть значення z3 :'))
print('Введіть координати вершини D')
x4 = float(input('Введіть значення x4 :'))
y4 = float(input('Введіть значення y4 :'))
z4 = float(input('Введіть значення z4 :'))
# Обраховуємо вектори
# vector_AB(i1,o1,p1)
i1 = x2-x1
o1 = y2-y1
p1 = z2-z1
# vector_BC(i2,o2,p2)
i2 = x3-x2
o2 = y3-y2
p2 = z3-z2
# vector_СD(i3,o3,p3)
i3 = x4-x3
o3 = y4-y3
p3 = z4-z3
# vector_AD(i4,o4,p4)
i4 = x4-x1
o4 = y4-y1
p4 = z4-z1
# перевіряємо чи вектори перпендикулярні
# vector_AB*vector_BC=i1*i2+o1*o2+p1*p2=0
if i1*i2+o1*o2+p1*p2 == 0:
    i3*i2+o3*o2+p3*p2 == 0
    i3*i4+o3*o4+p3*p4 == 0
    print('Точки  A, B, C, D можуть вони бути вершинами прямокутника.')
else: print('Точки  A, B, C, D НЕ можуть вони бути вершинами прямокутника.')
