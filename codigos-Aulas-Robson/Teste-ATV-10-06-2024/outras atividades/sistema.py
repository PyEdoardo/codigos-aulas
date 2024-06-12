import funcoes_sistema

dados = {}

while True:
    opcao = input('''
    [0] - Sair
    [1] - Inserir usuário
    [2] - Listar nome de todos os usuários
    [3] - Listar dados de um usuário
    [4] - Listar os nomes dos usuários com último acesso em uma data específica
    [5] - Alterar dados de um usuário, com as seguintes possibilidades (todos, nome, último acesso ou máquina)
    [6] - Excluir um usuário
''')
    
    if opcao == "0":
        break
    if opcao == "1":
            login = input("Login: ")
            nome = input("Nome: ")
            ult_acess = input("Último acesso: ")
            maquina = input("Máquina: ")
            print(funcoes_sistema.criarUsuarios(dados, login, nome, ult_acess, maquina))
    
    elif opcao == "2":
         for login, dado in dados.items():
              print(dado)

    # elif opcao == "3":
         
    elif opcao == "4":
         while True:
            menu = input('''
            [1] - Todos
            [2] - Nome
            [3] - Último acesso
            [4] - Máquina
    ''')
            
            if menu == "1":
                new_nome = input("Nome: ")
                new_ult_acess = input("Último acesso: ")
                new_maquina = input("Máquina: ")
                