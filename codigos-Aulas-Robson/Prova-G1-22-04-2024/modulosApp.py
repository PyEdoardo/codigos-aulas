def valorTotalEstoque(produtos):
    i = 0
    estoque = 0
    while i < len(produtos):
        estoque = estoque + produtos[i][1]
        valorDoEstoque = estoque * produtos[i][2]
        i = i + 1
    return valorDoEstoque

def produtosInferiorADez(produtos):
    i = 0
    nomeItensMenorEstoque = []
    while i < len(produtos):
        if produtos[i][1] < 10:
            nomeItem = produtos[i][0]
            nomeItensMenorEstoque.append(nomeItem)
        i = i + 1
    if sum(nomeItensMenorEstoque) < 10:
        return 'Nenhum item ficou abaixo de 10'    
    return nomeItensMenorEstoque

def produtoMaisCaro(produtos):
    i = 0
    nomeProdMaisCaro = ''
    maisCaro = 0
    while i < len(produtos):
        if produtos[i][2] > maisCaro:
            maisCaro = produtos[i][2]
            nomeProdMaisCaro = produtos[i][0]
        i = i + 1
    return nomeProdMaisCaro

def produtoMaisBarato(produtos):
    i = 0
    nomeProdMaisBarato = ''
    maisBarato = 9999999
    while i < len(produtos):
        if produtos[i][2] < maisBarato:
            maisBarato = produtos[i][2]
            nomeProdMaisBarato = produtos[i][0]
        i = i + 1
    return nomeProdMaisBarato

def doisPrimeiros(produtos):
    primeiros = []
    i = 0
    if len(produtos) < 2:
        primeiros.append(produtos[0][0])
        primeiros.append(produtos[1][0])
    else:
        while i < len(produtos):
            primeiros.append(produtos[i][0])
            i = i + 1
    return primeiros

def doisUltimos(produtos):
    ultimos = []
    i = 0
    cont = -1
    if len(produtos) < 2:
        ultimos.append(produtos[-1][0])
        ultimos.append(produtos[-2][0])
    else:
        while i < len(produtos):
            ultimos.append(produtos[cont][0])
            cont = cont - 1
            i = i + 1
    if len(ultimos) > 2:
        ultimos.pop()
    return ultimos

