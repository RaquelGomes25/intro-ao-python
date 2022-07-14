# Crie uma classe que modele o objeto "carro".
# Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
# Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.
class Carro:
    def _init_(self, cor, modelo):
        self.ligado = False
        self.cor = cor
        self.modelo = modelo
        self.velocidade = 0
        self.velocidade_min = 1
        self.velocidade_max = 150

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def acelerar_carro(self):
        if not self.ligado:  # testa se a tv esta ligada
            return

        if self.velocidade < self.velocidade_max:
            self.velocidade += 1

    def reduzir_carro(self):
        if not self.ligado:
            return

        if self.velocidade > self.velocidade_min:
            self.velocidade -= 1


# Crie uma instância da classe carro.
carro_passeio = Carro("amarelo", "camaro")
carro_trabalho = Carro("vermelho", "mustang")


# Faça o carro "andar" utilizando os métodos da sua classe.
carro_passeio.ligar()
carro_passeio.acelerar_carro()

# Faça o carro "parar" utilizando os métodos da sua classe.
carro_passeio.desligar()
