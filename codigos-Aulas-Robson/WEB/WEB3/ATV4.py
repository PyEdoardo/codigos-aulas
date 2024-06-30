def contaPalavra(texto):
    palavras = texto.split()
    contadores = {}

    for palavra in palavras:
        if palavra in contadores:
            contadores[palavra] += 1
        else:
            contadores[palavra] = 1

    for palavra, contagem in contadores.items():
        if contagem == 1:
            print(f'{palavra} appears {contagem} time.')
        else:
            print(f'{palavra} appears {contagem} times.')

texto = input("Digite o texto: ")
contaPalavra(texto)
