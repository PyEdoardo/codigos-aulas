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

def alterarNotas(matricula, nota1, nota2, arquivojson):
    arquivo = open(arquivojson, 'r', encoding='utf8')
    leitura = arquivo.read()
    alunos = {}
    if leitura:
        alunos = json.loads(leitura)
    arquivo.close()
    if matricula not in alunos:
        return 'Não existe essa matrícula!'
    else:
        alunos[matricula]['nota1'] = nota1
        alunos[matricula]['nota2'] = nota2
    return alunos[matricula]

def salvarNoJson(arquivojson, alunoModificados):
    arquivo = open(arquivojson, 'w', encoding='utf8')
    alunos = json.dumps(alunoModificados, indent=4, ensure_ascii=False)
    arquivo.write(alunos)
    arquivo.close()
    return 'Arquivo Modificado'
    


def exportarSituacao(situacao, arquivoTexto):
    arquivo = open(arquivoTexto, 'w', encoding='utf8')
    for aluno in situacao:
        arquivo.write(f'{situacao[aluno]["matricula"]} ,{situacao[aluno]["nome"]} ,{situacao[aluno]["situacao"]}\n')
    arquivo.close()



