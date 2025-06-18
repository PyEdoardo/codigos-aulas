class No:
    def __init__(self, valor):
        self.esq = None
        self.dir = None
        self.info = valor

    def insere(self, valor):
        if valor < self.info:
            if self.esq == None:
                self.esq = No(valor)
            else:
                self.esq.insere(valor)

        else:
            if self.dir == None:
                self.dir = No(valor)
            else:
                self.dir.insere(valor)

    def busca(self, valor):
        if valor == self.info:
            return True
        elif valor < self.info:
            if self.esq == None:
                return False
            else:
                return self.esq.busca(valor)
        else:
            if self.dir == None:
                return False
            else:
                return self.dir.busca(valor)
    
    def nivel(self, valor):
        if valor == self.info:
            return 1
        elif valor < self.info:
            if self.esq == None:
                return False
            else:
                return self.dir.nivel(valor) + 1
        else:
            if self.dir == None:
                return False
            else:
                return self.dir.nivel(valor) + 1
            
    def maior_val(self):
        if self.dir != None:
            return self.dir.maior_val()
        else:
            return self.info
        


class Tree:
    def __init__(self):
        self.raiz = None
    
    def insere(self, valor):
        if self.raiz == None:
            self.raiz = No(valor)
        else:
            return self.raiz.insere(valor)
    
    def busca(self, valor):
        if self.raiz == None : return False
        else:
            return self.raiz.busca(valor)

    def nivel(self, valor):
        if self.raiz == None:
            return False
        else:
            return self.raiz.nive(valor) - 1
        
    def maior_val(self):
        if self.raiz == None:
            return 0
        else:
            return self.raiz.maior_val()

    def menor_val(self):
        if self.raiz == None:
            return 0
        else:
            return self.raiz.menor_val()

    #Só serve pra teste e inserir vários valores de uma vez.
    def insereV(self, *valores):
        for valor in valores:
            self.insere(valor)