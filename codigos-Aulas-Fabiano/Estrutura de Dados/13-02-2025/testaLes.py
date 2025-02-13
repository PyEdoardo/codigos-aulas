import les

l = les.Les(5)

print("Antes remover")
l.inserir_fim("A")
l.inserir_fim("B")
l.inserir_fim("C")
l.inserir_fim("D")

if not l.esta_cheia():
    l.inserir_fim("E")
else:
    print("Está cheia")

if not l.esta_vazia():
    l.inserir_fim("F")
else:
    print("Está cheio")




