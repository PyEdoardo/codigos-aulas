estoque = [['001', 'marmelada', 50, 6.50],
           ['002', 'goiabada', 20, 6.00],
           ['003', 'ambrosia', 25, 5.00],
           ['004', 'maria mole', 100, 5.50],
           ['005', 'brigadeiro', 55, 4.00]]

continuar = 's'

while continuar == 's':
    doce = []
    doce.append(input("Código do Produto: "))
    doce.append(input("Nome do Doce: "))
    doce.append(int(input("Estoque desse Doce: ")))
    doce.append(float(input("Preço unitário: ")))
    estoque.append(doce)
    continuar = input("Deseja adicionar mais doces? (s ou n) ")

i = 0

while i < len(estoque):
    print(f"\nNome do Doce: {estoque[i][1]} \nValor Total do Doce em Estoque: {estoque[i][2] * estoque[i][3]} \n-------------")
    i = i + 1

i = 0

comprar = 's'
codigo = ''
quantidadeDoces = 0

while comprar == 's':
    codigo = int(input("Qual Código do Produto? "))
    quantidadeDoces = int(input("Qual a Quantidade? "))
    if quantidadeDoces < estoque[codigo][2]:
        print("Tem Estoque!")
        estoque[codigo][2] = estoque[codigo][2] - quantidadeDoces
        print(f"Doce: {estoque[codigo][1]} Você irá pagar: R${estoque[codigo][2] * estoque[codigo][3]} ")
    else:
        print("Não tem estoque!")       
