import re

class Pessoa:
    __pessoas = []

    def __init__(self, nome, sobrenome, idade: int, cpf):
        self.nome = nome            #STRING
        self.sobrenome = sobrenome  #STRING
        self.idade = idade          #INT
        self.__cpf = cpf            #STRING
        self.__contas_bancarias = []

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, novo_cpf):
        self.__cpf = novo_cpf

    def __eq__(self, other):
        if isinstance(other, Pessoa):
            return (self.nome == other.nome and
                    self.sobrenome == other.sobrenome and
                    self.idade == other.idade and
                    self.cpf == other.cpf)

        return False


    def info_banco(self):
        pass


    def info_contas(self):
        pass

    @classmethod
    def pessoas(cls):
        return cls.__pessoas

    @classmethod
    def contas_bancarias(cls):
        return cls.__contas_bancarias


class Banco:

    def __init__(self, nome,cnpj,nro_banco):
        self.__nome = nome
        self.__cnpj = cnpj
        self.__nro_banco = nro_banco
        self.__contas_banco = []


    #Atributos protegidos por decoradores
    @property
    def nome(self):                 #STRING
        return self.__nome

    @nome.setter
    def nome(self,novo_nome):
        self.__nome = novo_nome

    @property
    def cnpj(self):
        return self.__cnpj

    @cnpj.setter
    def cnpj(self, novo_cnpj):
        self.__cnpj = novo_cnpj

    @property
    def nro_banco(self):
        return self.__nro_banco

    @nro_banco.setter
    def nro_banco(self, novo_nro_banco):
        self.__nro_banco = novo_nro_banco


    #Métodos da classe
    @classmethod
    def info_banco(cls):
        pass

    @classmethod
    def info_contas(cls):
        pass

    @classmethod
    def criar_conta(cls):
        # self,titular,banco,nro_conta,saldo,senha

        lista_pessoas = Pessoa.pessoas()

        val = Validacoes()

        validar_pessoa = {'Nome' : val.validar_nome,
                  'Sobrenome' : val.validar_sobrenome,
                  'Idade' : val.validar_idade,
                  'CPF' : val.validar_cpf}

        cliente_em_codigo = []

        validar_banco = {'Nome' : val.validar_nome,
                         'CNPJ' : val.verifica_cnpj,
                         'Número do Banco' : val.verifica_nro_banco}

        banco_em_codigo = []

        print('\nCADASTRO DE CONTA\n\n')

        #para validar os dados eu acesso as chaves e valores no dicionario
        print('Cadastro Pessoa Física:\n\n')

        dados_pessoa = []
        dados_banco = []

        for chave, funcao in validar_pessoa.items():
            while True:

                pergunta = input(f'Digite seu(a) {chave}: ')

                teste = funcao(pergunta)
                if teste:
                    dados_pessoa.append(pergunta)
                    break
                else:
                    print(f'{chave} inválido(a)')

        nova_pessoa = Pessoa(dados_pessoa[0], dados_pessoa[1], int(dados_pessoa[2]), dados_pessoa[3])

        if not lista_pessoas:
            lista_pessoas.append(nova_pessoa)

        else:
            flag = False
            for i in lista_pessoas:
                if nova_pessoa == i:
                    flag = True

            if flag == False:
                lista_pessoas.append(nova_pessoa)






    @classmethod
    def fechar_conta(cls):
        pass

    def __eq__(self, other):
        if isinstance(other, Banco):
            return (self.nome == other.nome and
                    self.cnpj == other.cnpj and
                    self.nro_banco == other.nro_banco)

        return False

class ContaBancaria:
    def __init__(self,titular,banco,nro_conta,saldo,senha):
        self._titular = titular     #Objeto Pessoa
        self._banco = banco         #Objeto Banco
        self._nro_conta = nro_conta
        self._saldo = saldo
        self._senha = senha



    #Atributos protegidos por decoradores:

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self,novo_titular):
        self._titular = novo_titular

    @property
    def banco(self):
        return self._banco

    @banco.setter
    def banco(self, novo_banco):
        self._banco = novo_banco

    @property
    def nro_conta(self):
        return self._nro_conta

    @nro_conta.setter
    def nro_conta(self, novo_nro_conta):
        self._nro_conta = novo_nro_conta

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, novo_saldo):
        self._saldo = novo_saldo

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, nova_senha):
        self._senha = nova_senha

    @classmethod
    def todas_contas(cls):
        return cls.__todas_contas

    #Métodos da classe
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

    #Atributos Protegidos
    @property
    def taxas_mensais(self):
        return self.__taxas_mensais

    @taxas_mensais.setter
    def taxas_mensais(self,nova_taxas_mensais):
        self.__taxas_mensais = nova_taxas_mensais


    #Métodos da Classe
    def info(self):
        pass

    def novo_mes(self):
        pass

class ContaPoupanca(ContaBancaria):

    def __init__(self, pessoa, banco, nro_conta, saldo, senha, rendimentos,saques_mensais):
        super().__init__(pessoa, banco, nro_conta, saldo, senha)

        self.__rendimentos = rendimentos
        self.__saques_mensais = saques_mensais

    @property
    def rendimentos(self):
        return self.__rendimentos

    @rendimentos.setter
    def rendimentos(self, novo_rendimentos):
        self.__rendimentos = novo_rendimentos

    @property
    def saques_mensais(self):
        return self.__saques_mensais

    @saques_mensais.setter
    def saques_mensais(self, novo_saques_mensais):
        self.__saques_mensais = novo_saques_mensais

    def info(self):
        pass

    def novo_mes(self):
        pass

    def saque(self):
        pass

class Interface:

    def __init__(self):

        self.bancos_cadastrados = []
        self.clientes_cadastrados = []
        self.contas_cadastradas = []

    def menu(self):

        print(f"\n 1 - Cadastrar Banco\n"
              f" 2 - Cadastrar Cliente\n"
              f" 3 - Cadastrar Conta Bancária\n"
              f" 4 - Listar Bancos Cadastrados\n"
              f" 5 - Listar Pessoas Cadastradas\n"
              f" 6 - Listar Contas Cadastradas\n"
              f" 8 - Verificar Senha\n"
              f" 9 - Saque\n"
              f"10 - Depósito\n")

        while True:

            try:
                pergunta_menu_1 = int(input('Digite a Opção desejada: \n'))

                match pergunta_menu_1:

                    case 1:
                        self.cadastrar_banco()

                    case 2:
                        self.cadastrar_cliente()

                    case 3:
                        Banco.criar_conta()


            except ValueError:
                print('\nEntrada Inválida! Somente números inteiros.')

    def cadastrar_banco(self):

        print("Cadastrar Banco")

        nome = input('\nDigite o nome do banco: \n')
        cnpj = input('Digite o CNPJ do banco: \n')
        nro_banco = int(input('Digite o número da conta do banco: \n'))

        novo_banco = Banco(nome, cnpj, nro_banco)
        self.bancos_cadastrados.append(novo_banco)

        print('\nBanco criado.')
        self.menu()


    def cadastrar_cliente(self):

        print("Cadastrar Cliente\n")

        nome = input('\nDigite o nome do cliente: \n')
        sobrenome = input('Digite o sobrenome do cliente: \n')
        idade = int(input('Digite a idade do cliente: \n'))
        cpf = input('Digite o cpf do cliente: \n')

        nova_pessoa = Pessoa(nome, sobrenome, idade, cpf)
        self.clientes_cadastrados.append(nova_pessoa)

        print('Novo cliente criado.')
        self.menu()


    def cadastrar_conta(self):

        self.menu()


    def listar_bancos(self):
#1 - acessar a lista de bancos
#2 - iterar sobre a lista
#3 - retornar a lista usando um for.
        pass

class Validacoes:

    def validar_nome(self,valor):
        return bool(re.fullmatch(r"[A-Za-zÀ-ÿ\s]+", valor))

    def validar_sobrenome(self,valor):
        return bool(re.fullmatch(r"[A-Za-zÀ-ÿ\s]+", valor))

    def validar_idade(self,valor):
        return valor.isdigit()

    def validar_cpf(self, valor):
        return re.fullmatch(r"\d{11}", valor)

    def validar_senha(self,valor):
        return valor.isdigit()

    def verifica_cnpj(self,valor):
        return re.match(r'[0-9]{2}\.[0-9]{3}\.[0-9]{3}\/[0-9]{4}\-[0-9]{2}', valor)

    def verifica_nro_conta(self,valor):
        return valor.isdigit()

    def verifica_nro_banco(self,valor):
        return valor.isdigit()

    def verifica_saldo(self,valor):
        try:
            float(valor)
            return True
        except ValueError:
            return False




if __name__ == '__main__':

    Interface().menu()
