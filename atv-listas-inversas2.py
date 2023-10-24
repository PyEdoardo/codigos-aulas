listaPrecos = [15.00, 20.00, 10.00, 25.00, 30.00, 5.00]

listaProdutos = ['Boneca', 'Camisa', 'Caneca', 'Chaveiro', 'Caneta', 'Copo']

i = 5

while i >= 0:
    if listaPrecos[i-1] > listaPrecos[i]:
        print("Mais Caro: ", listaProdutos[i-1])
    else:
        print("Mais Caro: ", listaProdutos[i])
    i = i - 1            