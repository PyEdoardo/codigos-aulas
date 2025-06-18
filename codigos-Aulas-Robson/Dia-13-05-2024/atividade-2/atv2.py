lista_objetos = input("Digite uma lista de objetos separados por vírgulas: ").split(', ')


contagem_objetos = {}

for objeto in lista_objetos:

    objeto = objeto.strip().lower()


    if objeto in contagem_objetos:
        contagem_objetos[objeto] += 1

    else:
        contagem_objetos[objeto] = 1


print("Quantidades de objetos cadastrados:")
for objeto, contagem in contagem_objetos.items():
    print(f"{objeto} - {contagem}")

print("Total de objetos:", sum(contagem_objetos.values()))