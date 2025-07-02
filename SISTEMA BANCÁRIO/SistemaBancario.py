import re


class Pessoa:
    __todas_as_pessoas = []

    __todas_as_contas = []

    def __init__(self, nome, sobrenome, idade, cpf):
        self.nome = nome  # STRING
        self.sobrenome = sobrenome  # STRING
        self.idade = idade  # INT
        self.__cpf = cpf  # STRING
        self.__contas_bancarias = []

    def __eq__(self, other):
        if isinstance(other, Pessoa):
            return (self.nome == other.nome and
                    self.sobrenome == other.sobrenome and
                    self.idade == other.idade and
                    self.cpf == other.cpf)

        return False

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, novo_cpf):
        self.__cpf = novo_cpf

    @property
    def contas_bancarias(self):
        return self.__contas_bancarias

    ############
    # isinstance() é uma função que testa se
    # um objeto é uma instância de uma
    # DETERMINADA (qualquer) classe ou de uma subclasse dela

    @contas_bancarias.setter
    def contas_bancarias(self, nova_conta_bancaria):
        if isinstance(nova_conta_bancaria, ContaBancaria):
            if not self.__contas_bancarias:
                self.__contas_bancarias.append(nova_conta_bancaria)
            else:
                if nova_conta_bancaria not in self.__contas_bancarias:
                    self.__contas_bancarias.append(nova_conta_bancaria)

    # CLASSMETHOD's

    @classmethod
    def criar_pessoa(cls):

        while True:

            lista_de_pessoas = Pessoa.buscar_pessoa()
            val = Validacoes()
            validar_pessoa = {'Nome': val.validar_nome,
                              'Sobrenome': val.validar_sobrenome,
                              'Idade': val.validar_idade,
                              'CPF': val.validar_cpf}

            print('CADASTRO DE CLIENTE\n')

            print(f'Ex. de CPF: 000.000.000-00 \n')

            dados_pessoa = []

            for chave, funcao in validar_pessoa.items():
                while True:

                    dado = input(f'Digite o(a) {chave} do cliente: ')

                    validacao = funcao(dado)
                    if validacao:
                        dados_pessoa.append(dado)
                        break
                    else:
                        print(f'{chave} inválido(a)')

            nova_pessoa = Pessoa(dados_pessoa[0], dados_pessoa[1], dados_pessoa[2], dados_pessoa[3])

            interface = Interface()
            if not lista_de_pessoas:
                lista_de_pessoas.append(nova_pessoa)
                print('Cliente cadastrado com sucesso!')
                print(lista_de_pessoas)

                interface.menu()

            else:
                if nova_pessoa not in lista_de_pessoas:

                    lista_de_pessoas.append(nova_pessoa)
                    print('Cliente cadastrado com sucesso!')
                    print(lista_de_pessoas)

                    interface.menu()
                    break
                else:
                    print('Cliente já existe')

    @classmethod
    def buscar_cpf(cls, cpf):

        for pessoa in cls.__todas_as_pessoas:
            if cpf == pessoa.cpf:
                return pessoa.nome, pessoa.sobrenome, pessoa.idade, pessoa.cpf
            else:
                return "Cliente não existe"

    @classmethod
    def buscar_conta(cls):
        return cls.__todas_as_contas

    def info(self):
        return (f'\nCLIENTE\n'
                f'Nome: {self.nome}'
                f'Sobrenome: {self.sobrenome}'
                f'CPF: {self.__cpf}'
                f'Idade: {self.idade}')

    def info_contas(self):  # IMPLEMENTAR TIPO DE CONTA
        if self.__contas_bancarias:
            print(f'\nContas do titular {self.nome}\n')
            for conta in self.__contas_bancarias:
                return (f'\nNome do Banco: {conta.Banco.nome}'
                        f'Nº do Banco: {conta.Banco.nro_banco}\n'
                        f'Nº da Conta: {conta.nro_conta}\n'
                        f'Saldo total: {conta.saldo:.2f}\n')
        else:
            return f'Não existem contas cadastradas neste CPF.'


class Banco:
    todos_os_bancos = []

    todas_contas_de_Banco = []  # TODAS AS CONTAS DE TODOS OS BANCOS, PRA BUSCA.

    def __init__(self, nome, cnpj, nro_banco):
        self.__nome = nome
        self.__cnpj = cnpj
        self.__nro_banco = nro_banco
        self.__contas_bancarias = []

    @property
    def nome(self):  # STRING
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
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

    @property
    def contas_bancarias(self):
        return self.__contas_bancarias

    @contas_bancarias.setter
    def contas_bancarias(self, nova_conta_bancaria):

        if isinstance(nova_conta_bancaria, ContaBancaria):

            if not self.__contas_bancarias:
                self.__contas_bancarias.append(nova_conta_bancaria)

            else:
                if nova_conta_bancaria not in self.__contas_bancarias:
                    self.__contas_bancarias.append(nova_conta_bancaria)

    # CLASSMETHOD's
    @classmethod
    def criar_banco(cls):
        # self,titular,banco,nro_conta,saldo,senha

        while True:

            lista_de_bancos = Banco.buscar_banco()

            val = Validacoes()
            validar_banco = {'Nome': val.validar_nome,
                             'CNPJ': val.validar_cnpj,
                             'Número': val.validar_nro_banco}

            print('CADASTRO DE BANCO\n')

            print(f'Ex. de CNPJ: " 00.000.000/0000-00 "\n'
                  f'Ex. de número de Banco: 0000 (4 dígitos)\n')

            dados_banco = []

            for chave, funcao in validar_banco.items():
                while True:

                    dado = input(f'Digite o(a) {chave} do Banco: ')

                    validacao = funcao(dado)

                    if validacao:
                        dados_banco.append(dado)
                        break
                    else:
                        print(f'{chave} inválido(a)')

            novo_banco = Banco(dados_banco[0], dados_banco[1], dados_banco[2])

            interface = Interface()
            if not lista_de_bancos:
                lista_de_bancos.append(novo_banco)
                print('Banco cadastrado com sucesso!')

                interface.menu()

            else:
                if novo_banco not in lista_de_bancos:

                    lista_de_bancos.append(novo_banco)
                    print('Banco cadastrado com sucesso!')

                    interface.menu()
                    break
                else:
                    print('Banco já existe')

    def info_banco(self):
        print(f"\nINFORMAÇÕES DO BANCO\n:")
        return (f'\nNome: {self.nome}\n'
                f'Nº do Banco: {self.nro_banco}\n'
                f'CNPJ: {self.cnpj}\n')

    @classmethod
    def info_contas(cls):

        if not cls.todas_contas_de_Banco:
            print(f'\nNão existem contas cadastradas.\n')
            return Interface().menu()
        else:
            print('\nLISTA GERAL DE CONTAS:\n')

            for conta in cls.todas_contas_de_Banco:
                print(f'\nTitular: {conta.Pessoa.nome}\n'
                      f'Nome do Banco: {conta.Banco.nome}\n'
                      f'Nº Conta: {conta.nro_conta}\n'
                      f'Tipo de conta: {conta.tipo}\n'
                      f'Saldo total: {conta.saldo:.2f}')

            return f'\n{Interface().menu()}'

    @classmethod
    def buscar_banco(cls, nro_banco):

        for banco in cls.todos_os_bancos:
            if nro_banco == banco.nro_banco:
                return banco.nome, banco.cnpj, banco.nro_banco
            else:
                return "Banco não existe"

    @classmethod
    def buscar_conta(cls):
        return cls.todas_contas_de_Banco

    @classmethod
    def adicionar_conta(cls, nova_conta):
        cls.todas_contas_de_Banco.append(nova_conta)

    @classmethod
    def fechar_conta(cls):
        return cls.todas_contas_de_Banco  #####################

    def __eq__(self, other):
        if isinstance(other, Banco):
            return (self.nome == other.nome and
                    self.cnpj == other.cnpj and
                    self.nro_banco == other.nro_banco)

        return False


class ContaBancaria:
    todas_as_contas = []

    def __init__(self, titular, banco, nro_conta, saldo, senha):
        self._titular = titular  # Objeto Pessoa
        self._banco = banco  # Objeto Banco
        self._nro_conta = nro_conta
        self._saldo = saldo
        self._senha = senha

    # Atributos protegidos por decoradores:
    def __str__(self):
        return (f"Banco: {self.banco.nome}\n"
                f"Nº Banco: {self.banco.nro_banco}\n"
                f"Titular: {self._titular.nome}\n"
                f"Conta: {self._nro_conta}\n"
                f"Saldo: {self.saldo}")

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, novo_titular):
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

    # CLASSMETHOD's

    @classmethod
    def cadastrar_conta(cls):
        while True:

            print(f'\nEx. de CPF: 000.000.000-00 \n'
                  f'Número de Banco deve conter 4 dígitos numéricos\n'
                  f'Número da conta deve conter 10 digitos numéricos\n'
                  f'A senha deve ser númerica com 4 dígitos')

            # titular,banco,nro_conta,saldo,senha
            interface = Interface()
            lista_de_contas = ContaBancaria.buscar_conta()
            val = Validacoes()
            validar_conta = {'CPF': val.validar_cpf,
                             'Número do Banco': val.validar_nro_banco,
                             'Número da Conta': val.validar_nro_conta,
                             'Senha': val.validar_senha
                             }

            dados_conta = []

            for chave, funcao in validar_conta.items():
                while True:

                    dado = input(f'Digite o(a) {chave}: ')

                    validacao = funcao(dado)
                    if validacao:
                        dados_conta.append(dado)
                        break
                    else:
                        print(f'{chave} inválido(a)')

            tipo_de_conta = None
            while True:

                print(f'\n1- Conta Corrente\n'
                      f'2- Conta Poupança\n')

                tipo = input('\nDigite o tipo de conta: ')

                if tipo.lower() == "1":
                    tipo_de_conta = "corrente"
                    break

                elif tipo.lower() == "2":
                    tipo_de_conta = "poupança"
                    break

                else:
                    print('INVÁLIDO')

            # preciso verificar se o cpf existe na classe Pessoa(além da função de validação).

            titular_atual = None  # <<<<
            banco_atual = None  # <<<<

            pessoa = Pessoa.buscar_cpf(dados_conta[0])
            banco = Banco.buscar_banco(dados_conta[1])
            conta = ContaBancaria.buscar_conta(dados_conta[2])

            if pessoa:

                if banco:

                    if not conta:

                        if tipo_de_conta.lower() == 'corrente':

                            conta_atual = ContaCorrente(pessoa, banco, dados_conta[2], 0.0, dados_conta[3],
                                                        0.0)

                            ContaBancaria.adicionar_conta(conta_atual)
                            Banco.adicionar_conta(conta_atual)
                            ContaCorrente.adicionar_conta_corrente(conta_atual)

                        if tipo_de_conta.lower() == 'poupanca':
                            conta_atual = ContaPoupanca(pessoa, banco, dados_conta[2], 0.0, dados_conta[3],
                                                        0.0,0.0)

                            ContaBancaria.adicionar_conta(conta_atual)
                            Banco.adicionar_conta(conta_atual)
                            ContaPoupanca.adicionar_conta_poupanca(conta_atual)




    @classmethod
    def adicionar_conta(cls, nova_conta):
        cls.todas_as_contas.append(nova_conta)


    @classmethod
    def buscar_conta(cls, nro_conta):
        for conta in cls.todas_as_contas:
            if nro_conta == conta.nro_conta:
                return "Conta Já existe"


def saque(self):
    pass


def deposito(self):
    pass


def verificar_senha(self):
    pass


class ContaCorrente(ContaBancaria):
    contas_correntes = []

    def __init__(self, pessoa, banco, nro_conta, saldo, senha, taxas_mensais):
        super().__init__(pessoa, banco, nro_conta, saldo, senha)

        self.__taxas_mensais = taxas_mensais

    # Atributos Protegidos
    @property
    def taxas_mensais(self):
        return self.__taxas_mensais

    @taxas_mensais.setter
    def taxas_mensais(self, nova_taxas_mensais):
        self.__taxas_mensais = nova_taxas_mensais

    # Métodos da Classe
    @classmethod
    def criar_conta_corrente(cls):
        pass

    @classmethod
    def adicionar_conta_corrente(cls, nova_conta_corrente):

        if not cls.contas_correntes:
            cls.contas_correntes.append(nova_conta_corrente)
        else:
            if nova_conta_corrente not in cls.contas_correntes:
                cls.contas_correntes.append(nova_conta_corrente)
            else:
                return f'Conta já existe.'

    def info(self):
        pass

    def novo_mes(self):
        pass


class ContaPoupanca(ContaBancaria):
    contas_poupanca = []

    def __init__(self, pessoa, banco, nro_conta, saldo, senha, rendimentos, saques_mensais):
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

    @classmethod
    def adicionar_conta_poupanca(cls, nova_conta_poupanca):
        if not cls.contas_poupanca:
            cls.contas_poupanca.append(nova_conta_poupanca)
        else:
            if nova_conta_poupanca not in cls.contas_poupanca:
                cls.contas_poupanca.append(nova_conta_poupanca)

    def info(self):
        pass

    def novo_mes(self):
        pass

    def saque(self):
        pass


class Interface:

    def __init__(self):
        pass

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
                        Banco.criar_banco()

                    case 2:
                        Pessoa.criar_pessoa()

                    case 3:
                        self.cadastrar_conta()


            except ValueError:
                print('\nEntrada Inválida! Somente números inteiros.')

    def listar_bancos(self):
        # 1 - acessar a lista de bancos
        # 2 - iterar sobre a lista
        # 3 - retornar a lista usando um for.
        pass


class Validacoes:

    def validar_nome(self, valor):
        return bool(re.fullmatch(r"[A-Z a-zÀ-ÿ\s]+", valor))
        # letras de a a-z maiúsculas ou mínusculas e símbolos

    def validar_sobrenome(self, valor):
        return bool(re.fullmatch(r"[A-Za-zÀ-ÿ\s]+", valor))

    def validar_idade(self, valor):
        return valor.isdigit()

    def validar_cpf(self, valor):
        return re.fullmatch(r"[0-9]{3}.[0-9]{3}.[0-9]{3}-[0-9]{2}", valor)

    def validar_senha(self, valor):
        return re.fullmatch(r'[0-9]{4}', valor)

    def validar_cnpj(self, valor):
        return re.fullmatch(r'[0-9]{2}.[0-9]{3}.[0-9]{3}/[0-9]{4}-[0-9]{2}', valor)

    def validar_nro_conta(self, valor):
        return re.fullmatch(r'[0-9]{10}', valor)

    def validar_nro_banco(self, valor):
        return re.fullmatch(r'[0-9]{4}', valor)

    def validar_saldo(self, valor):
        try:
            float(valor)
            return True
        except ValueError:
            return False


if __name__ == '__main__':
    Interface().menu()
