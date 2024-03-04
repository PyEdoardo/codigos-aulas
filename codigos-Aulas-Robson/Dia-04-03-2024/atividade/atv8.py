def numero(valor):
    if valor <= 1:
        return False
    
    soma_divisores = 1

    for i in range(2, int(valor**0.5) + 1):
        if valor % i == 0:
            soma_divisores += i
            if i != valor // i:
                soma_divisores += valor // i

    return soma_divisores == valor

while True:
    num = int(input('Digite um numero para saber se e perfeito ou nao(para sair digite 0): '))
    if num == 0:
        break
    print(f'{num} e numero perfeito? {numero(num)} ')

    ##peguei da net pq tá hard