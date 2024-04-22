import modulo

lista = [1, 2, 3, 4, 5, 6, 6, 7, 9, 8]
item = int(input("Digite o Indíce do item: "))
(lista, numero) = modulo.popar(lista, item)
print(f'Item removido: {numero}, Nova Lista: {lista}')