"""
AC03-TEC-PROGRAMAÇÕES-RC1
Programa para calculo de juros simples e juros compostos.

Autor: Marcos Silva (1902671)
Data: 06/05/2020

"""
import math
# funcao juros_simples(c, i, t)
def juros_simples(c, i, t):
    montante_final = c + (c * i * t)
    return montante_final

# juros_compostos(c, i, t):
def juros_compostos(c, i, t):
    calc_i = 1 + i
    pow_i = math.pow(calc_i, t)
    montante_final = c * pow_i
    return montante_final

# Programa principal (ja implementado, voce nao precisa se preocupar com o codigo a partir deste ponto)
opcao = input()
capital = float(input())
taxa = float(input())
tempo = float(input())
if opcao == 'simples':
	montante_final = juros_simples(capital, taxa, tempo)
elif opcao == 'composto':
	montante_final = juros_compostos(capital, taxa, tempo)
print("{0:.2f}".format(montante_final))