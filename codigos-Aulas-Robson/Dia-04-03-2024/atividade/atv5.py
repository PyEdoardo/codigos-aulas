def idade(anos, meses, dias):
    calculo = (anos * 360) + (meses * 30)
    totalDias = calculo + dias
    return totalDias

qtAnos = int(input("Digite a Quantidade de Anos: "))

qtMeses = int(input("Digite a Quantidade de Meses: "))

qtDias = int(input("Digite a Quantidade de Dias: "))

print(f'Quantidade de Dias: {idade(qtAnos, qtMeses, qtDias)}')