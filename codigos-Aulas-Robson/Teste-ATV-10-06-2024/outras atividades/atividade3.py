palavras = {

}

while True:
    deseja = input('Deseja inserir palavras? (sim para continuar e não para parar.): ')
    if deseja == 'não' or deseja == 'nao' or deseja == 'n' or deseja == 'Nao' or deseja == 'Não':
        break
    palavraIng = input('Digite a palavra em inglês: ')
    palavraPT = input('Digite a palavra em portugês: ')
    palavras[palavraIng] = palavraPT

while True:
    procurarIng = input('Qual palavra em inglês deseja procurar (0 para encerrar): ')
    if procurarIng == '0':
        break
    if procurarIng not in palavras:
        print("Palavra não encontrada!")
    else:
        print(f'Palavra em Inglês: {palavraIng} | Palavra em Português: {palavras.get(procurarIng)}')
