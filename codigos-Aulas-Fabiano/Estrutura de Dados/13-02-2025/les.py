class Les:
    def __init__(self, tamanho):
        self.tam = tamanho
        self.quant = 0
        self.vetor = [None] * self.tam

    def inserir_fim(self, valor):
        self.vetor[self.quant] = valor
        self.quant += 1

    def show(self):
        for i in range(self.quant):
            print(self.vetor[i], end=' ')
        print("\n")
    
    def remover_fim(self):
        self.quant -= 1
    
    def esta_cheia(self):
        return self.quant == self.tam
    
    def esta_vazia(self):
        return self.quant == 0
    