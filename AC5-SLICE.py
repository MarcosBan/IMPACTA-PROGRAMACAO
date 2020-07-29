"""
AC05-TEC-PROGRAMAÇÕES-RC1
Programa para concatenar strings.
Autor: Marcos Pereira Silva (1902671)
Data: 21/05/2020

"""

string = input()
i1 = int(input())
f1 = int(input())
i2 = int(input())
f2 = int(input())

f1 += 1
f2 += 1
slice = string[i1:f1]
slice2 = string[i2:f2]

print(slice + slice2)
