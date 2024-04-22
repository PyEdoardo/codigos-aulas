def fazAlgo(a,b):
    if a>b:
        return a
    return b
def fazAlgumaCoisa(a,b):
    if a>b:
        return True
    return False

def fazAindaMais(a,b):
    return a>b

def fazOutraCoisa(*a):
    b = a[0]
    for i in a:
        if i > b:
            b = i
    return b

def fazMais(*a):
    if a:
        print(' Teve Argumentos ')
    else:
        print(' Não teve argumentos')

def oQueFaz(*a):
    soma = 0
    for i in a:
        soma += i
    return soma
    print('Total = ', soma)

def fazOQue(a,b):           
    if a > b:
        return True
    else:
        return False
    print('Concluido')