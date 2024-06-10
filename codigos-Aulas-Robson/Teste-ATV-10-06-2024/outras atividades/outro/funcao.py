import json


def cadastrarLivros(livros, isbn, titulo, autor, genero, precoCompra, precoVenda, qntDisp):
    if isbn in livros:
        return "O ISBN já foi cadastrado!"
    else:
        livros[isbn] = {
            'titulo': titulo,
            'autor': autor,
            'genero': genero,
            'precoCompra': precoCompra,
            'precoVenda': precoVenda,
            'qntDisp': qntDisp
        }
        return "Livros cadastrados com sucesso!"
    
def salvarLivros(nomeArquivo, livros):
    arquivo = open(nomeArquivo, 'w', encoding='utf-8')
    livrosJson = json.dumps(livros, indent=4, ensure_ascii=False)
    arquivo.write(livrosJson)
    arquivo.close()


def carregarLivros(nomeArquivo):
    arquivo = open(nomeArquivo, 'r')
    conteudo = arquivo.read().strip()
    livros = {}
    if conteudo:
        livros = json.loads(conteudo)

    arquivo.close()
    return livros

def excluirLivro(livros, isbn):
    if isbn in livros:
        del livros[isbn]
        return "Livro excluido com sucesso"
    else:
        return "Livro não encontrado"