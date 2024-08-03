import json

alunos = {

}

disciplinas = {

}

def adicionar_aluno(alunos, nome):
    if nome not in alunos:
        alunos[nome] = {}
    else:
        print(f"Aluno {nome} já existe.")

def adicionar_disciplina(disciplinas, nome):
    if nome not in disciplinas:
        disciplinas[nome] = {}
    else:
        print(f"Disciplina {nome} já existe.")

def matricular_em_disciplina(alunos, disciplinas, aluno, disciplina):
    if aluno not in alunos:
        print(f"O Aluno não está matriculado.")
    if disciplina not in disciplins:
        print(f"A Disciplina não está adicionada.")
    elif
