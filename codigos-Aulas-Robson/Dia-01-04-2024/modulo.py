#Módulos da Atividade

def contar(num, lista):
    contar = 0
    for i in lista:
        if i == num:
            contar += 1
    return contar

def estender(lista, nova_lista):
    for i in nova_lista:
        lista.append(i)

def inserir(lista, indice, num):
    lista[indice:indice] = [num]

def remover(lista, num):
    nova_lista = []
    for i in lista:
        if i != num:
            nova_lista.append(i)
    return nova_lista        

def popar(lista, num=-1):
    removido = num
    pop_lista = []
    
    return removido

def indexar(lista, num):
    for i in range(len(lista)):
        if lista[i] == num:
            return i
    
def sortear(lista):
    for i in range(len(lista)):
        menor_index = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[menor_index]:
                menor_index = j
        lista[i], lista[menor_index] = lista[menor_index], lista[i]

def reverso(lista):  
    lista[:] = lista[::-1]
    return lista