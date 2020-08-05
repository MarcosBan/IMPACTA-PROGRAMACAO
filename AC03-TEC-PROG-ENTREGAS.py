"""
AC03-TEC-PROGRAMAÇÕES-RC1
Programa para informar media de entregas em 7 dias.

Autor: Marcos Silva (-)
Data: 21/04/2020

"""
diasMeta = 0
entreTotalDias = 0
for contDias in range (0,7):
    entreDias = int(input())display dlmalloc-memory
    entreTotalDias = entreTotalDias + entreDias
    mediaEntre = entreTotalDias // 7
    if entreDias >= 100:
        meta = entreDias
        metaTotal = meta + meta
        diasMeta = diasMeta + 1
    else:
        continue

print(diasMeta)
print(mediaEntre)
