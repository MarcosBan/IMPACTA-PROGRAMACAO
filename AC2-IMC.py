"""
AC02-TEC-PROGRAMAÇÕES-RC1
Programa para calcular o indice de massa corporal (IMC)

Autor: Marcos Silva (1902671)
Data: 06/04/2020

"""
def base_imc(altura, peso):
      if IMC < 17.00:
            print(IMC)
            print("Muito abaixo do peso")
      elif IMC >= 17.00 and IMC < 18.50:
            print(IMC)
            print("Abaixo do peso")
      elif IMC >= 18.50 and IMC < 25.00:
            print(IMC)
            print("Peso normal")
      elif IMC >= 25.00 and IMC < 30.00:
            print(IMC)
            print("Acima do peso")
      elif IMC >= 30.00 and IMC < 35.00:
            print(IMC)
            print("Obesidade grau I")
      elif IMC >= 35.00 and IMC < 40.00:
            print(IMC)
            print("Obesidade grau II")
      else:
            print(IMC)
            print("Obesidade grau III")

Altura = float(input())
Peso = float(input())

IMC = round(Peso/(Altura * Altura), 2)

base_imc(Altura, Peso)


