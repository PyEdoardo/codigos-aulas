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

def alterarSituacao(matriculaAlterar, nota1Nova, nota2Nova, frequenciaNova, arquivojson):
    arquivo = open(arquivojson, 'r', encoding='utf8')
    dicionario_alunos = json.load(arquivo)
    arquivo.close()

    if matriculaAlterar in dicionario_alunos:
        dicionario_alunos[matriculaAlterar]['nota1'] = nota1Nova
        dicionario_alunos[matriculaAlterar]['nota2'] = nota2Nova
        dicionario_alunos[matriculaAlterar]['percentualFrequencia'] = frequenciaNova
    else:
        return 'Erro'
    arquivo = open(arquivojson, 'w', encoding='utf8')
    json.dump(dicionario_alunos, arquivo, indent=4, ensure_ascii=False)
    arquivo.close()


def exportarSituacao(situacao, arquivoTexto):
    arquivo = open(arquivoTexto, 'w', encoding='utf8')
    for aluno in situacao:
        arquivo.write(f'{situacao[aluno]["matricula"]} ,{situacao[aluno]["nome"]} ,{situacao[aluno]["situacao"]}\n')
    arquivo.close()

def adicionarAluno(nome, nota1, nota2, frequencia, arquivojson):
    arquivo = open(arquivojson, 'r', encoding='utf8')
    dicionario_Alunos = json.load(arquivo)
    arquivo.close()

    maior_matrícula = 0

    for matricula in dicionario_Alunos.keys():
        numero_matricula = int(matricula)
        if numero_matricula < maior_matrícula:
            numero_matricula = maior_matrícula
    numero_matricula = numero_matricula + 1

    dicionario_Alunos[numero_matricula] = {
        'nome' : nome,
        'nota1' : nota1,
        'nota2' : nota2,
        'percentualFrequencia' : frequencia
    }

    arquivo = open(arquivojson, 'w', encoding='utf8')
    json.dump(dicionario_Alunos, arquivo, indent=4, ensure_ascii=False)




