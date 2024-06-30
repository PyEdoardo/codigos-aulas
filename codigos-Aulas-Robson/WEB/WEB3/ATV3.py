def frequência_parcial(lista, nome_a_parar):
    contadores = {}
    for item in lista:
        if item in contadores:
            contadores[item] += 1
        else:
            contadores[item] = 1
        if item == nome_a_parar:
            break
    return contadores

estudantes = ['Cindy', 'John', 'Cindy', 'Adam', 'Adam', 'Jimmy', 'Joan', 'Cindy', 'Joan']

estado_apos_adam1 = {}
for item in estudantes:
    if item in estado_apos_adam1:
        estado_apos_adam1[item] += 1
    else:
        estado_apos_adam1[item] = 1
    if item == 'Adam':
        break

estado_apos_adam2 = {}
adam_count = 0
for item in estudantes:
    if item in estado_apos_adam2:
        estado_apos_adam2[item] += 1
    else:
        estado_apos_adam2[item] = 1
    if item == 'Adam':
        adam_count += 1
        if adam_count == 2:
            break

estado_apos_jimmy = {}
for item in estudantes:
    if item in estado_apos_jimmy:
        estado_apos_jimmy[item] += 1
    else:
        estado_apos_jimmy[item] = 1
    if item == 'Jimmy':
        break

print("Estado após visitar o primeiro 'Adam':", estado_apos_adam1)
print("Estado após visitar o segundo 'Adam':", estado_apos_adam2)
print("Estado após visitar 'Jimmy':", estado_apos_jimmy)
