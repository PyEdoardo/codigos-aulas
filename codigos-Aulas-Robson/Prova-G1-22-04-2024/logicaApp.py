import modulosApp

produtos = []
i = 1
while True:
    nomeProd = input(f'Digite o Nome do Produto {i}: ')
    if nomeProd == '0':
        break
    quantidadeProd = float(input("Digite a Quantidade do Produto: "))
    precoUnitarioProd = float(input("Digite o Preço Unitário do Produto: "))
    categoriaProd = input("Digite a Categoria do Produto: ")
    qtTotalEstoque =+ quantidadeProd
    produtos.append([nomeProd, quantidadeProd, precoUnitarioProd, categoriaProd])
    i = i + 1

qtProdutosTotal = i

print(f'\nArmazém Tech - Gestão de Produtos\n---------------------------------\nProdutos    |   Qt-Estoque   |    Pre. Unitário   |   Categoria\n')
i = 0
while i < len(produtos):
    print(f'{produtos[i][0]} | {produtos[i][1]} | {produtos[i][2]} | {produtos[i][3]}')
    i = i + 1
print(f'\nTotal de Produtos Processados: {qtProdutosTotal}')
print(f'Valor Total do Estoque: {modulosApp.valorTotalEstoque(produtos)}')
print(f'Produto com Estoque Inferior a 10: {modulosApp.produtosInferiorADez(produtos)}')
print(f'O Produto com Valor Mais Caro: {modulosApp.produtoMaisCaro(produtos)}')
print(f'O Produto com Valor Mais Barato: {modulosApp.produtoMaisBarato(produtos)}')
print(f'Os Dois Primeiros Produtos da Lista São: {modulosApp.doisPrimeiros(produtos)}')
print(f'Os Dois Últimos Produtos da Lista São: {modulosApp.doisUltimos(produtos)}')
