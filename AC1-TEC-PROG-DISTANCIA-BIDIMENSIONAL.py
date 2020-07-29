"""
AC01-TEC-PROGRAMAÇÕES-RC1
Programa para calculo de distancia entre dois objetos em um espaço bidimensional

Autor: Marcos Silva (1902671)
Data: 22/03/2020
"""
import math

xPTA = float(input())
yPTA = float(input())
xPTB = float(input())
yPTB = float(input())

subtraixBA = xPTB - xPTA
subtraiyBA = yPTB - yPTA
potencxBA = math.pow(subtraixBA,2)
potencyBA = math.pow(subtraiyBA,2)
somaXY = potencxBA + potencyBA
distAB = math.sqrt(somaXY)

print(distAB)


