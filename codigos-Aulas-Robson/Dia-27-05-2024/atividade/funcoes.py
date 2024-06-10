def cadastrarAlunos(alunos, matricula, nome, g1, g2):
    arquivo = open('alunos.txt', 'a')
    alunos[matricula] = {'nome' : nome, 'g1' : g1, 'g2' : g2}
    arquivo.write(f'Matricula: {matricula}, Nome: {nome}, G1: {g1}, G2: {g2}\n')
    arquivo.close

def listarAlunos(alunos):
    for aluno in alunos:
        print(alunos)

    