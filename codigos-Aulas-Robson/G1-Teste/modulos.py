def calcularMedia(notas):
    media = sum(notas) / len(notas)
    return media

def situacaoAluno(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

def maiorNota(alunos):
    maiorNota = 0
    