import func

arq = ('acesso.json')
livrosAcervo = func.carregarLivro(arq)

while True:
    Menu = str(input('''
1 -  Cadastrar livro novo
2 - Listar livro
3 - Excluir livro
4 - Relatorio livros sem estoque
0 - Sair 
 ''')) 
    if Menu == '0':
        
        break
    if Menu == '1':
        isbn = str(input('digite o ISBN do livro'))
        tituloLivro = str(input('Digite o titulo do livro'))
        nomeAutor = str(input('Digite o autor do livro'))
        genero = str(input('Digite o genero do livro'))
        precoCompra = float(input('Digite o preço de compra do livro'))
        precoVenda = float(input('Digite o preço e venda do livro'))
        qtdDisponivel = int(input('Digite a quantidade em estoque'))

        func.cadLivro(livrosAcervo,isbn,tituloLivro,nomeAutor,genero,precoCompra,precoVenda,qtdDisponivel)
        func.salvarLivro(arq, livrosAcervo)
    
    elif Menu == "2":
        if livrosAcervo:
            for isbn, livros in livrosAcervo.items():
                print(f"Codigo do livro : {isbn} Nome do Livro : {livros['Titulo']}")

    elif Menu == "3":
        livroDel = str(input('Qual deseja deletar? use o ISBN.'))
        print(func.excluirLivro(livrosAcervo, livroDel))
        func.salvarLivro(arq, livrosAcervo)
    
    elif Menu == '4':
        if livrosAcervo:
            for isbn, livros in livrosAcervo.items():
                if livros['Qtd_Estoque'] == 0:
                    print(f"{isbn} - {livros['Titulo']}" )





    








        
        




