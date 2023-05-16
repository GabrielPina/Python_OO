
class Conta:

    # função construtora, self é a nossa referencia
    def __init__(self,numero,titular,saldo,limite):
        print("Construindo obejto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        #self.__codigo_banco = "001"
        # quando eu coloco __ antes da atributo, eu informo que ela é uma atributo privada

# FUNÇÃO = METODOS É O QUE O OBJETO SABE FAZER
# ATRIBUTOS SÃO AS CARACTERISTICAS (É O QUE TEM)

    def extrato(self):
        print("Saldo de {} do Titular {}".format(self.__saldo, self.__titular))

    def depositar(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar): # METODO PRIVADO
        valor_disponivel_para_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_para_sacar

    def sacar(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite da conta".format(valor))
# PARA UTILIZAR, TEMOS QUE REFERENCIAR NO TERMINAL, OU SEJA, conta.extrato(), conta.depositar(VALOR) e conta.sacar(valor)

    def transferir(self, valor, destino): # A ORIGEM SEMPRE VAI SER A REFERENCIA conta2.transferir(30.0, conta) -> conta2 SERÁ A ORIGEM
        self.sacar(valor)
        destino.depositar(valor)

    # OS METODOS GETTERS SÃO RESPONSAVEIS POR RETORNAR ALGO.
    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    # OS SETTERS SÃO RESPONSAVEIS POR ACESSAR E RECEBER
    @limite.setter
    def limite(self,limite): # SET NUNCAAAA RETORNA NADAAAAA, ELE MUDA/ALTERA ALGO, NESSE CASO IREMOS ALTERAR O LIMITE
        self.__limite = limite

    @staticmethod # METODO ESTATICO, NÃO PRECISA DO SELF E O VALOR É PRE DEFINIDO
    def codigo_banco():
        return "001"

    @staticmethod #USANDO UM DICIONARIO
    def codigos_bancos():
        return {'BB': '001','Caixa': '104','Bradesco':'237'}