class Pe:
    def __init__(self, tamanho):
        self.tam = tamanho
        self.quant = 0
        self.vetor = [None] * self.tam

    def push(self, valor):
        self.vetor[self.quant] = valor
        self.quant += 1

    def push_v(self, *valores):
        for i in valores:
            self.push(i)

    #Não usar
    def show(self):
        for i in range(self.quant):
            print(self.vetor[i], end=' ')
        print("\n")

    def ver_topo(self):
        return self.vetor[self.quant - 1]
    
    def pop(self):
        self.quant -= 1
    
    def esta_cheia(self):
        return self.quant == self.tam
    
    def esta_vazia(self):
        return self.quant == 0
    
