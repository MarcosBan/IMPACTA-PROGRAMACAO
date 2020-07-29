"""
AC01-TEC-PROGRAMAÇÕES-RC1
Programa para cadastro de pessoas soma de idades.

Autor: Marcos Silva (1902671)
Data: 22/03/2020

"""
import math

primeiraPessoa = input()
primeiraIdade = float(input())
segundaPessoa = input()
segundaIdade = float(input())
terceiraPessoa = input()
terceiraIdade = float(input())
quartaPessoa = input()
quartaIdade = float(input())
quintaPessoa = input()
quintaIdade = float(input())

# Validação dos dados inserido / conversão para positivos

validPriIdade= int(math.fabs(primeiraIdade))
validSecIdade= int(math.fabs(segundaIdade))
validTerIdade= int(math.fabs(terceiraIdade))
validQuaIdade= int(math.fabs(quartaIdade))
validQuiIdade= int(math.fabs(quintaIdade))

somaIdades = int(validPriIdade + validSecIdade + validTerIdade + validQuaIdade + validQuiIdade)

# MEDIA ARITMETICA

mediaArit = somaIdades/5
multIdades = (validPriIdade * validSecIdade * validTerIdade * validQuaIdade * validQuiIdade)

# MEDIA GEOMETRICA

mediaGeo = (multIdades**(1/5))
fimMediaGeo = math.trunc(mediaGeo)
print("Pessoa:",primeiraPessoa, "," ,validPriIdade)
print("Pessoa:",segundaPessoa, ",",validSecIdade)
print("Pessoa:",terceiraPessoa,"," ,validTerIdade)
print("Pessoa:",quartaPessoa, "," ,validQuaIdade)
print("Pessoa:",quintaPessoa, "," ,validQuiIdade)
print(somaIdades)
print(mediaArit)
print(fimMediaGeo)