import json

def cadastrarAluno(alunos, matricula, nome, g1, g2):
    if matricula in alunos:
        return "A matrícula informa já existe!"
    else:
        alunos[matricula] = {
            'nome': nome,
            'g1': g1,
            'g2': g2
        }
        return "Aluno cadastrado com sucesso."
    
def salvarAlunos(nomeArquivo, alunos):
    arquivo = open(nomeArquivo, 'w', encoding='utf-8')
    alunosJson = json.dumps(alunos, indent=4, ensure_ascii=False)
    arquivo.write(alunosJson)
    arquivo.close()

def carregarAlunos(nomeArquivo):
    arquivo = open(nomeArquivo, 'r')
    conteudo = arquivo.read().strip()
    alunos = {}
    if conteudo:
        alunos = json.loads(conteudo)

    arquivo.close()
    return alunos