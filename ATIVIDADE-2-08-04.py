#Atividade 2 - 08/04 - Marcos Silva 1902671
dividendo = int(input())
divisor = int(input())
contagem = divisor
quociente = 0
while contagem >= 0:
    print(dividendo)
    dividendo = dividendo - divisor
    resto = dividendo % divisor
    quociente = quociente + 1
    contagem = contagem - 1
print("Resultado = ",quociente)
print("Resto = ", resto)