"""
AC05-TEC-PROGRAMAÇÕES-RC1
Programa para identificar numeros impares e pares, e trazer a media dos valores.

Autor: Marcos Silva (1902671)
Data: 19/05/2020

"""
def media_pares_impares(lista):
    tam = len(lista)
    cont_indice = 0
    soma_par = 0
    soma_impar = 0
    cont_par = 0
    cont_impar = 0
    while cont_indice < tam:
        val_indice = lista[cont_indice]
        cont_indice += 1
        if val_indice % 2 == 0:
            soma_par += val_indice
            cont_par += 1
        else:
            soma_impar += val_indice
            cont_impar += 1
    media_par = soma_par / cont_par
    media_impar = soma_impar / cont_impar
    print(media_par)
    print(media_impar)


lista = eval(input())
media_pares_impares(lista)

