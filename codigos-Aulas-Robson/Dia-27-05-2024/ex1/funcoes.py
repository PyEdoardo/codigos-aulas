import datetime

def lerNotas(nomeArquivo):
    arquivo = open(nomeArquivo, 'r')
    notasString = arquivo.read().strip().splitlines()
    arquivo.close()
    return notasString

def salvarMP(nomeArquivo, alunos):
    arquivo = open(nomeArquivo, 'a')
    for matricula, aluno in alunos.items():
        arquivo.write(f"\nDia: {datetime.date.today().day} | Mes: {datetime.date.today().month} | Ano: {datetime.date.today().year} {aluno['nome']}, {aluno['mp']}\n")
    arquivo.close()    