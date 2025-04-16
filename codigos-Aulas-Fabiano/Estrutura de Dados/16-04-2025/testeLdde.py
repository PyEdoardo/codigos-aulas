import Ldde

lista = Ldde.Ldde() #Instânciamos uma classe Ldde

lista.inserir_fim(1) #Função que insere no último nó da lista
lista.inserir_fim(2)
lista.inserir_fim(3)
lista.inserir_fim(4)
lista.inserir_fim(5)
lista.inserir_fim(6)
lista.inserir_fim(7)
#Após a inserção a lista deve estar assim [1,2,3,4,5,6,7]
lista.remover_extremidades() #Na remoção, o self.prim irá apontar para o self.prim.prox, e o self.ult irá apontar para o self.ult.ant, e diminuindo 2 no quant.
lista.show() #Deverá printar [2,3,4,5,6]
