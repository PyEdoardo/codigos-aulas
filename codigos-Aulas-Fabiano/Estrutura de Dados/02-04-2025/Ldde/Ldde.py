class No:
    def __init__(self, anterior, valor, proximo):
        self.info = valor
        self.ant = anterior
        self.prox = proximo

class Ldde:
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0
    
    def inserir_inicio(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(None, valor, None)
        else:
            #self.prim = self.prim.prox.ant = No(None, valor, self.prim)
            self.prim.ant = self.prim = No(None, valor, self.prim)
        self.quant += 1
    
    def inserir_final(self, valor):
        if self.quant == 0:
            self.prim = self.ult = No(None, valor, None)
        else:
            self.ult.prox = self.ult = No(self.ult, valor, None)
        self.quant += 1
    
    def remover_inicio(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.prim = self.prim.prox
            self.prim.ant = None
        self.quant -= 1
    
    def remover_final(self):
        if self.quant == 1:
            self.prim = self.ult = None
        else:
            self.ult = self.ult.ant
            self.ult.prox = None
        self.quant -= 1

    def show(self):
        aux = self.prim
        for i in range(self.quant):
            print(f'Valor: {aux.info} | Quant: {i}')
            aux = aux.prox
    
    #Teste
    def show_inverso(self):
        aux = self.ult
        for i in range(self.quant):
            print(f'Valor: {aux.info} | Quant: {i}')
            aux = aux.ant

    def remover_val(self, valor):
        aux = self.prim
        ant = None
        while aux is not None:
            if aux.info != valor:
                ant = aux
                aux = aux.prox
            else:
                ant.prox = aux.prox
                ant.ant = aux.ant
                self.quant -= 1
                return
    
        
                