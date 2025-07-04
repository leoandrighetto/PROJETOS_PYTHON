import re

class Pessoa:
    __todas_as_pessoas = []


class Pessoa:
    __todas_as_pessoas = []

    def __init__(self, nome, sobrenome, idade: int, cpf):
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

            print('CADASTRO DE CLIENTE\n')

            print(f'Ex. de CPF: 000.000.000-00 \n')

            val = Validacoes()
            validar_pessoa = {'Nome': val.validar_nome,
                              'Sobrenome': val.validar_sobrenome,
                              'Idade': val.validar_idade,
                              'CPF': val.validar_cpf}

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

            nova_pessoa = Pessoa(dados_pessoa[0], dados_pessoa[1], int(dados_pessoa[2]), dados_pessoa[3])

            busca = Pessoa.buscar_cpf(dados_pessoa[3])

            if not busca:

                cls.__todas_as_pessoas.append(nova_pessoa)
                print('\nCliente Cadastrado.\n')
                Estoque().atualizar_estoque()
                Interface().menu()

            else:
                print('\nCliente já existe\n')

    @classmethod
    def buscar_cpf(cls, cpf):

        for pessoa in cls.__todas_as_pessoas:
            if cpf == pessoa.cpf:
                return pessoa

    def info(self):
        return (f'\nNome: {self.nome}\n'
                f'Sobrenome: {self.sobrenome}\n'
                f'CPF: {self.__cpf}\n'
                f'Idade: {self.idade}\n')

    def info_contas(self):
        if self.__contas_bancarias:
            print(f'\nContas do titular {self.nome}\n')
            for conta in self.__contas_bancarias:
                return (f'\nNome do Banco: {conta.Banco.nome}'
                        f'Nº do Banco: {conta.Banco.nro_banco}\n'
                        f'Nº da Conta: {conta.nro_conta}\n'
                        f'Saldo total: {conta.saldo:.2f}\n')
        else:
            return f'Não existem conta cadastradas neste CPF.'

    @classmethod
    def listar_pessoas(cls):

        if cls.__todas_as_pessoas:

            print(f'\nPessoas cadastradas no sistema')

            for pessoa in cls.__todas_as_pessoas:
                print(f'\nNome: {pessoa.nome} {pessoa.sobrenome}\n'
                      f'CPF: {pessoa.cpf}\n'
                      f'Idade: {pessoa.idade}\n')
        else:
            print(f'\nNão existem pessoas cadastradas neste sistema.\n')

    @classmethod
    def retornar_todas_pessoas(cls):

        if cls.__todas_as_pessoas:
            return cls.__todas_as_pessoas

        return False

    def retornar_contas_bancarias(self):
        pass

class Banco:
    __todos_os_bancos = []

    __todas_contas_de_Banco = []  # TODAS AS CONTAS DE TODOS OS BANCOS, PRA BUSCA.

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

        print('\nCADASTRO DE BANCO\n')

        print(f'\nEx. de CNPJ: "00.000.000/0000-00"\n'
              f'Ex. de número de Banco: 0000 (4 dígitos)')

        while True:

            val = Validacoes()
            validar_banco = {'Nome': val.validar_nome,
                             'CNPJ': val.validar_cnpj,
                             'Número': val.validar_nro_banco}

            dados_banco = []

            for chave, funcao in validar_banco.items():
                while True:

                    dado = input(f'\nDigite o(a) {chave} do Banco: ')

                    validacao = funcao(dado)

                    if validacao:
                        dados_banco.append(dado)
                        break
                    else:
                        print(f'{chave} inválido(a)')

            novo_banco = Banco(dados_banco[0], dados_banco[1], dados_banco[2])

            busca = Banco.buscar_banco(dados_banco[2])

            if not busca:
                cls.__todos_os_bancos.append(novo_banco)

                print('\nBanco cadastrado com sucesso!\n')

                Interface().menu()

            else:
                print('Banco já existe')

    @classmethod
    def listar_bancos(cls):
        print(f'\nBancos cadastrados no sistema')

        if cls.__todos_os_bancos:
            for banco in cls.__todos_os_bancos:
                print(f'\nNome: {banco.nome} | CNPJ: {banco.cnpj}\n'
                      f'Nº do Banco: {banco.nro_banco}')
            Interface().menu()

        else:
            print(f'Não existem pessoas cadastradas neste sistema.')
            Interface().menu()

    def info_banco(self):
        print(f"\nINFORMAÇÕES DO BANCO\n:")
        return (f'\nNome: {self.nome}\n'
                f'Nº do Banco: {self.nro_banco}\n'
                f'CNPJ: {self.cnpj}\n')

    @classmethod
    def info_contas(cls):

        if not cls.__todas_contas_de_Banco:
            print(f'\nNão existem contas cadastradas.\n')
            return Interface().menu()
        else:
            print('\nLISTA GERAL DE CONTAS:\n')

            for conta in cls.__todas_contas_de_Banco:
                print(f'\nTitular: {conta.Pessoa.nome}\n'
                      f'Nome do Banco: {conta.Banco.nome}\n'
                      f'Nº Conta: {conta.nro_conta}\n'
                      f'Tipo de conta: {conta.tipo}\n'
                      f'Saldo total: {conta.saldo:.2f}')

            return f'\n{Interface().menu()}'

    @classmethod
    def buscar_banco(cls, nro_banco):

        for banco in cls.__todos_os_bancos:
            if nro_banco == banco.nro_banco:
                return banco.nome, banco.cnpj, banco.nro_banco

    @classmethod
    def buscar_conta(cls):
        return cls.__todas_contas_de_Banco

    @classmethod
    def adicionar_conta(cls, nova_conta):
        cls.__todas_contas_de_Banco.append(nova_conta)

    @classmethod
    def fechar_conta(cls):
        return cls.__todas_contas_de_Banco  #####################

    def __eq__(self, other):
        if isinstance(other, Banco):
            return (self.nome == other.nome and
                    self.cnpj == other.cnpj and
                    self.nro_banco == other.nro_banco)

        return False

class ContaBancaria:
    __todas_as_contas = []

    def __init__(self, titular, banco, nro_conta, senha, saldo: float = 0.0):
        self._titular = titular  # Objeto Pessoa
        self._banco = banco  # Objeto Banco
        self._nro_conta = nro_conta
        self.senha = senha
        self._saldo = saldo

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

        print(f'\nCADASTRO DE CONTA')

        while True:

            print(f'\nEx. de CPF: 000.000.000-00 \n'
                  f'Número de Banco: 4 dígitos numéricos\n'
                  f'Número da conta: 5 digitos numéricos\n'
                  f'A senha deve ser númerica e com 4 dígitos\n')

            # titular,banco,nro_conta,saldo,senha
            interface = Interface()

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
                    tipo_de_conta = "poupanca"
                    break

                else:
                    print('INVÁLIDO')

            pessoa = Pessoa.buscar_cpf(dados_conta[0])
            banco = Banco.buscar_banco(dados_conta[1])
            conta = ContaBancaria.buscar_conta(dados_conta[2])

            if pessoa:

                if banco:

                    if not conta:

                        if tipo_de_conta == 'corrente':
                            conta_atual = ContaCorrente(pessoa, banco, dados_conta[2], dados_conta[3], 0.0,
                                                        0.0)

                            ContaBancaria.adicionar_conta(conta_atual)
                            Banco.adicionar_conta(conta_atual)
                            banco.contas_bancarias = conta_atual
                            pessoa.contas_bancarias = conta_atual
                            
                            
                            #Estoque().atualizar_estoque()

                        if tipo_de_conta == 'poupanca':
                            conta_atual = ContaPoupanca(pessoa, banco, dados_conta[2], dados_conta[3], 0.0,
                                                        0.0, 3)

                            ContaBancaria.adicionar_conta(conta_atual)
                            Banco.adicionar_conta(conta_atual)
                            ContaPoupanca.adicionar_conta_poupanca(conta_atual)
                            pessoa.contas_bancarias = conta_atual
                            #Estoque().atualizar_estoque()

                        print('Conta criada!')
                        interface.menu()

                    else:
                        print('Conta já existe.')
                        interface.menu()

                else:
                    print('Banco não encontrado.')
                    interface.menu()
            else:
                print('\nCPF não identificado no sistema.')
                interface.menu()

    @classmethod
    def listar_contas(cls):
        print(f'\nCONTAS CADASTRADAS NO SISTEMA\n')

        if cls.__todas_as_contas:
            for conta in cls.__todas_as_contas:
                print(f'\nBanco: {conta.banco.nome}'
                      f'\nNº da Conta: {conta.nro_conta}\n'
                  f'Titular: {conta.titular.nome} {conta.titular.sobrenome} \n'
                      f'CPF: {titular.cpf}\n')
            Interface().menu()
        print('Não há contas cadastradas neste sistema\n')

    @classmethod
    def adicionar_conta(cls, nova_conta):
        cls.__todas_as_contas.append(nova_conta)

    @classmethod
    def buscar_conta(cls, nro_conta):
        for conta in cls.__todas_as_contas:
            if nro_conta == conta.nro_conta:
                return "Conta Já existe"

        return False

    @classmethod
    def verifica_senha(cls, conta, senha):

        for contas in cls.__todas_as_contas:
            if conta == contas.nro_conta:

                if senha == contas.senha:
                    return True

        return False

    @classmethod
    def verifica_senha_input(cls):

        val = Validacoes()

        validar_conta = {'Nº Conta': val.validar_nro_conta,
                         'Senha': val.validar_senha}

        dados_validacao = []

        for chave, funcao in validar_conta.items():
            while chave:

                dado = input(f'Digite o(a) {chave}: ')
                teste = funcao(dado)

                if teste:
                    dados_validacao.append(dado)
                    break

                else:
                    print(f'{dado} Inválido')

        for conta in cls.__todas_as_contas:
            if conta.nro_conta == dados_validacao[0]:

                if conta.senha == dados_validacao[1]:
                    return True

        return False

    @classmethod
    def saque(cls, nr_conta, senha, valor):

        try:
            valor = float(valor)

            if ContaBancaria.verifica_senha(nr_conta, senha):

                for conta in cls.__todas_as_contas:

                    if nr_conta == conta.nro_conta:
                        conta.saldo -= valor

                        return (f'Saque Realizado!\n'
                                f'Saldo atual: {conta.saldo}\n\n')

            return f'Saque não realizado, conta ou senhas inexistentes'


        except ValueError:
            return 'valor inválido'

    @classmethod
    def saque_input(cls):

        nr_conta = input('Digite o nº da conta: ')
        senha = input('Digite a senha da conta: ')

        try:
            valor = float(input('Digite o valor do despósito: '))

            if ContaBancaria.verifica_senha(nr_conta, senha):

                for conta in cls.__todas_as_contas:

                    if nr_conta == conta.nro_conta:
                        conta.saldo -= valor

                        return (f'Saque Realizado!\n'
                                f'Saldo atual: {conta.saldo:.2f}\n\n')

            return f'Saque não realizado, conta ou senhas inexistentes'


        except ValueError:
            return 'valor inválido'

    @classmethod
    def deposito(cls, nr_conta, senha, valor: float):

        try:
            valor = float(valor)

            if ContaBancaria.verifica_senha(nr_conta, senha):

                for conta in cls.__todas_as_contas:

                    if nr_conta == conta.nro_conta:
                        conta.saldo += valor

                        return (f'Depósito Realizado!\n'
                                f'Saldo atual: {conta.saldo}\n\n')

            return f'Depósito não realizado, conta ou senhas inexistentes'


        except ValueError:
            return 'valor inválido'

    @classmethod
    def deposito_input(cls):

        nr_conta = input('Digite o nº da conta: ')
        senha = input('Digite a senha da conta: ')

        try:
            valor = float(input('Digite o valor do despósito: '))

            if ContaBancaria.verifica_senha(nr_conta, senha):

                for conta in cls.__todas_as_contas:

                    if nr_conta == conta.nro_conta:
                        conta.saldo += valor

                        return (f'Depósito Realizado!\n'
                                f'Saldo atual: {conta.saldo}\n\n')

            return f'Depósito não realizado, conta ou senhas inexistentes'


        except ValueError:
            return 'valor inválido'


class ContaCorrente(ContaBancaria):
    __contas_correntes = []

    def __init__(self, titular, banco, nro_conta, senha, saldo, taxas_mensais: float = 15.50):
        super().__init__(titular, banco, nro_conta, senha, saldo)

        self.__taxas_mensais = taxas_mensais

    # Atributos Protegidos
    @property
    def taxas_mensais(self):
        return self.__taxas_mensais

    @taxas_mensais.setter
    def taxas_mensais(self, nova_taxas_mensais):
        self.__taxas_mensais = nova_taxas_mensais

    @classmethod
    def adicionar_conta_corrente(cls, nova_conta_corrente):

        if not cls.__contas_correntes:
            cls.__contas_correntes.append(nova_conta_corrente)

        else:
            if nova_conta_corrente not in cls.__contas_correntes:
                cls.__contas_correntes.append(nova_conta_corrente)

    def info(self):
        return (f'\nINFORMAÇÕES SOBRE CONTA\n'
                f'\nTitular: {self.titular.nome}\n'
                f'Banco: {self.banco.nome}\n'
                f'Nº da conta: {self.nro_conta}\n'
                f'Salda: {self.saldo}\n'
                f'Taxas Mensais: {self.taxas_mensais:.2f}\n')

    @classmethod
    def novo_mes(cls):

        nr_conta = input('informe o nº da conta')

        for conta in cls.__contas_correntes:
            if nr_conta == conta.nro_conta:
                conta.saldo -= 15.50

                return (f'\nTaxa atualizada\n'
                        f'Taxa atual: {conta.taxas_mensais:.2f}'
                        f'Saldo atual: {conta.saldo:.2f}')

        return f'Conta não encontrada'


class ContaPoupanca(ContaBancaria):
    __contas_poupanca = []

    def __init__(self, titular, banco, nro_conta, senha, saldo: float = 0.0, rendimentos: float = 0.5,
                 saques_mensais: int = 3):
        super().__init__(titular, banco, nro_conta, senha, saldo)

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
        if not cls.__contas_poupanca:
            cls.__contas_poupanca.append(nova_conta_poupanca)
        else:
            if nova_conta_poupanca not in cls.__contas_poupanca:
                cls.__contas_poupanca.append(nova_conta_poupanca)

    def __str__(self):
        return (f'\nINFORMAÇÕES SOBRE CONTA\n'
                f'\nTitular: {self.titular.nome}\n'
                f'Banco: {self.banco.nome}\n'
                f'Nº da conta: {self.nro_conta}\n'
                f'Saldo: {self.saldo}R$\n'
                f'Taxas Mensais: {self.rendimentos}R$\n'
                f'Saques Mensais: {self.saques_mensais}\n')

    @classmethod
    def novo_mes(cls):

        nr_conta = input('informe o nº da conta')

        for conta in cls.__contas_poupanca:
            if nr_conta == conta.nro_conta:
                saldo_calculado = conta.saldo * (0.5 / 100)

                conta.saldo += saldo_calculado
                conta.saques_mensais = 3

                return (f'\nNovo mês atualizado!\n'
                        f'Saldo anterior: {conta.saldo - saldo_calculado:.2f}'
                        f'Saldo atual (com rendimento de 0.5%): {conta.saldo:.2f}')

        return f'Conta não encontrada'

    @classmethod
    def saque(cls, nr_conta, senha, valor):

        try:
            valor = float(valor)

            if ContaBancaria.verifica_senha(nr_conta, senha):

                for conta in cls.__contas_poupanca:

                    if nr_conta == conta.nro_conta:

                        if conta.saques_mensais > 0 and conta.saldo > 0:
                            conta.saldo -= valor
                            conta.saques_mensais -= 1

                            return (f'Saque Realizado!\n'
                                    f'Saldo atual: {conta.saldo}\n'
                                    f'Qnt saques disponíveis: {conta.saque}\n\n')
                        else:
                            return 'Serviço de saque indisponível.'

            return f'Saque não realizado, conta ou senhas inexistentes'


        except ValueError:
            return 'valor inválido'

    @classmethod
    def saque_input(cls):

        nr_conta = input('Digite o nº da conta: ')
        senha = input('Digite a senha da conta: ')

        try:
            valor = float(input('Digite o valor do saque: '))

            if ContaBancaria.verifica_senha(nr_conta, senha):

                for conta in cls.__contas_poupanca:

                    if nr_conta == conta.nro_conta:

                        if conta.saques_mensais > 0 and conta.saldo > 0:
                            conta.saldo -= valor
                            conta.saques_mensais -= 1

                            return (f'Saque Realizado!\n'
                                    f'Saldo atual: {conta.saldo}\n'
                                    f'Qnt saques disponíveis: {conta.saque}\n\n')
                        else:
                            return 'Serviço de saque indisponível.'

            return f'Saque não realizado, conta ou senhas inexistentes'


        except ValueError:
            return 'valor inválido'


class Validacoes:

    @staticmethod
    def validar_nome(valor):
        return bool(re.fullmatch(r"[A-Z a-zÀ-ÿ\s]+", valor))
        # letras de a a-z maiúsculas ou mínusculas e símbolos

    @staticmethod
    def validar_sobrenome(valor):
        return bool(re.fullmatch(r"[A-Za-zÀ-ÿ\s]+", valor))

    @staticmethod
    def validar_idade(valor):
        return valor.isdigit()

    @staticmethod
    def validar_cpf(valor):
        return re.fullmatch(r"[0-9]{3}.[0-9]{3}.[0-9]{3}-[0-9]{2}", valor)

    @staticmethod
    def validar_senha(valor):
        return re.fullmatch(r'[0-9]{4}', valor)

    @staticmethod
    def validar_cnpj(valor):
        return re.fullmatch(r'[0-9]{2}.[0-9]{3}.[0-9]{3}/[0-9]{4}-[0-9]{2}', valor)

    @staticmethod
    def validar_nro_conta(valor):
        if re.fullmatch(r'[0-9]{5}', valor):
            return int(valor)

    @staticmethod
    def validar_nro_banco(valor):
        valor_str = str(valor)

        if valor_str.isdigit() and len(valor_str) == 4:
            return valor_str

        else:
            return False

    @staticmethod
    def validar_saldo(valor):
        try:
            float(valor)
            return True
        except ValueError:
            return False



class Estoque:

    def atualizar_estoque(self):

        with open ("banco_de_dados.txt", 'w', encoding = 'utf8') as arquivo:

            lista_pessoas = Pessoa.retornar_todas_pessoas()

            for pessoa in lista_pessoas: # acesso todas as pessoas.

                contas_pessoais = []

                if pessoa.contas_bancarias:

                    for contas in pessoa.contas_bancarias: #acessa a conta de cada pessoa pra manipular

                        if isinstance(contas, ContaCorrente):

                            obj_b = contas.banco

                            banco = f'Banco({obj_b.nome},{obj_b.cnpj},{obj_b.nro_banco})'

                            titular = pessoa.cpf

                            corrente = (f'ContaCorrente({titular},{banco},{contas.nro_conta},'
                                        f'{contas.senha},{contas.saldo},{float(contas.taxas_mensais)})')

                            contas_pessoais.append(corrente)

                        if isinstance(contas, ContaPoupanca):
                            obj_b = contas.banco

                            banco = f'Banco({obj_b.nome},{obj_b.cnpj},{obj_b.nro_banco})'

                            titular = pessoa.cpf

                            poupanca = (f'ContaPoupanca({titular},{banco},{contas.nro_conta},{contas.senha},{contas.saldo},'
                                        f'{float(contas.rendimentos)},{int(contas.saques_mensais)})')

                            contas_pessoais.append(poupanca)

                        arquivo.write(f'#{pessoa.nome},{pessoa.sobrenome},{pessoa.cpf},{str(pessoa.idade)},##{";".join(contas_pessoais)}\n')

                arquivo.write(f'#{pessoa.nome},{pessoa.sobrenome},{pessoa.cpf},{str(pessoa.idade)}\n')


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
              f" 7 - Saque\n"
              f" 8 - Depósito\n"
              f" 9 - Simular novo mês\n"
              f"10 - Buscar Cliente\n"
              f"11 - Buscar Banco\n"
              f"12 - Buscar Conta\n")

        while True:

            try:
                pergunta_menu_1 = int(input('Digite a Opção desejada: \n'))

                match pergunta_menu_1:

                    case 1:
                        Banco.criar_banco()

                    case 2:
                        Pessoa.criar_pessoa()

                    case 3:
                        ContaBancaria.cadastrar_conta()

                    case 4:
                        Banco.listar_bancos()

                    case 5:
                        Pessoa.listar_pessoas()

                    case 6:
                        ContaBancaria.listar_contas()

                    case 7:
                        self.saque()

                    case 8:
                        ContaBancaria.deposito_input()

                    case 9:
                        self.novo_mes()

                    case 10:
                        self.buscar_cliente()

                    case 11:
                        self.buscar_banco()

                    case 12:
                        self.buscar_conta()



            except ValueError:
                print('\nEntrada Inválida! Somente números inteiros.')

    @staticmethod
    def saque():
        while True:

            print(f'\n1- Conta Corrente\n'
                  f'2- Conta Poupança\n')

            tipo = input('\nDigite o tipo de conta: ')

            if tipo.lower() == "1":
                ContaBancaria.saque_input()

            elif tipo.lower() == "2":
                ContaPoupanca.saque_input()

            else:
                print('INVÁLIDO')

    @staticmethod
    def novo_mes():
        while True:

            print(f'\n1- Conta Corrente\n'
                  f'2- Conta Poupança\n')

            tipo = input('\nDigite o tipo de conta: ')

            if tipo.lower() == "1":
                ContaCorrente.novo_mes()

            elif tipo.lower() == "2":
                ContaPoupanca.novo_mes()

            else:
                print('INVÁLIDO')

    @staticmethod
    def buscar_cliente():

        print(f'\nBusca de cliente\n'
              f'Exemplo de CPF: 000.000.000-00\n\n')

        per = input('Digite o cpf do cliente: ')

        pessoa = Pessoa.buscar_cpf(per)

        if pessoa:
            print(pessoa.info())
        else:
            print(f'\nPessoa não encontrada\n')


    @staticmethod
    def buscar_banco():
        pass

    @staticmethod
    def buscar_conta():
        pass



if __name__ == '__main__':
    Interface().menu()
