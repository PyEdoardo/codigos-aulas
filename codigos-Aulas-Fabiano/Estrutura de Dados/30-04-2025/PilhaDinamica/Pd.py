class No:
    def __init__(self, valor, proximo):
        self.info = valor
        self.prox = proximo

class Pd:

    def __init__(self):
        self.topo = None
        self.quant = 0

    def push(self, valor):
        self.topo = No(valor, self.topo)
        self.quant += 1
    
    def pop(self):
        self.topo = self.topo.prox
        self.quant -= 1

    def ver_topo(self):
        return self.topo.info

    def esta_vazia(self):
        return self.quant == 0

    #Não obrigatório
    def ver_topop(self):
        aux = self.ver_topo()
        self.pop()
        return aux

    #Não usar
    def show(self):
        aux = self.prim
        for i in range(self.quant):
            print(f'Valor: {aux.info} | Quant: {i}')
            aux = aux.prox