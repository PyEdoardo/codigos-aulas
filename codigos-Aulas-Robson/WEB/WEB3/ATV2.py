agenda_r = {
    '(123)456-78-90': ['Anna', 'Karenina'],
    '(901)234-56-78': ['Yu', 'Tsun'],
    '(321)908-76-54': ['Hans', 'Castorp']
            }

def rlookup(agenda, telefone):
    if telefone in agenda:
        nome_completo = agenda[telefone]
        print(f'O número {telefone} pertence a {nome_completo[0]} {nome_completo[1]}.')
    else:
        print(f'O número {telefone} não está na agenda.')

while True:
    print("Molde Número: (xxx)xxx-xx-xx")
    numero = input("Qual Número deseja procurar? (000 para fechar.) ")
    if numero == '000' or numero == '00' or numero == '0':
        break
    else:
        rlookup(agenda_r, numero)
