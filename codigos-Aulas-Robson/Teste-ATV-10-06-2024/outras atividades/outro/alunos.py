import funcoes

arquivo = 'alunos.json'
alunos = funcoes.carregarAlunos(arquivo)

while True:
    menu = input('''
    [1] - Cadastrar alunos
    [2] - Listar alunos
    [0] - Sair
    ''')
    if menu == "0":
        break

    if menu == "1":
        matricula = input("Entre com a matrícula: ")
        nome = input("Entre com o nome: ")
        g1 = float(input("Entre com a nota G1: "))
        g2 = float(input("Entre com a nota G2: "))
        print(funcoes.cadastrarAluno(alunos, matricula, nome, g1, g2))
        funcoes.salvarAlunos(arquivo, alunos)

    elif menu == "2":
        for matricula, aluno in alunos.items():
            print(f"{matricula} - {aluno['nome']}")
