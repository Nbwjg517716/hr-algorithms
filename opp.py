#studying classes
class Vendedor():
    def __init__(self, nome):
        self.nome=nome 
        self.vendas=0 


    def vendeu(self, vendas):
        self.vendas= vendas 
    
        print(vendas)

    def bateu_meta(self, meta):
        if self.vendas > meta:
            print(self.nome, "Bateu a meta")
        else:
            print(self.nome, "Não bateu a meta")


vendedor1= Vendedor("lira")
vendedor1.vendeu(10000)
vendedor1.bateu_meta(500)
print(vendedor1.vendeu)

vendedor2= Vendedor("Rafael")
vendedor2.vendeu(600)
vendedor2.bateu_meta(100)
print(vendedor2.bateu_meta)
