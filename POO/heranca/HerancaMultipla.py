class animal:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    
class mamifero(animal):
    def __init__(self, **kw):
        super().__init__(**kw)

class ave(animal):
    def __init__(self, voa, **kw):
        self.voa = voa
        super().__init__(**kw)

    def botarOvo(self):
        print(f"o(a) " + self.nome + " botou um ovo!")

class coruja(ave):
    def spectroPatronum(self):
        print(f"o(a) " + self.nome + " esta agora agindo como seu espirito quardião!")

class cachorro(mamifero):
    def latir(self):
        print("cachorro latiu!")

class gato(mamifero):
    def miar(self):
        print(f"o(a) " + self.nome + " miou!")



cachorro1 = cachorro(nome = "Rex", cor = "marrom")
gato1 = gato(nome = "Mia", cor = "preto")
coruja1 = coruja(nome = "harry", cor = "branca", voa = True)

print(cachorro1)
print(gato1)
print(coruja1)

cachorro1.latir()
gato1.miar()
coruja1.spectroPatronum()
coruja1.botarOvo()