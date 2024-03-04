def ordenar(numero1, numero2, numero3):
    menor = numero1
    if numero2 < menor:
        menor = numero2
    if numero3 < menor:
        menor = numero3

    maior = numero1
    if numero2 > maior:
        maior = numero2
    if numero3 > maior:
        maior = numero3

    meio = numero1 + numero2 + numero3 - menor - maior    
    return f'{menor}, {meio}, {maior}'

num1 = int(input("Digite o 1 Inteiro:\n "))
num2 = int(input("Digite o 2 Inteiro:\n "))
num3 = int(input("Digite o 3 Inteiro:\n "))

print(ordenar(num1, num2, num3))