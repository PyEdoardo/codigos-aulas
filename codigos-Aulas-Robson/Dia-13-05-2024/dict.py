pessoas_lista = [
    ['Fulano', 22],
    ['Ciclano', 33]
]

pessoas_dict = {
    1 : {"nome" : "Fulano", "idade" : 22},
    2 : {"nome" : "Ciclano", "idade" : 33},
    3 : {"nome" : "Fulano", "idade" : 50}
}

#print(pessoas_lista)
#print('\n')
#print(pessoas_dict[2])

chaveParaPesquisar = int(input('Digite o Valor: '))

pessoa = pessoas_dict.get(chaveParaPesquisar)
if pessoa == None:
    print("O código pesquisado não existe!")
else:
    print("O código pesquisado pertence a: ", pessoas_dict["nome"])
    