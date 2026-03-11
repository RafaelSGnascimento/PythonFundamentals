class animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        return "O animal faz um som"
    
class mamifero(animal):
    pass

class ave(animal):
    pass

class cachorro(mamifero):
    pass

class gato(mamifero):
    pass

class papagaio(ave):    
    pass

cachorro1 = cachorro("Rex")
gato1 = gato("Mia")
papagaio1 = papagaio("Loro")