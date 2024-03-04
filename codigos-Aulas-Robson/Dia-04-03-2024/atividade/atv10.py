def triangulo (ladoA, ladoB, ladoC):
    if ladoA + ladoB > ladoC and ladoA + ladoC > ladoB and ladoB + ladoC > ladoA:
        if ladoA == ladoB == ladoC:
            resultado = 'Equilátero'
        elif ladoA == ladoB or ladoB == ladoC or ladoC == ladoA:
            resultado = 'Isósceles'
        else:
            resultado = 'Escaleno'
    else:
        resultado = 'Nao e um triangulo'
    
    return resultado

dadosA = float(input('Digite o valor do ladoA: '))
dadosB = float(input('Digite o valor do ladoB: '))
dadosC = float(input('Digite o valor do ladoC: '))

print(triangulo(dadosA, dadosB, dadosC))