def mediasAluno(nota1, nota2, nota3, tipoMedia):
    if tipoMedia == 'A' or tipoMedia == 'A':
        media = (nota1 + nota2 + nota3) / 3
    elif tipoMedia == 'P' or tipoMedia == 'p':
        media = ((nota1 * 5) + (nota2 * 3) + (nota3 * 2)) / (5 + 3 + 2)
    return media

tipoAluno = input("Deseja Qual Tipo de Média?\nDigite 'A' para Média Aritmética\nOu Digite 'P' para Média Ponderada: ")

n1 = float(input("Qual Foi a 1° Nota?"))
n2 = float(input("Qual Foi a 2° Nota?"))
n3 = float(input("Qual Foi a 3° Nota?"))

print(f'\nTotal das Notas: \nNota 1: {n1}\nNota 2: {n2}\nNota 3: {n3}\nTipo de Média: {tipoAluno}\nMédia: {mediasAluno(n1, n2, n3, tipoAluno)}')