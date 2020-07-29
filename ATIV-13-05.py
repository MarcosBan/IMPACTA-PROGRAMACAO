#Atividade - 13/05 - Marcos Silva 1902671
def conta_pares(lst):
    tamanho = len(lst)
    indice = 0
    num_par = 0
    while indice < tamanho:
        if lst[indice] % 2 == 0:
           num_par += 1
        indice += 1
    )
    return num_par
qtd_lista = int(input("Informe a quantidade de numeros para lista: "))
lista = []
for i in range(0,qtd_lista):#Criando lista de zeros.
    lista.insert(i,0)
    i += 1
print(lista)
for i in range(0,qtd_lista):#Criando
    num = int(input("Valor: "))
    lista[i] = num
    i += 1
print(lista)
pares = conta_pares(lista)
print("A quantidade de pares é: ", pares)

####################EXERCICIO 2 ERRO################
def soma_dos_elementos(lst):
    tamanho = len(lst)
    indice = 0
    soma = 0
    while indice <= tamanho:
        soma = soma + lst[indice]
        indice += 1
    return soma

qtd_lista = int(input("Informe a quantidade de numeros para lista: "))
lista = []
for i in range(0,qtd_lista):#Criando
    num = int(input("Valor: "))
    lista.append(num)
    i += 1
print(lista)
somado = soma_dos_elementos(lista)
print("A soma dos elementos é: ", somado)

