import Pd

teste = input("Digite uma palavra (não digite em maiúsculo!): ")

pilha1 = Pd.Pd()

for i in teste:
    pilha1.push(i)

i = 0
e_palindromo = False

while True:
    if i > len(teste) - 1:
        break
    if pilha1.ver_topo() == teste[i]:
        pilha1.pop()
    i += 1
    if pilha1.esta_vazia():
        e_palindromo = True
        break

if e_palindromo:
    print("É palindromo!")
else:
    print("Não é palindromo!")


