import random
numeros = []

i = 0
while i < 10:
    numeros.append(random.randint(1,50))
    i = i + 1
print("Números: ", numeros)
i = 0
while i < 5:
    print(numeros[i])
    i = i + 1
soma = 0
i = 0
while i < len(numeros):
    if i % 2 == 0:
        soma = soma + numeros[i]
    i = i + 1
menor = 100
i = len(numeros)-1
while i >= len(numeros)-4:
    if numeros[i] < menor:
        menor = numeros[i]
    i = i - 1
print("Menores: ", menor)        
