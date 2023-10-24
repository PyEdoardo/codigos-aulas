g = []
r = []
i = 0
while i < 10:
    g.append(input("Gabarito: "))
    i = i + 1
i = 0
while i < 10:
    r.append(input("Respota: "))
    i = i + 1

errou = []
acertos = 10
i = 0
while i < 10:
    if g[i] != r[i]:
        errou.append(i)
    else:
        acertos = acertos + 1
    i = i + 1
i = 0
while i < len(errou):
    print(errou[i])
    i = i + 1
if acerto >= 6:
    print("Aprovado! ")
else:
    print("Reprovado! ")                
