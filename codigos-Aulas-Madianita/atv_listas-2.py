cardapio = [['Cachorro-Quente', 5.00],
            ['X-Salada', 10.00],
            ['X-Bacon', 12.00],
            ['Bauru', 8.00],
            ['Refrigerante', 4.00],
            ['Suco', 6.00]] #Lista do Cardápio

print(cardapio)

fechar = 'n'
totalConta = 0
while fechar == 'n':
    cod = int(input("Código do Produto: "))
    qt = int(input("Quantidade do Produto: "))
    totalConta = totalConta + cardapio[cod][1]
    fechar = input("Quer Fechar a Conta? (s ou n)")
print("Valor da Conta: ", totalConta)

i = 0
sair = 'n'
while i < len(cardapio) and sair != 'n':
    desconto = float(input("Digite o Desconto: "))
    produtoDesc = int(input("Digite o Produto: "))
    cardapio[produtoDesc].append(desconto)
    print("Cardapio: ", cardapio)
    i = i + 1
