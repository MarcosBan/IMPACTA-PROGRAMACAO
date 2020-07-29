#Atividade - 29/04 - Marcos Silva 1902671


def imprime_lista(lista):
    qtd_itens = len(lst)
    i = 0
    while i < qtd_itens:
        print(i, "-", lista[i])
        i = i + 1

lst = ['cereal', 'banana', 'maçã', 'melão','iogurte']

imprime_lista(lst)
tam = len(lst)
print("A quantidade de itens na lista é, ", tam)
print("O elemento no indice 3 é", lst[3])

inserir = input("Insira um item a lista: ")
lst.append(inserir)
imprime_lista(lst)
del lst[2]
print("Removento indice 2")

imprime_lista(lst)
