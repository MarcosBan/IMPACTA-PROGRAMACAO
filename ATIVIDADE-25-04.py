#Atividade - 25/04 - Marcos Silva 1902671
def soma_multi(n, modo):
    if modo == 1:
        ntotal = n + 11
        for contagem in range (n,ntotal):
            print(n)
            n = n + 1
    elif modo == 2:
        tab = 0
        while tab <= 10:
            multi = n * tab
            tab = tab + 1
            print(multi)
    else:
        print("Modo inválido!!")

numero = int(input("Informe o numero: "))
modo = int(input("Informe o modo de operação: "))

soma_multi(numero, modo)