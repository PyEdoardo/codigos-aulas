def peso_ideal (altura, sexo):
    if sexo == 'masculino':
        ideal = (72.7*altura) - 58
    elif sexo == 'feminino':
        ideal = (62.1*altura) - 44.7
    return f'O seu peso ideal e: {ideal}'

alt = float(input('Digite sua altura: '))
sex = input('Seu sexo: ')
print(peso_ideal(alt, sex))