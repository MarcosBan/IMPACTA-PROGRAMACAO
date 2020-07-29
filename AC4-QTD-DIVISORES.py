"""
AC03-TEC-PROGRAMAÇÕES-RC1
Programa para identificar quantidade de divisores.

Autor: Marcos Silva (1902671)
Data: 06/05/2020

"""

def checa_quantidade_divisores(n, qtd):
    contador = 1
    divisor = 0
    while contador <= n:
        dividiu = n % contador
        contador = contador + 1
        if dividiu == 0:
            divisor = divisor + 1
            continue
    if divisor == qtd:
        return True
    else:
        return False

# Programa principal (ja implementado, voce nao precisa se preocupar com o codigo partir deste ponto)
n = int(input())
qtd = int(input())
if checa_quantidade_divisores(n, qtd): # se a funcao devolve True, entao...
	print(n, "possui", qtd, "divisores")
else:
	print(n, "nao possui", qtd, "divisores",)

