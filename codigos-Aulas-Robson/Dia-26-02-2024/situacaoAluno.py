while True:
    nomeAluno = input('Entre com o nome do aluno ou digite "sair" para encerrrar: ')
    if nomeAluno == 'sair':
        break
    notaG1 = float(input("Nota G1: "))
    notaG2 = float(input("Nota G2: "))
    frequencia = int(input("Entre com a frequência: "))
    mp = (notaG1 + (notaG2 * 2))/3
    
    if frequencia < 75:
        print(f"O aluno {nomeAluno} foi reprovado por falta.")
    elif mp >= 6:
        print(f"O aluno {nomeAluno} foi aprovado.")
    else:
        ef = float(input("Entre com a nota de EF: "))
        mf = (mp + (ef * 2))/3
        if mf >= 6:
            print(f"O aluno {nomeAluno} foi aprovado.")
        else:
            print(f"O aluno {nomeAluno} foi reprovado.")

