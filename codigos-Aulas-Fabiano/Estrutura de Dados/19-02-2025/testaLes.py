import les

l = les.Les(5)

l.inserir_inicio("A")
l.inserir_inicio("B")
l.inserir_inicio("C")
l.inserir_fim("D")
# l.show()

# l.remover_inicio()
# l.remover_inicio()
# l.show()
print(l.get_quant())
l.duplicar_quant()
l.show()
print(l.get_quant())
