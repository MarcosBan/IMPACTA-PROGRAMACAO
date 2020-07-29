"""
Programa que interpreta o tipo do conteudo dentro da variavel.

Autor: Marcos Silva
Data: 11/03/2020
"""
#Comentario de uma unica linha.
FraseString = (input("Digite uma frase: "))
NumeroInt = int(input("Digite um numero: "))

TipoFrase = type(FraseString)
TipoNumero = type(NumeroInt)
"""
if TipoFrase == "<class 'str'>":
	TipoFrase = "Isso é string coroi"
else:
	print("Erro desconhecido")

if TipoNumero == "<class 'int'>":
	TipoNumero = "Isso é numero inteiro coroi"
else:
	print("Erro desconhecido")
"""
print("A primeira entrada é um dado tipo: ", TipoFrase)
print("A segunda entrada é um dado tipo: ", TipoNumero)
input("Pressione Enter para sair do programa")