class Les:
    def __init__(self, tamanho):
        self.tam = tamanho
        self.quant = 0
        self.vetor = [None] * self.tam

    def inserir_fim(self, valor):
        self.vetor[self.quant] = valor
        self.quant += 1

    def inserir_inicio(self, valor):
        for i in range(self.quant, 0, -1):
            self.vetor[i] = self.vetor[i - 1]
        self.vetor[0] = valor
        self.quant += 1

    def show(self):
        for i in range(self.quant):
            print(self.vetor[i], end=' ')
        print("\n")
    
    def remover_fim(self):
        self.quant -= 1

    def remover_inicio(self):
        for i in range(self.quant - 1):
            self.vetor[i] = self.vetor[i + 1]
        self.quant -= 1
    
    def esta_cheia(self):
        return self.quant == self.tam
    
    def esta_vazia(self):
        return self.quant == 0
    
    ## Teste

    def get_quant(self):
        return self.quant
    
    def buscar_indice(self, valor):
        indice = 0
        for i in range(self.quant):
            if self.vetor[i] == valor:
                indice = int(i)
                return indice

    def inserir_apos(self, valAntes, valDepois):
        indice = self.buscar_indice(valAntes)
        if indice == -1:
            return "Nenhum valor"
        pos_inserir = indice + 1

        i = self.quant

        while i > pos_inserir:
            self.vetor[i] = self.vetor[i - 1]
            i -= 1
        self.vetor[pos_inserir] = valAntes
        self.quant += 1
    
    def inserir_antes(self, valAntes, valDepois):
        indice = self.buscar_indice(valAntes)

        if indice == -1:
            return "Nenhum valor"
        i = self.quant

        while i > indice:
            self.vetor[i] = self.vetor[i - 1]
            i -= 1
        self.vetor[indice] = valDepois
        self.quant += 1