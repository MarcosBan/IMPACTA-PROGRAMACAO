"""
AC03-TEC-PROGRAMAÇÕES-RC1
Programa para informar contar numeros naturais de 0 a 99.

Autor: Marcos Silva (1902671)
Data: 21/04/2020

"""
primeiroNum = int(input())
segundoNum = int(input())

testeImpar1 = primeiroNum % 2
testeImpar2 = segundoNum % 2

if testeImpar1 == 1 and testeImpar2 == 0:
    for primeiroNum in range(primeiroNum,segundoNum,2):
        print(primeiroNum)
        primeiroNum = primeiroNum + 1
elif testeImpar1 == 0 and testeImpar2 == 1:
    for primeiroNum in range(primeiroNum,segundoNum + 1,2):
        primeiroNum = primeiroNum + 1
        print(primeiroNum)
elif testeImpar1 == 0 and testeImpar2 == 0:
    for primeiroNum in range(primeiroNum,segundoNum,2):
        primeiroNum = primeiroNum + 1
        print(primeiroNum)
elif testeImpar1 == 1 and testeImpar2 == 1:
    for primeiroNum in range(primeiroNum,segundoNum + 1,2):
        print(primeiroNum)
        primeiroNum = primeiroNum + 1

