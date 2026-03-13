class Bicicleta:
    def __init__(self,cor,modelo,ano,valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor



    def parar(self):
        print("A bicicleta parou")

    def acelerar(self):
        print("A bicicleta acelerou")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

b1 = Bicicleta("vermelha","caloi",2020,1500)
b2 = Bicicleta("azul","monark",2018,1200)
b3 = Bicicleta("preta","caloi",2021,2000)
b4 = Bicicleta("verde","monark",2019,1800)
b5 = Bicicleta("amarela","caloi",2022,2500)
b6 = Bicicleta("roxa","monark",2020,1600)
b7 = Bicicleta("laranja","caloi",2017,1000)
b8 = Bicicleta("rosa","monark",2021,2200)
b9 = Bicicleta("cinza","caloi",2019,1700)