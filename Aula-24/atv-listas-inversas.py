listaNum = [10, 8, 11, 5, 4, 7]

cont = len(listaNum)-1

inv = []

while cont >= 0:
    inv.append(listaNum[cont])
    cont = cont - 1
print("Lista Normal: ", listaNum)
print("Lista Inversa: ", inv)    