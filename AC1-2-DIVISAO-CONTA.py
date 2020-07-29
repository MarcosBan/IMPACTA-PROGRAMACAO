"""
AC01-2-TEC-PROGRAMAÇÕES-RC1
Programa para divisão de contas a pagar.

Autor: Marcos Silva (1902671)
Data: 05/04/2020

"""

pessoaUm = input('Insira o nome da primeira pessoa: ')
pessoaDois = input('Insira o nome da segunda pessoa: ')
pessoaTres = input('Insira o nome da terceira pessoa: ')
contaValor = float(input('Insira o valor total da conta: '))

divisaoConta = float(contaValor // 3)
diferençaConta = round(contaValor - (divisaoConta+divisaoConta), 2)

print(pessoaUm, "R$:", diferençaConta)
print(pessoaDois, "R$:", divisaoConta)
print(pessoaTres, "R$:", divisaoConta)