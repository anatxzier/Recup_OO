from Classes import *

banco = Banco("anaju")

def criar():
    print("Para criar uma conta digite o seu nome e saldo")
    nome_cliente = str(input(">> "))
    saldo_cliente = float(input(">> "))
    banco.criar_conta(nome_cliente, saldo_cliente)
    print("Conta criada")

def sacar():
    print("Digite o nome da sua conta e a quantidade do saque")
    conta_cliente = str(input(">> "))
    saque_cliente = float(input(">> "))
    banco.sacar(conta_cliente, saque_cliente)




def main():

    x = True
    while x == True:

            print("Bem vindo ao banco, o que desesa fazer? \n [1] Cria conta \n [2] Saque \n [3] Depositar \n [4] Transferir \n [5] Verificar saldo \n [6] Sair")
            escolha1 = int(input(">> "))

            match escolha1:
                case 1:
                    criar()
                case 2:
                    sacar()
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    banco.listar()
                case 6:
                    print("Saindo...")
                    break
                case _:
                    print("O valor não está disponível")
