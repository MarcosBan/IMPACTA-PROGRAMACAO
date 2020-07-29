"""
Programa que estipula conta de agua.

Autor: Marcos Silva
Data: 11/03/2020
"""
#Comentario de uma unica linha.
SalarioMin = float(input("Informe o salario minimo: "))
GastoMens = float(input("Informe o gasto mesal de agua em litros: "))
#Calculo de porcentagem A(Quantidade Porcentagem) * B / 100.

DoisPorcentoLitro = (2 * SalarioMin)/100
ValorConta = (DoisPorcentoLitro * GastoMens)/1000
ValorDesConto = ValorConta - (15 * ValorConta)/100  



print("Valor de 1000L é: ", DoisPorcentoLitro)
print("Valor da conta é: ", ValorConta)
print("Valor com desconto de 15% é: ", ValorDesConto)
input("Pressione Enter para sair do programa")
