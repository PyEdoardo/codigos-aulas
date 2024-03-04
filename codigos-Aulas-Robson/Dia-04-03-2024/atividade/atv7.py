def horas (segundos):
    minutos, segundos = divmod(segundos, 60)
    horas, minutos = divmod(minutos, 60)
    return f'{horas}:{minutos}:{segundos}'

seg = int(input('Digite uma hora em segundos: '))
print(horas(seg))