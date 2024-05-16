def procLogin(login, usuarios):
    usuarios = {}
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
            dictData[key] = {'nome' : usuarios[key]['nome'], 'ultimo_acesso' : usuarios[key]['ultimo_acesso']}
    return dictData

def modificarNome(login, novoNome, usuarios):
    if login not in usuarios:
        return 'Não existe esse usuário!'
    else:
        usuarios[login]['nome'] == novoNome
        
          