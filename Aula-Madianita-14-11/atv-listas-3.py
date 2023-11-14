flores = []

continuar = 's'

while continuar == 's':
    flor = []
    flor.append(input("Digite o Nome da Flor: "))
    flor.append(float(input("Digite o Preço da Flor: ")))
    flores.append(flor)
    continuar = input("Deseja Continuar? (s ou n)")

print(f"\nFlores Cadastradas: ")

i = 0

while i < len(flores):
    print(f"\nFlor: {i} \nNome: {flores[i][0]} \nPreço da Unidade: {flores[i][1]} \n----------------")
    i = i + 1

print("\nRelatório Final: ")

i = 0
maior = 0
while i < len(flores):
    print(f"{i} -- {flores[i][0]} -- Valor do Buque: R${12*flores[i][1]}")
    if maior < flores[i][1]:
        maior = flores[i][1]
    i = i + 1

print(f"O Maior Valor é: {maior}, e as flores que têm esse valor são: ")
i = 0
while i < len(flores):
    if maior == flores[i][1]:
        print(flores[i[0]])


