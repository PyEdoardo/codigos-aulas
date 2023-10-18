#listaaluno = ["Bruno", "Ana", "Bia", "Eva"] #Lista Básica de Strings em Python
#print(listaaluno) #Print dos elementos da lista

#num = [1,2,3,4,5] #Lista Básica de Inteiros
#print(num) #Print dos Inteiros

#lista_aluno = ["Ana", 8.4, "Bia", 10, "Eva", 5.5, "Edoardo", 10.50] #Lista com valores Strings e Float
#print("Tamanho da Lista: ", len(lista_aluno)) #Print usando função len, para mostrar a quantidade de elementos da lista
#cont = len(lista_aluno) #Flag do While usando os elementos da lista
#print(cont)

#nome = input("Nome: ")
#nomes = ["Ana", "Victor", "Bia"]

#if nome in nomes: #If básico para saber se existe a string da variável nome, dentro da lista nomes
    #print("Existe na Lista")
#else:
    #print("Não Existe! ")



#nomes = ["Ana", "Victor", "Bia"] #Usando [] para mostrar apenas alguns valores da Lista
#print("Nome: ", nomes[0]) #o [] com número 0 mostra apenas o nome Ana
#print("Nome: ", nomes[1])
#print("Nome: ", nomes[2])

#nomes = ["Ana", "Victor", "Bia"]
#cont = 0
#while cont < len(nomes): #Usando While para verificar cada nome por vez
#    print("Posição: ", cont, "Nome: ", nomes[cont]) #Usando a Flag para olhar algum elemento específico da lista
#    cont = cont + 1 #Para não ficar em loop


#nomes = []
#print("Tamanho: ", len(nomes), nomes)
#nomes.append("Ana")
#print("Tamanho: ", len(nomes), nomes)
#nomes.append("Bia")
#print("Tamanho: ", len(nomes), nomes)
#nomes.append("Edoardo")
#print("Tamanho: ", len(nomes), nomes)

#lista_nomes = ["Ana", "Bia", "Eva"]
#print(lista_nomes)
#lista_nomes[1] = "Sara"
#print(lista_nomes)


#nomes = []
#cont = 0
#while cont < 4:
#    nomes.append(input("Digite o Nome: "))
#    print("Tamanho da Lista: ", len(nomes), nomes)
#    cont = cont + 1


#1 Atividade
#numeros = []

#flag = 0
#while flag != 0:
#    var_num = int(input("Digite o Número Inteiro: "))
#    numeros.append(var_num)
#    flag = flag + 1
#print("Elementos: ", )
#flag = 0
#while flag < len(numeros):
#    print(numeros[flag])
#    flag = flag + 1

#2 Atividade
#num = []
#flag = int(input("Digite o Número: "))

#while flag != 0:
#    num.append(flag)
#    flag = int(input("Digite o Número: "))
#print(num)
#i = 0
#while i < len(num):
#    print(num[i])
#    i = i + 1    

#3 Atividade
lista = [3,5,6,4,3,2,9,8,7,10,55,9939]
maior_elm = 0
i = 0
while i < len(lista):
    if lista[i] > maior_elm:
        maior_elm = lista[i]
    i = i + 1
print("Maior Número: ", maior_elm)
                                                                                                                                                                                                                                      
