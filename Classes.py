class Banco:
    def __init__(self, nomebanco):
        self.nomebanco = nomebanco
        self.cliente = {}

    def criar_conta(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo
        self.cliente[self.nome] = [self.saldo]


    def sacar(self, conta, valor):
        self.conta = conta
        if conta in self.cliente and valor < self.saldo in self.cliente[self.nome] == [self.saldo]:
                self.saldo = self.saldo - valor
                print("realizado")
        else: 
            print("Não foi possivel")




    def depositar(self, conta, valor):
        self.conta = conta
        self.valor = valor

        for conta in self.cliente and valor < self.saldo in self.cliente[self.nome] == [self.saldo]:
            self.saldo = self.saldo + valor



    def transferir(self, origem, destino, valor):
        if self.saldo in origem > valor:
            destino += valor and origem - valor

    def listar(self):
        for chave, valor in self.cliente.items():
            print (f"nome: {chave} \n saldo: {valor}")

    
        
