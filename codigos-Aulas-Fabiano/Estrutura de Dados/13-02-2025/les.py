class Les:
    def __init__(self, tamanho):
        self.tam = tamanho
        self.quant = 0
        self.vetor = [None] * self.tam
    def inserir_fim(self, valor):
        self.vetor[self.quant] = valor
        self.quant += 1
        