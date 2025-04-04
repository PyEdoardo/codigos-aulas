import ArvoreBin

a = ArvoreBin.ArvoreBin()
valores = [50, 30, 70, 20, 40, 60, 80]

for valor in valores:
    a.inserir(valor)

a.exibir_grafico()