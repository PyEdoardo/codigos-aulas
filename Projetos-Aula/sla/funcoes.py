def cadastroAluno(alunos, matricula, nome, idade, g1, g2, carga_horaria, status, arquivo):
    arq = open(arquivo, 'a')
    alunos[matricula] = {'nome': nome, 'idade' : idade, 'g1' : g1, 'g2' : g2, 'carga_horaria' : carga_horaria, 'status' : status }
    arq.write(f'{matricula},{nome},{idade},{g1},{g2}{carga_horaria},{status}')
    arq.close()
    return "Operação Sucedida! "

def statusAluno(alunos, matricula, g1, g2, carga_horaria, status):
    g1_aluno = alunos['matricula']['g1']
    g2_aluno = alunos['matricula']['g2']
    total = g1 + (g2 * 2)
    if carga_horaria >= 70 and total >= 6:
        alunos['matricula']['status'] = 'aprovado'
    if carga_horaria >= 70 and total < 6:
        alunos['matricula']['status'] = 'exame final'
    else:
        alunos['matricula']['status'] = 'reprovado'

def criarMatricula(NomeArquivo):
    arquivo = open(NomeArquivo, 'r')
    lenMatricula = len(str(arquivo))
    arquivo.close()
    if lenMatricula in [0, '0']:
        return 1
    else:
        return lenMatricula
    
    