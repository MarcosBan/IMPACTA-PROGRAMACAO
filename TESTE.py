cont = 0
somaCor = 0
qtdDias = 0
while cont <= 7:
	cont = cont + 1
	num = int(input())
	somaCor = somaCor + num
	if num >= 100:
		qtdDias = qtdDias + 1
media = somaCor // 7
print(int(media))
print(int(qtdDias))