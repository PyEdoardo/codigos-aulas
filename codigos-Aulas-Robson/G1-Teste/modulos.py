def calcularMedia(notas):
    media = sum(notas) / len(notas)
    return media

def situacaoAluno(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

def maiorMedia(alunos):
    maiorMedia = 0
    nomeMaior = ''
    i = 0
    while i < len(alunos):
        if alunos[i][2] > maiorMedia:
            maiorMedia = alunos[i][2]
            nomeMaior = alunos[i][0]
        i = i + 1    
    return maiorMedia, nomeMaior

def menorMedia(alunos):
    menorMedia = 9999
    nomeMenor = ''
    i = 0
    while i > len(alunos):
        if alunos[i][2] < menorMedia:
            menorMedia = alunos[i][2]
            nomeMenor = alunos[i][0]
        i = i + 1    
    return menorMedia, nomeMenor      