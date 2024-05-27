def lerNotas(nomeArquivo):
    arquivo = open(nomeArquivo, 'r')
    notasString = arquivo.read().strip().splitlines()
    arquivo.close()
    return notasString