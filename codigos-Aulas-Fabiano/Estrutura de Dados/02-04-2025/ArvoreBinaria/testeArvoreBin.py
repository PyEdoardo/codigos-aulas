import ArvoreBin

a = ArvoreBin.ArvoreBin()
valores = [10, 230, 20, 30, 10, 1, 0, 2, 50]

for valor in valores:
    a.inserir(valor)

a.exibir_grafico()