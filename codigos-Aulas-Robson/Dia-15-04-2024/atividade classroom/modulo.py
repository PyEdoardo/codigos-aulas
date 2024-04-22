def interrogatorio():
    perguntas = [
        "Telefonou para a vítima?",
        "Esteve no local do crime?",
        "Mora perto da vítima?",
        "Devia para a vítima?",
        "Já trabalhou com a vítima?"
    ]

    respostas_positivas = 0
    for pergunta in perguntas:
        resposta = input(pergunta + " (s/n): ")
        if resposta.lower() == "s":
            respostas_positivas += 1

    if respostas_positivas == 2:
        return "Suspeita"
    elif 3 <= respostas_positivas <= 4:
        return "Cúmplice"
    elif respostas_positivas == 5:
        return "Assassino"
    else:
        return "Inocente"

print(interrogatorio())

notas = []
nota = float(input("Digite uma nota ou -1 para encerrar: "))
while nota != -1:
    notas.append(nota)
    nota = float(input("Digite uma nota ou -1 para encerrar: "))

print(f"Quantidade de valores lidos: {len(notas)}" )
print(f"Valores na ordem informada: {notas}" )
print("Valores na ordem inversa:")
for nota in reversed(notas):
    print(nota)

soma = sum(notas)
media = soma / len(notas) if notas else 0
acima_media = len([nota for nota in notas if nota > media])
abaixo_sete = len([nota for nota in notas if nota < 7])

print("Soma dos valores:", soma)
print("Média dos valores:", media)
print("Quantidade de valores acima da média:", acima_media)
print("Quantidade de valores abaixo de sete:", abaixo_sete)
print("Programa encerrado.")


def calcula_salarios():
    intervalos = [0] * 9
    while True:
        vendas_brutas = float(input("Digite o valor das vendas brutas do vendedor (ou -1 para encerrar): "))
        if vendas_brutas == -1:
            break

        salario = 200 + 0.09 * vendas_brutas
        if salario < 300:
            intervalos[0] += 1
        elif salario < 400:
            intervalos[1] += 1
        elif salario < 500:
            intervalos[2] += 1
        elif salario < 600:
            intervalos[3] += 1
        elif salario < 700:
            intervalos[4] += 1
        elif salario < 800:
            intervalos[5] += 1
        elif salario < 900:
            intervalos[6] += 1
        elif salario < 1000:
            intervalos[7] += 1
        else:
            intervalos[8] += 1

    print("\nSalários:")
    print("$200 - $299:", intervalos[0])
    print("$300 - $399:", intervalos[1])
    print("$400 - $499:", intervalos[2])
    print("$500 - $599:", intervalos[3])
    print("$600 - $699:", intervalos[4])
    print("$700 - $799:", intervalos[5])
    print("$800 - $899:", intervalos[6])
    print("$900 - $999:", intervalos[7])
    print("$1000 em diante:", intervalos[8])

calcula_salarios()








def competicao_salto():
    while True:
        nome_atleta = input("Nome do atleta (ou 'fim' para encerrar): ")
        if nome_atleta.lower() == 'fim':
            break

        saltos = []
        for i in range(1, 6):
            salto = float(input(f"{i}º Salto: "))
            saltos.append(salto)

        media_saltos = sum(saltos) / len(saltos)

        print("\nResultado final:")
        print("Atleta:", nome_atleta)
        print("Saltos:", " - ".join(str(salto) for salto in saltos))
        print("Média dos saltos: %.1f m" % media_saltos)

competicao_salto()







def calcula_percentual(votos_jogador, total_votos):
    return (votos_jogador / total_votos) * 100 if total_votos > 0 else 0

def enquete_melhor_jogador():
    votos = [0] * 23
    total_votos = 0

    while True:
        numero_jogador = int(input("Número do jogador (0=fim): "))
        if numero_jogador == 0:
            break
        elif 1 <= numero_jogador <= 23:
            votos[numero_jogador - 1] += 1
            total_votos += 1
        else:
            print("Informe um valor entre 1 e 23 ou 0 para sair!")

    print("\nResultado da votação:")
    print("Foram computados", total_votos, "votos.")

    mais_votado = max(votos)
    for i, v in enumerate(votos):
        if v > 0:
            percentual = calcula_percentual(v, total_votos)
            print("Jogador %d: %d votos, %.1f%%" % (i + 1, v, percentual))

    melhor_jogador = votos.index(mais_votado) + 1
    percentual_melhor_jogador = calcula_percentual(mais_votado, total_votos)
    print("\nO melhor jogador foi o número %d, com %d votos, correspondendo a %.1f%% do total de votos." % (melhor_jogador, mais_votado, percentual_melhor_jogador))

enquete_melhor_jogador()





def enquete():
    sistemas = ['Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro']
    votos = [0, 0, 0, 0, 0, 0]
    total_votos = 0

    while True:
        voto = int(input("Qual o melhor Sistema Operacional para uso em servidores? (0-6, 0 para encerrar): "))
        if voto == 0:
            break
        elif 1 <= voto <= 6:
            votos[voto - 1] += 1
            total_votos += 1
        else:
            print("Valor inválido.")

    print("\nSistema Operacional     Votos     %")
    print("-------------------     -----     ---")
    for i in range(6):
        percentual = votos[i] / total_votos * 100
        print(f"{sistemas[i]:<20} {votos[i]:<7} {percentual:.2f}%")

    print("-------------------     -----")
    print(f"Total{total_votos:>20}")

    mais_votado = max(votos)
    indice_mais_votado = votos.index(mais_votado)
    percentual_mais_votado = mais_votado / total_votos * 100
    print(f"\nO Sistema Operacional mais votado foi o {sistemas[indice_mais_votado]}, com {mais_votado} votos, correspondendo a {percentual_mais_votado:.2f}% dos votos.")

enquete()
