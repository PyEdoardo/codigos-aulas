import random
###ATV 1:
while True:
    n1 = float(input("Digite o Número 1: "))
    n2 = float(input("Digite o Número 2: "))
    n3 = float(input("Digite o Número 3: "))
    n4 = float(input("Digite o Número 4: "))
    n5 = float(input("Digite o Número 5: "))
    media = (n1 + n2 + n3 + n4 + n5) /  5
    print(media)
    fechar = input("Gostaria de Terminar? Sim ou Não: ")
    if fechar == "s":
        break

###ATV 2:
numero = float(input("Digite um Número: "))
if (numero%2) == 0:
    print("Par")
else:
    print("Impar")

###ATV 3:
while True:
    idade = int(input("Digite a Idade: "))
    if idade >= 18:
        print("Você é Maior de Idade!! ")
    else:
        print("Você é Menor de Idade!!! ")
    fechar = input("Gostaria de Terminar? Sim ou Não: ")
    if fechar == "s":
        break

###ATV 4:

valorProduto = float(input("Digite o Valor do Produto: "))

desconto = valorProduto * 0.1

print(f"Valor do Produto: {valorProduto}\nValor com Desconto: {desconto} ")

###ATV 5:

while True:
    qtTentativas = 0
    numAleatorio = random.randint(0, 100)
    num = int(input("Digite um Número Inteiro: "))
    if num == numAleatorio:
        print(f"********************************\nParabéns o Número Correto é {numAleatorio}\nQuantidade de Tentativas: {qtTentativas} !")
    else:
        qtTentativas += 1
        print("Você Errou!!!\n")

