"""
AC01-TEC-PROGRAMAÇÕES-RC1
Programa para cadastro de pessoas soma de idades.

Autor: Marcos Silva (1902671)
Data: 22/03/2020

"""
import math

primeiraPessoa = input()
primeiraIdade = int(input())
segundaPessoa = input()
segundaIdade = int(input())
terceiraPessoa = input()
terceiraIdade = int(input())
quartaPessoa = input()
quartaIdade = int(input())
quintaPessoa = input()
quintaIdade = int(input())

# Validação dos dados inserido / conversão para positivos

validPriIdade= math.fabs(primeiraIdade)
validSecIdade= math.fabs(segundaIdade)
validTerIdade= math.fabs(terceiraIdade)
validQuaIdade= math.fabs(quartaIdade)
validQuiIdade= math.fabs(quintaIdade)

potencPriIdade= math.pow(validPriIdade, 1)
potencSecIdade= math.pow(validSecIdade, 2)
potencTerIdade= math.pow(validTerIdade, 3)
potencQuaIdade= math.pow(validQuaIdade, 4)
potencQuiIdade= math.pow(validQuiIdade, 5)

somaPotenc = potencPriIdade + potencSecIdade + potencTerIdade + potencQuaIdade + potencQuiIdade
somaIdades = validPriIdade + validSecIdade + validTerIdade + validQuaIdade + validQuiIdade

# MEDIA ARITMETICA

mediaArit = somaIdades/5
multIdades = (validPriIdade * validSecIdade * validTerIdade * validQuaIdade * validQuiIdade)
# MEDIA GEOMETRICA

mediaGeo = (multIdades**(1/5))
fimMediaGeo = math.trunc(mediaGeo)
print("pessoa: ",primeiraPessoa, ", " ,validPriIdade)
print("pessoa: ",segundaPessoa, ", " ,validSecIdade)
print("pessoa: ",terceiraPessoa, ", " ,validTerIdade)
print("pessoa: ",quartaPessoa, ", " ,validQuaIdade)
print("pessoa: ",quintaPessoa, ", " ,validQuiIdade)
print(somaIdades)
print(mediaArit)
print(fimMediaGeo)