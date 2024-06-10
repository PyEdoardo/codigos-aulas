import funcao

arquivo = 'livros.json'
livros = funcao.carregarLivros(arquivo)

while True:
    menu = input('''
    [0] - Sair
    [1] - Cadastrar livros
    [2] - Listar livros
    [3] - Excluir livro
    [4] - Relatório de livros sem estoque
''')
    
    if menu == "0":
        break
    if menu == "1":
        isbn = input("ISNB: ")
        titulo = input("Título: ")
        autor = input("Autor: ")
        genero = input("Gênero: ")
        precoCompra = float(input("Preço de compra: "))
        precoVenda = float(input("Preço de venda: "))
        qntDisp = int(input("Quantidade disponível: "))
        print(funcao.cadastrarLivros(livros, isbn, titulo, autor, genero, precoCompra, precoVenda, qntDisp))
        funcao.salvarLivros(arquivo, livros)
    elif menu == "2":
        for isbn, livro in livros.items():
            print(f"{isbn} - {livro['titulo']} - {livro['qntDisp']}")
    
    elif menu == "3":
        livroDel = input("Digite o ISBN do livro que deseja excluir: ")
        print(funcao.excluirLivro(livros, livroDel))
        funcao.salvarLivros(arquivo, livros)

    elif menu == "4":
        for isbn, livro in livros.items():
            if livro['qntDisp'] == 0:
                print(f"{isbn} - {livro['titulo']}")