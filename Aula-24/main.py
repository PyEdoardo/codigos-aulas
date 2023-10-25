print("Tipos de Cálculos: (A) Adição, (S) Subtração, (C) Circunferência de Círculos, (M) Multiplicação, (R) Raiz Quadrada, (P) Potênciação, (Sair) Fecha o Programa. ") # tipos de variações de cálculos
tipo = input("Digite o Tipo de Cálculo: ") #variável que registra o tipo do cálculo

while tipo != 'Sair' or tipo != 'sair':
 if tipo == 'A':
    soma_1 = float(input("Digite o Número 1: ")) #var do primeiro num da adição
    soma_2 = float(input("Digite o Número 2: ")) #var do 2 num da adição

    def adic(soma_1, soma_2): # função que cria a adição
        soma = soma_1 + soma_2
        return soma
    soma_num = adic(soma_1, soma_2)
    print(soma_num)
    print("------------------------------------------")
    tipo = input("Digite o Tipo de Cálculo: ")  # variável que registra o tipo do cálculo

 elif tipo == 'S':
   sub_1 = float(input("Digite o Número 1: "))
   sub_2 = float(input("Digite o Número 2: "))

   def subt(sub_1, sub_2):
       sub = sub_1 - sub_2
       return sub
   subtracao = subt(sub_1, sub_2)
   print(subtracao)
   print("------------------------------------------")
   tipo = input("Digite o Tipo de Cálculo: ")  # variável que registra o tipo do cálculo

 elif tipo == 'C':
    raio = float(input("Digite o Raio: "))
    pi = 3.1415926535

    def circun(pi, raio):
        circ = 2 * pi * raio
        return circ
    circunf = circun(pi, raio)
    print(circunf)
    print("------------------------------------------")
    tipo = input("Digite o Tipo de Cálculo: ")  # variável que registra o tipo do cálculo

 elif tipo == 'M':
    expoente = float(input("Digite o Expoente: "))
    multi = float(input("Digite o Multiplicador: "))

    def mult(expoente, multi):
        multiplic = expoente * multi
        return multiplic
    res = mult(expoente, multi)
    print(res)
    print("------------------------------------------")
    tipo = input("Digite o Tipo de Cálculo: ")  # variável que registra o tipo do cálculo

 elif tipo == 'R':
    raiz = float(input("Digite a Raiz: "))

    def r_quad(raiz):
        raiz_quad = float(raiz ** (1/2))
        return raiz_quad

    res = float(r_quad(raiz))
    print(res)
    print("------------------------------------------")
    tipo = input("Digite o Tipo de Cálculo: ")  # variável que registra o tipo do cálculo

 elif tipo == 'P':
     num_1 = float(input("Digite o Número a Ser Potênciado: "))
     pot = int(input("Digite a Potência: "))
     def potenc(num_1, pot):
         calc = num_1 ** pot
         return calc
     potencia = potenc(num_1, pot)
     print(potencia)
     print("------------------------------------------")
     tipo = input("Digite o Tipo de Cálculo: ")  # variável que registra o tipo do cálculo


