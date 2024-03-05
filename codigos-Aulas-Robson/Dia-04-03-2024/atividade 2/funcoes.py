## Primeiro:

def numVerdFalso(num):
    if num >= 0:
        return True
    else:
        return False
    
## Segundo:

def numVerdFalso2(num):
    if num >= 0:
        return f"O Valor {num} é Positivo! "
    else:
        return f"O Valor {num} é Negativo! "
    
## Terceiro:

def valorImparPar(num):
    if num % 2 == 0:
        return f'O Número {num} é Par'
    else:
        return f'O Número {num} é Impar'

## Quarto:

def mediasAluno(nota1, nota2, nota3, tipoMedia):
    if tipoMedia == 'A' or tipoMedia == 'A':
        media = (nota1 + nota2 + nota3) / 3
    elif tipoMedia == 'P' or tipoMedia == 'p':
        media = ((nota1 * 5) + (nota2 * 3) + (nota3 * 2)) / (5 + 3 + 2)
    return media

## Quinta:

def idadeEmDias(anos, meses, dias):
    calculo = (anos * 360) + (meses * 30)
    totalDias = calculo + dias
    return totalDias

## Sexta:

def ordenarNumeros(numero1, numero2, numero3):
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

## Sétima:

def horas (segundos):
    minutos, segundos = divmod(segundos, 60)
    horas, minutos = divmod(minutos, 60)
    return f'{horas}:{minutos}:{segundos}'

## Oitavo:

def numero(valor):
    if valor <= 1:
        return False
    
    soma_divisores = 1

    for i in range(2, int(valor**0.5) + 1):
        if valor % i == 0:
            soma_divisores += i
            if i != valor // i:
                soma_divisores += valor // i

    return soma_divisores == valor

## Nono:

def peso_ideal (altura, sexo):
    if sexo == 'masculino':
        ideal = (72.7*altura) - 58
    elif sexo == 'feminino':
        ideal = (62.1*altura) - 44.7
    return f'O seu peso ideal e: {ideal}'

## Décimo:

def triangulo (ladoA, ladoB, ladoC):
    if ladoA + ladoB > ladoC and ladoA + ladoC > ladoB and ladoB + ladoC > ladoA:
        if ladoA == ladoB == ladoC:
            resultado = 'Equilátero'
        elif ladoA == ladoB or ladoB == ladoC or ladoC == ladoA:
            resultado = 'Isósceles'
        else:
            resultado = 'Escaleno'
    else:
        resultado = 'Não e um triangulo'
    
    return resultado            