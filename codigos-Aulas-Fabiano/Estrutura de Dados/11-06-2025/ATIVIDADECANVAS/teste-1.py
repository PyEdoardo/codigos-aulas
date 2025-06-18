import Tree

tree = Tree.Tree()
valores = [8, 3, 14, 6, 10, 5, 12, 4, 13, 15]
for valor in valores:
    tree.insere(valor)

print('Ancestrais de 4 a partir da raiz: 8 3 6 5')
tree.imprime_ancestrais(4)  
print('Ancestrais de 13 a partir da raiz: 8 14 10 12')
tree.imprime_ancestrais(13) 
print('Ancestrais de 5 a partir da raiz: 8 3 6')
tree.imprime_ancestrais(5)

print('Menores que 8 em ordem crescente: 3 4 5 6')
tree.imprime_menores(8)     
print('Menores que 13 em ordem crescente: 3 4 5 6 8 10 12')
tree.imprime_menores(13)


print('Irmão de 3: 14')
tree.imprime_irmao(3)       
print('Irmão de 6:  ')
tree.imprime_irmao(6)       # Saída esperada: Nada
print('Irmão de 15: 10')
tree.imprime_irmao(15)
print('Irmão de 8:  ')
tree.imprime_irmao(8)      # Saída esperada: Nada

print('Irmão de 3: 14')
print(tree.retorna_irmao(3))

print('Irmão de 6: None')
print(tree.retorna_irmao(6)) # Saída esperada: None
print('Irmão de 15: 10')
print(tree.retorna_irmao(15))
print('Irmão de 8: None')
print(tree.retorna_irmao(8)) # Saída esperada: None


print('Pai de 3: 8')
print(tree.retorna_pai(3))  
print('Pai de 6: 3')
print(tree.retorna_pai(6))  
print('Pai de 10: 14')
print(tree.retorna_pai(10))  

