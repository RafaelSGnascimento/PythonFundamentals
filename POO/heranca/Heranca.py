class Veiculo:
    def __init__(self, marca, modelo, ano, cor, valor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.valor = valor

    def ligar(self):
        print(f"O {self.modelo} está ligado.")   
    
    def desligar(self):
        print(f"O {self.modelo} está desligado.")   

    def acelerar(self): 
        print(f"O {self.modelo} está acelerando.")

    def frear(self):
        print(f"O {self.modelo} está freando.")

class Carro(Veiculo): 
    def Drif(self):
        print(f"O {self.modelo} está fazendo drift.")

class Moto(Veiculo):
    def empinar(self):
        print(f"A {self.modelo} está empinando.")   

class Caminhao(Veiculo):
    def carregar(self, carga):
        print(f"O {self.modelo} está carregando {carga}.")

moto = Moto("Honda", "CB500", 2021, "preta", 25000)
carro = Carro("Toyota", "Corolla", 2020, "prata", 80000)
caminhao = Caminhao("Volvo", "FH16", 2019, "branca", 300000)

moto.ligar()
carro.acelerar()    
caminhao.frear()
caminhao.carregar("carga pesada")
moto.empinar()
carro.Drif()