import json

def cadLivro(livrosAcervo,isbn,tituloLivro,nomeAutor,genero,precoCompra,precoVenda,qtdDisponivel):
    if isbn in livrosAcervo:
        return 'Ja existe esse livro no cadastro'
    
    else: 
        livrosAcervo[isbn] = {
            'Titulo': tituloLivro,
            'Autor': nomeAutor,
            'genero': genero,
            'PrecoAq.': precoCompra,
            'PrecoVen.': precoVenda,
            'Qtd_Estoque': qtdDisponivel
            }
        

def excluirLivro(livrosAcervo, isbn):
    if isbn in livrosAcervo:
        del livrosAcervo[isbn]
        return 'Livro excluído com sucesso'
    else:
        return 'ISBN não encontrado no acervo'
    
def salvarLivro(nomeArquivo,livrosAcervo):
    arquivo = open(nomeArquivo, 'w')
    LivrosacervoJson = json.dumps(livrosAcervo, indent=4, ensure_ascii=False)
    arquivo.write(LivrosacervoJson)
    arquivo.close()

def carregarLivro(nomeArquivo):
    arq = open(nomeArquivo, 'r', encoding='utf8')
    conteudo =  arq.read().strip()
    livros = {}
    if conteudo:
        livros = json.loads(conteudo)
  
    arq.close()
    return livros

    

