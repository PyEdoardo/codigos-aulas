def procLogin(login, usuarios):
    if login not in usuarios:
        return 'Não existe este usuário!'
    else:
        return usuarios[login]
    
def procData(data, usuarios):
    dictData = {}
    for key in usuarios:
        if data not in usuarios[key]['ultimo_acesso']:
            return 'Não existe essa data!'
        elif data == usuarios[key]['ultimo_acesso']:
            dictData[key] = {'nome' : usuarios[key]['nome'], 'ultimo_acesso' : usuarios[key]['ultimo_acesso'], 'id_maquina' : usuarios[key]['id_maquina']}
    return dictData

def modificarNome(login, novoNome, usuarios):    
    usuarios[login]['nome'] = novoNome
    return 'Nome Alterado!'

def modificarData(login, novaData, usuarios):
    usuarios[login]['ultimo_acesso'] = novaData
    return 'Data Alterada'

def modificarID(login, novoID, usuarios):
    usuarios[login]['id_maquina'] = novoID
    return 'ID Alterado!'
        
def modificarTudo(login, tudoNovo, usuarios):
    usuarios[login]['nome'] = tudoNovo[0]
    usuarios[login]['ultimo_acesso'] = tudoNovo[1]
    usuarios[login]['id_maquina'] = tudoNovo[2]
    return 'Tudo Alterado!'

def apagarUsuario(login, usuarios):
    del usuarios[login]
    return 'Usuário Apagado!'