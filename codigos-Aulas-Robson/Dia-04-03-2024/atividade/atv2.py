def numBool(num):
    if num >= 0:
        return f"O Valor {num} é Positivo! "
    else:
        return f"O Valor {num} é Negativo! "

numero = float(input("Digite o Número: "))
print(numBool(numero))