class No:
    def __init__(self, valor, proximo):
        self.info = valor
        self.prox = proximo

class FilaD:
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0

    def inserir(self, valor):
        novo = No(valor, None)
        if self.quant == 0:
            self.prim = self.ult = No(valor, None)
        else:
            self.ult.prox = self.ult = No(valor, None)
        self.quant += 1

    def inserirV(self, *valores):
        for i in valores:
            self.inserir(i)
    
    def remover(self):
        if self.quant == 0:
            return None
        valor = self.prim.info
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.prim = self.prim.prox
        self.quant -= 1
        return valor

    def ver_primeiro(self):
        if self.quant == 0:
            return None
        return self.prim.info

    def esta_vazio(self):
        return self.quant == 0

    def show(self):
        aux = self.prim
        for i in range(self.quant):
            print(f'Valor: {aux.info} | Quant: {i}')
            aux = aux.prox
