class Pessoa:
    def __int__(self, nome, sobrenome, idade, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.__cpf = cpf
        self.__contas_bancarias = []

    def info_banco(self):
        pass

    def info_contas(self):
        pass

    def criar_conta(self):
        pass

    def fechar_conta(self):
        pass


class Banco:

    def __init__(self, nome,cnpj,nro_banco,contas_bancarias):
        self.__nome = nome
        self.__cnpj = cnpj
        self.__nro_banco = nro_banco
        self.__contas_bancarias = contas_bancarias

    def info_banco(self):
        pass

    def info_contas(self):
        pass

    def criar_conta(self):
        pass

    def fechar_conta(self):
        pass


class ContaBancaria:

    def __init__(self,pessoa,banco,nro_conta,saldo,senha):
        self._pessoa = pessoa
        self._banco = banco
        self._nro_conta = nro_conta
        self._saldo = saldo
        self._senha = senha

    def saque(self):
        pass

    def deposito(self):
        pass

    def verificar_senha(self):
        pass

class ContaCorrente(ContaBancaria):

    def __init__(self,pessoa,banco,nro_conta,saldo,senha,taxas_mensais):
        super().__init__(pessoa,banco,nro_conta,saldo,senha)

        self.__taxas_mensais = taxas_mensais

    def info(self):
        pass

    def novo_mes(self):
        pass


class ContaPoupanca(ContaBancaria):

    def __init__(self, pessoa, banco, nro_conta, saldo, senha, rendimentos,saques_mensais):
        super().__init__(pessoa, banco, nro_conta, saldo, senha)

        self.__rendimentos = rendimentos
        self.__saques_mensais = saques_mensais

    def info(self):
        pass

    def novo_mes(self):
        pass

    def saque(self):
        pass

class Interface:

    def interface(self):
        pass

