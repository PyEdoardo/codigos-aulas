def valorTotalEstoque(produtos):
    soma = 0
    for produto in produtos:
        soma += produto[1] * produto[2]
    return soma

def produtosInferiorADez(produtos):
    i = 0
    nomeItensMenorEstoque = []
    itensMenorEstoque = []
    while i < len(produtos):
        if produtos[i][1] < 10:
            itemMenor = produtos[i][1]
            itensMenorEstoque.append(itemMenor)
            nomeItem = produtos[i][0]
            nomeItensMenorEstoque.append(nomeItem)
        i = i + 1
    if sum(itensMenorEstoque) < 10:
        return 'Sem itens menores que 10! '
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
    if len(primeiros) < 2:
        primeiros.pop()
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

