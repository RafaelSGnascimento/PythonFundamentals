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
