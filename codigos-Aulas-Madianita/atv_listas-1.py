pessoas = [['Ana Maria', 10],
          ['Pedro', 20],
          ['Carlos', 8],
          ['Carla', 18]]

i = 0

while i < len(pessoas):
    print(pessoas[i])
    i = i + 1
cont = 's'

while cont == 's':
    pessoa = []
    pessoa.append(input("Nome: "))
    pessoa.append(input(int("Idade: ")))
    pessoas.append(pessoa)
    cont = input("Deseja Continuar? ")
i = 0

while i < len(pessoas):
    print("Nome: ", pessoas[i][0], "Idade: ", pessoas[i][1])
    if pessoas[i][1] < 18:
        print("Maior de Idade! ")
    else:
        print("Menor de Idade! ")
    i = i + 1
nomePesq = input("\nNome da Pessoa que Quer Encontrar: ")

i = 0
existe = "n"
while i < len(pessoas):
    if pessoas[i][0] == nomePesq:
        print("A idade da pessoa é", pessoas[i][1])
        existe = 's'
    i = i + 1
if existe == 'n':
    print("A Pessoa não existe! ")
else:
    print("Ela exite! ")
                


