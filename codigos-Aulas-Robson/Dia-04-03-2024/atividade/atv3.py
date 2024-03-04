def valorImparPar(num):
    if num % 2 == 0:
        return f'O Número {num} é Par'
    else:
        return f'O Número {num} é Impar'

numero = int(input("Digite um Valor Inteiro: "))

print(valorImparPar(numero))