def adicionar_membro(nome, idade, email, cpf, membros):
    membro = {
              'nome': nome, 
              'idade': idade, 
              'email': email
              }
    membros[cpf] = membro
    print(f'Membro "{nome}" adicionado ao clube.')

def remover_membro(cpf, membros):
    nome_cpf = membros[cpf]['nome']
    if cpf in membros:
        membros.pop(cpf)
        return f'Membro "{nome_cpf}" removido do clube.'
    else:
        return 'Membro Não Encontrado.'

def listar_membros(membros):
    lista_membros = {}
    for membro in membros:
        nome = membros[membro]['nome']
        email = membros[membro]['email']
        lista_membros[membro] = {
            'nome' : nome,
            'email' : email
        }
    return lista_membros

def quantidade_membros(membros):
    quantidade = len(membros)
    return quantidade