presidentes = {'Barack Hussein Obama II':'Hawaii',
'George Walker Bush':'Connecticut',
'William Jefferson Clinton':'Arkansas',
'George Herbert Walker Bush':'Massachussetts',
'Ronald Wilson Reagan':'Illinois',
'James Earl Carter, Jr':'Georgia'}

def estadoNasc(presidente, presidentes):
    if presidente not in presidentes:
        return 'Presidente Não Encontrado!'
    else: 
        estado = presidentes[presidente]
        return estado

presidente_pergunta = input("Digite o Nome do Presidente: ")
print(estadoNasc(presidente_pergunta, presidentes))