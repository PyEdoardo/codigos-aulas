class No:
    def __init__(self, anterior, valor, proximo):
        self.ant = anterior
        self.info = valor
        self.prox = proximo

class Lddec:
    def __init__(self):
        self.prim = self.ult = None
        self.quant = 0
    
    def inserir_inicio(self, valor):
        if self.quant == 0:
            self.ult = self.prim = No(self.ult, valor, self.prim)
        else: 
            self.prim.ant = self.prim = No(self.ult, valor, self.prim)
            self.ult.prox = self.prim
        self.quant += 1
        
    def inserir_final(self, valor):
        if self.quant == 0:
            self.ult = self.prim = No(self.ult, valor, self.prim)
        else:
            self.ult.prox = self.ult = No(self.ult, valor, self.prim)
            self.prim.ant = self.ult
        self.quant += 1
        
        
    def show(self):
        aux = self.prim
        
        #Teste
        prox = aux.prox
        ant = aux.ant
        for i in range(self.quant):
            print(f'Valor: {aux.info} | Próximo: {prox.info} | Anterior: {ant.info}')
            aux = aux.prox
            prox = aux.prox
            ant = aux.ant
            
    def show_inverso(self):
        aux = self.ult
        
        #Teste
        prox = aux.prox
        ant = aux.ant
        for i in range(self.quant):
            print(f'Valor: {aux.info} | Próximo: {prox.info} | Anterior: {ant.info}')
            aux = aux.ant
            prox = aux.prox
            ant = aux.ant
    
    def inserir_valores_final(self, *valores):
        if len(valores) <= 1:
            return
        for i in valores:
            self.ult.prox = self.ult = No(self.ult, i, self.prim)
            self.ult.ant = self.ult
            self.quant += 1