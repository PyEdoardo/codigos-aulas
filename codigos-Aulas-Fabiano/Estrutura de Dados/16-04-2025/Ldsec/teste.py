import Ldsec

lista = Ldsec.Ldsec() #Instância da Classe Ldsec

lista.inserir_fim(1) #Lista = None < 1 > None
lista.inserir_fim(2) #Lista = 1 <-> 2
lista.inserir_fim(3) #Lista = 1 <-> 2 <-> 3, com 3 apontando para 1
lista.inserir_fim(4) #Lista = 1 <-> 2 <-> 3 <-> 4, com 4 apontando para 1

#Após as inserções, deverá ficar assim 4 < 1 <-> 2 <-> 3 <-> 4 > 1
#Com 1 sendo prim, e a função irá recursivamente até o prox de algum nó ser igual o self.prim
#Nesse caso ele e o ultimo e irá "virar o ult" e uma variavel auxiliar irá criar o nó no ultimo e apontar para o prim deixando a lista circular

lista.show() #Saida experada = 1, 2, 3, 4
