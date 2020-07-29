NUM = int(input("Informe um número: "))
divisor = 1
subNum = 0
for i in range(1, NUM+1):
    s = divisor/(NUM-subNum)
    divisor = divisor + 1
    subNum = subNum + 1
    somaS = s + s
    sFinal =  somaS + (NUM-1)/2 + NUM
print("Valor Final: ", sFinal)