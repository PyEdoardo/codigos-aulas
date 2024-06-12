def criarUsuarios(dados, login, nome, ult_acess, maquina):
    if login in dados:
        return "Já existe essee login!"
    else:
        dados[login] = {
          'nome': nome,
          'ult_acess': ult_acess,
          'maquina': maquina
        }
        return "Usuário cadastrado com sucesso!"
    
def alterarUsuarios(login, nome, ult_acess, maquina):
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
                
