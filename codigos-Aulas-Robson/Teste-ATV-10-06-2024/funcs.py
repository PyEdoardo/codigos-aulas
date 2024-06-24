import json

def situacaoAlunos(arquivojson):
    arquivo = open(arquivojson, 'r', encoding='utf8')
    conteudo = arquivo.read().strip()
    alunos = {}
    situacao = {}
    if conteudo:
        alunos = json.loads(conteudo)
    for aluno in alunos:
        if alunos[aluno]['nota1'] >= 6 and alunos[aluno]['nota2'] >= 6 and alunos[aluno]['percentualFrequencia'] >= 75:
            situacao[aluno] = {
                'matricula' : aluno,
                'nome' : alunos[aluno]["nome"],
                'situacao' : 'aprovado'
            }
        elif alunos[aluno]['nota1'] >= 6 or alunos[aluno]['nota2'] >= 6 and alunos[aluno]['percentualFrequencia'] >= 75:
            situacao[aluno] = {
                'matricula' : aluno,
                'nome' : alunos[aluno]["nome"],
                'situacao' : 'recuperação'
            }
        else:
            situacao[aluno] = {
                'matricula' : aluno,
                'nome' : alunos[aluno]["nome"],
                'situacao' : 'reprovado'
            }
    arquivo.close()
    return situacao

def alterarSituacao(alunos ,matriculaAlterar, nota1Nova, nota2Nova, arquivojson):
    


def exportarSituacao(situacao, arquivoTexto):
    arquivo = open(arquivoTexto, 'w', encoding='utf8')
    for aluno in situacao:
        arquivo.write(f'{situacao[aluno]["matricula"]} ,{situacao[aluno]["nome"]} ,{situacao[aluno]["situacao"]}\n')
    arquivo.close()



