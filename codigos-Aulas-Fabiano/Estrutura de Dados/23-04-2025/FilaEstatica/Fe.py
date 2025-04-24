class Fe: #Fifo | First In - First Out | Funcoes init, inserir, remover, ver_primeiro e esta cheia que é opcional e esta vazia
    def __init__(self, tamanho):
        self.tam = tamanho
        self.quant = 0
        self.vetor = [None] * self.tam
    
    def inserir(self, valor):
        self.vetor[self.quant] = valor
        self.quant += 1
    
    def remover(self):
        for i in range(self.quant - 1):
            self.vetor[i] = self.vetor[i + 1]
        self.quant -= 1

    def esta_cheia(self):
        return self.quant == self.tam
    
    def esta_vazia(self):
        return self.quant == 0

    def ver_primeiro(self):
        return self.vetor[0]

    def show(self): #Apenas pra teste
        for i in range(self.quant):
            print(f'Pos: {i} | Valor: {self.vetor[i]}')
    