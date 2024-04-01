import modulo

lista = [1, 2, 3, 4, 5, 6, 6, 7, 9, 8]

# 1:
repete = int(input("Digite: "))
print(f'O Valor {repete} aparece {modulo.contar(repete, lista)} vezes')

# 2: 
lista2 = [1, 19, 40, 20]
print(f'Estender lista: {modulo.estender(lista, lista2)}')

# 3:
inserir = int(input("Digite um valor para inserir na lista: "))
indice = int(input("Digite o Indice de onde inserir o item: "))
print(f'Lista com item inserido: {modulo.inserir(lista, indice, inserir)}')

# 4:
item_remover = int(input("Digite o Valor a ser Removido da Lista"))
print(f'Item: {item_remover} removido da lista, resultado: \n{modulo.remover(lista, item_remover)}')

# 5:
indice_popado = int(input("Digite o indice para popar na Lista: "))
print(f'Lista: {lista}, Item Popado: {modulo.popar(lista, indice_popado)}')



