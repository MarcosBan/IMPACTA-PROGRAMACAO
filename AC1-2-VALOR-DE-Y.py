"""
AC01-2-TEC-PROGRAMAÇÕES-RC1
Programa para encontrar o valor de Y.

Autor: Marcos Silva (1902671)
Data: 05/04/2020

"""
import math
valorX = float(input("Informe o valor de X: "))

#Valores necessários para primeira parte da formula
e = math.e
pi = math.pi
ePowPi = math.pow(e, pi) # e Elevado a pi
piPowE = math.pow(pi, e) # pi Elevado a e
xQuadrado = math.pow(valorX,2)
logX = math.log(xQuadrado, 3)
yPrimeiraEtapa = logX + e + ePowPi + piPowE

#Valores para seugnda parte da formula

multiX = 2 * valorX
ySegundaEtapa = math.sqrt(multiX)
valorY = yPrimeiraEtapa / ySegundaEtapa

print(valorY)