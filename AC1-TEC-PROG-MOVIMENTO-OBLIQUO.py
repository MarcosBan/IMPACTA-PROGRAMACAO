"""
AC01-TEC-PROGRAMAÇÕES-RC1
Programa para calculo de altura máxima que pode ser alcançada por um objeto considerando: Angulo, Vellocidade Inicial e gravidade

Autor: Marcos Silva (1902671)
Data: 22/03/2020
"""
import math

anguloGraus = float(input("Informe o angulo em graus: "))
velocidaInicial = float(input("Informe a velocidade incial: "))
gravidade = float(input("Informe a gravidade: ))

graus = math.radians(anguloGraus)
potenVelocidade = math.pow(velocidaInicial,2)
senoGraus = math.sin(graus)
potenSenoGraus = math.pow(senoGraus,2)
gravidadeReal = 2*gravidade
alturaMaxima = potenVelocidade*potenSenoGraus/gravidadeReal

print("A altura maxima alcançada pelo objeto sera ", alturaMaxima)

input("Pressione qualquer tecla para sair")
