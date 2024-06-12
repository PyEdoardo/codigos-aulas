import funcoes

alunos = {

}


while True:
    opcao = input("Gostaria de Cadastrar, listar ou sair: ")
    if opcao == 'sair':
        break
    if opcao in ['cadastrar', 'cadastro']:
        matricula = input("Digite a Matrícula: ")
        nome = input("Digite o nome: ")
        g1 = float(input("Digite a nota de G1: "))
        g2 = float(input("Digite a nota de G2: "))
        funcoes.cadastrarAlunos(alunos, matricula, nome, g1, g2)
    if opcao in ['listar', 'list', 'Listar']:
        funcoes.listarAlunos(alunos)

print(alunos)  
