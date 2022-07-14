# O banco Banco Delas é um banco moderno e eficiente, com vantagens exclusivas para clientes mulheres.
# Modele um sistema orientado a objetos para representar contas correntes em do Banco Delas seguindo os requisitos abaixo.

# 1. Cada conta corrente pode ter um ou mais clientes como titular.
# 2. O banco controla apenas o nome, o telefone e a renda mensal de cada cliente.
# 3. A conta corrente apresenta um saldo e uma lista de operações de saques e depósitos.
#    Quando a cliente fizer um saque, diminuiremos o saldo da conta corrente. Quando ela
#    fizer um depósito, aumentaremos o saldo.
# 4. Clientes mulheres possuem em suas contas um cheque especial de valor igual à sua renda
#    mensal, ou seja, elas podem sacar valores que deixam a sua conta com valor negativo até
#    -renda_mensal.
# 5. Clientes homens por enquanto não têm direito a cheque especial.

# Para modelar seu sistema, utilize obrigatoriamente os conceitos "classe", "herança" e "polimorfismo".
# Opcionalmente, você pode também utilizar "propriedades", "encapsulamento" e "classe abstrata".
class Cliente():
    def _init_(self, nome, telefone, genero, renda_mensal):
        self._nome = nome
        self.telefone = telefone
        self.genero = genero
        self.renda_mensal = renda_mensal

    def _str_(self):
        return f'Cliente: {self._nome}, Telefone: {self.telefone}, Genero: {self.genero}, Renda Mensal: {self.renda_mensal}'


class Conta(Cliente):
    def _init_(self, nome,  genero, renda_mensal, saldo=0):
        super()._init_(nome, genero, renda_mensal)
        self.saldo = 0
        self.correntista = nome
        self.operações = [("DEPOSITO", saldo)]

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operações += [("SAQUE", valor)]
        else:
            print("Saldo insuficiente")

    def deposito(self, valor):
        self.saldo += valor
        self.operações += {("DEPOSITO", valor)}

    def extrato(self):
        print("EXTRATO: ")
        for op in self.operacoes:
            print("%10s %10.2f\n" % (op[0], op[1]))
        print("\n Saldo: %10.2f\n" % self.saldo)


class ChequeEspecial(Conta):
    def _init_(self, nome,  genero, renda_mensal, saldo=0):
        super()._init_(self, nome, genero, renda_mensal, saldo)
        self.limite = renda_mensal

    def saque(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.operações.append[("SAQUE", valor)]
            return True
        else:
            return self.saque(valor)


cliente1 = Cliente("Mariana", 71999999999, "F", 5000)
conta = ChequeEspecial([cliente1], 1000)
