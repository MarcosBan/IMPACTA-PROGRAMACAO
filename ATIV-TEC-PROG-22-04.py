#Atividade 2 - 22/04 - Marcos Silva 1902671
percentil = float(input("Informe o percentual: "))
valorReal = float(input("Informe o valor do produto: "))
teste = 0
while teste != 1:
    if percentil > 0 and percentil <=1:
        percentilFloat = percentil * 100
        novoValor = percentilFloat*valorReal/100
        print(novoValor)
        teste = 1
    elif percentil >= 10 and percentil <=100:
        novoValor = percentil*valorReal/100
        print(novoValor)
        teste = 1
    else:
        print("Valor percentual invalido!")
        percentil = float(input("Informe o percentual: "))
        teste = 0