import re

class Pessoa:
    __todas_as_pessoas = []

    def __init__(self, nome, sobrenome, idade: int, cpf):
        self.nome = nome  # STRING
        self.sobrenome = sobrenome  # STRING
        self.idade = idade  # INT
        self.__cpf = cpf  # STRING
        self.__contas_bancarias = []

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, novo_cpf):
        self.__cpf = novo_cpf

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

    def info(self):
        return (f'\nNome: {self.nome}\n'
                f'Sobrenome: {self.sobrenome}\n'
                f'CPF: {self.__cpf}\n'
                f'Idade: {self.idade}\n')

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

    @classmethod
    def info_contas(cls, novo_nro_conta):

        for pessoa in cls.__todas_as_pessoas:
            if pessoa.contas_bancarias:
                for conta in pessoa.contas_bancarias:
                    if conta.nro_conta == novo_nro_conta:
                        return (f'\nNome do Banco: {conta.banco.nome}'
                                f'Nº do Banco: {conta.banco.nro_banco}\n'
                                f'Nº da Conta: {conta.nro_conta}\n'
                                f'Saldo total: {conta.saldo:.2f}\n')

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
        return cls.__todas_as_pessoas

class Banco:
    __todos_os_bancos = []

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
                Estoque().atualizar_estoque()
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
        print('INFORMAÇÕES DO BANCO:\n')
        print(f'\nNome co Banco: {self.nome}\n'
                f'Nº do Banco: {self.nro_banco}\n'
                f'CNPJ: {self.cnpj}\n')

    def info_contas(self,banco):

        print('CONTAS DO BANCO:\n')
        if banco.contas_bancarias:

            for conta in banco.contas_bancarias:

                if isinstance(conta, ContaCorrente):
                    conta.info()

                if isinstance(conta,ContaPoupanca):
                    conta.info()

        else:
            return f'Banco não possui contas'

    @classmethod
    def buscar_banco(cls, nro_banco):

        for banco in cls.__todos_os_bancos:
            if nro_banco == banco.nro_banco:
                return banco

    @classmethod
    def fechar_conta(cls):
        nro = input("Digite o número da conta que deseja fechar: ").strip()
        conta = cls.buscar_conta(nro)
        if not conta:
            print("Conta não encontrada.")
            return

        if conta in cls.__todas_as_contas:
            cls.__todas_as_contas.remove(conta)

        if conta.titular and conta in conta.titular.contas_bancarias:
            conta.titular.contas_bancarias.remove(conta)

        if conta.banco and conta in conta.banco.contas_bancarias:
            conta.banco.contas_bancarias.remove(conta)

        print(f"Conta {nro} fechada com sucesso!")

        Estoque.atualizar_estoque()

    @classmethod
    def retornar_todos_os_bancos(cls):

        return cls.__todos_os_bancos

class ContaBancaria:

    __todas_as_contas = []

    def __init__(self, titular, banco, nro_conta: int, senha, saldo: float = 0.0):
        self._titular = titular  # Objeto Pessoa
        self._banco = banco  # Objeto Banco
        self._nro_conta = nro_conta
        self.senha = senha
        self._saldo = saldo

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

    @classmethod
    def todas_as_contas(cls):
        return cls.__todas_as_contas

    @senha.setter
    def senha(self, nova_senha):
        self._senha = nova_senha

    @classmethod
    def cadastrar_conta(cls):

        print(f'\nCADASTRO DE CONTA')

        while True:

            print(f'\nEx. de CPF: 000.000.000-00 \n'
                  f'Número de Banco: 4 dígitos numéricos\n'
                  f'Número da conta: 5 digitos numéricos\n'
                  f'A senha deve ser númerica e com 4 dígitos\n')

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

            pessoa = Pessoa.buscar_cpf(dados_conta[0])
            banco = Banco.buscar_banco(dados_conta[1])
            conta = ContaBancaria.buscar_conta(dados_conta[2])

            if pessoa:
                if banco:
                    if not conta:
                        while True:

                            print(f'\n1- Conta Corrente\n'
                                  f'2- Conta Poupança\n')
                            tipo = input('\nDigite o tipo de conta: ')

                            if tipo.lower() == "1":
                                conta_atual = ContaCorrente(pessoa, banco, dados_conta[2], dados_conta[3], 0.0,
                                                            0.0)
                                ContaBancaria.adicionar_conta(conta_atual)
                                banco.contas_bancarias = conta_atual
                                pessoa.contas_bancarias = conta_atual
                                print('Conta criada!')
                                Estoque().atualizar_estoque()
                                interface.menu()

                            elif tipo.lower() == "2":
                                conta_atual = ContaPoupanca(pessoa, banco, dados_conta[2], dados_conta[3], 0.0,
                                                            0.0, 3)
                                ContaBancaria.adicionar_conta(conta_atual)
                                banco.contas_bancarias = conta_atual
                                pessoa.contas_bancarias = conta_atual
                                print('Conta criada!')
                                Estoque().atualizar_estoque()
                                interface.menu()

                            else:
                                print('INVÁLIDO')

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

                if isinstance(conta, ContaCorrente):
                    conta.info()

                if isinstance(conta, ContaPoupanca):
                    conta.info()
            Interface().menu()

        else:
            print(f'\nNão há contas cadastradas neste sistema\n')

    @classmethod
    def adicionar_conta(cls, nova_conta):
        cls.__todas_as_contas.append(nova_conta)

    @classmethod
    def buscar_conta(cls, nro_conta):
        for conta in cls.__todas_as_contas:
            if nro_conta == conta.nro_conta:
                return conta

    @classmethod
    def verifica_senha(cls, conta, senha):

        for contas in cls.__todas_as_contas:
            if conta == contas.nro_conta:

                if senha == contas.senha:
                    return f'\nSenha correta'

        return f'\nSenha inválida'

    @classmethod
    def verifica_senha_input(cls):

        val = Validacoes()

        validar_conta = {'Nº Conta': val.validar_nro_conta,
                         'Senha': val.validar_senha}

        dados_validacao = []

        for chave, funcao in validar_conta.items():
            while True:

                dado = input(f'Digite o(a) {chave}: ')
                teste = funcao(dado)

                if teste:
                    dados_validacao.append(dado)
                    break

                else:
                    print(f'{chave} Inválido')

        validar = cls.verifica_senha(str(dados_validacao[0]), dados_validacao[1])

        return validar

    @classmethod
    def saque(cls, nr_conta, senha, valor):

        try:
            valor = float(valor)

            for conta in cls.__todas_as_contas:

                if nr_conta == conta.nro_conta:
                    if conta.verifica_senha(nr_conta, senha):
                        if valor > 0:
                            conta.saldo -= valor

                            return (f'Saque Realizado!\n'
                                    f'Saldo atual: {conta.saldo:.2f}\n\n')
                        else:
                            return f'Apenas valores maiores que 0.'

                    else:
                        return f'Senha incorreta'

            return f'Conta não existe'

        except ValueError:
            return 'Valor inválido'

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

                        Estoque.atualizar_estoque()
                        return (f'Depósito Realizado!\n'
                                f'Saldo atual: {conta.saldo}\n\n')

            return f'Depósito não realizado, conta ou senhas inexistentes ou inválidos'


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

                        Estoque.atualizar_estoque()
                        return (f'Depósito Realizado!\n'
                                f'Saldo atual: {conta.saldo}\n\n')

            return f'Depósito não realizado, conta ou senhas inexistentes'


        except ValueError:
            return 'valor inválido'

    @classmethod
    def retorna_conta(cls, conta=None):

        conta_formatada = []
        for conta in cls.__todas_as_contas:

            obj_b = conta.banco
            banco = f'Banco({obj_b.nome},{obj_b.cnpj},{str(obj_b.nro_banco)})'
            titular = conta.titular.cpf

            if isinstance(conta, ContaCorrente):
                conta_formatada.append(f'#CONTA ContaCorrente({titular},{banco},{str(conta.nro_conta)},'
                                       f'{conta.senha},{str(conta.saldo)},{str(conta.taxas_mensais)})\n')

            if isinstance(conta, ContaPoupanca):
                conta_formatada.append(
                    f'#CONTA ContaPoupanca({titular},{banco},{str(conta.nro_conta)},{conta.senha},{str(conta.saldo)},'
                    f'{str(conta.rendimentos)},{str(conta.saques_mensais)})\n')

        return conta_formatada

    @staticmethod
    def retorna_contas_bancarias(contas_pessoais):

        conta_formatada = []

        for conta in contas_pessoais:

            titular = conta.titular.cpf
            banco = conta.banco.nro_banco

            if isinstance(conta, ContaCorrente):
                conta_formatada.append(f'ContaCorrente({titular},'
                                       f'{str(banco)},{str(conta.nro_conta)},{conta.senha},{str(conta.saldo)},'
                                       f'{str(conta.taxas_mensais)})\n')

            if isinstance(conta, ContaPoupanca):
                conta_formatada.append(f'ContaPoupanca({titular},'
                                       f'{str(banco)},{str(conta.nro_conta)},{conta.senha},{str(conta.saldo)},'
                                       f'{str(conta.rendimentos)},{str(conta.saques_mensais)})\n')
        return conta_formatada

class ContaCorrente(ContaBancaria):

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

    def info(self):
        print(f'> CONTA CORRENTE <\n'
                f'\nTitular: {self.titular.nome}\n'
                f'Banco: {self.banco.nome}\n'
                f'Nº da conta: {self.nro_conta}\n'
                f'Saldo: {self.saldo:.2f}\n'
                f'Taxas Mensais: {self.taxas_mensais:.2f}\n')
        
    @classmethod
    def novo_mes(cls):
        nr_conta = input('informe o nº da conta: ')

        conta = ContaBancaria.buscar_conta(nr_conta)

        if conta and isinstance(conta, ContaCorrente):
            conta.saldo -= conta.taxas_mensais

            Estoque.atualizar_estoque()
            return (f'\nTaxa atualizada!\n'
                    f'Taxa atual: {conta.taxas_mensais:.2f}\n'
                    f'Saldo atual: {conta.saldo:.2f}\n')

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

    def info(self):
        print(f'> CONTA POUPANÇA <\n'
              f'Titular: {self.titular.nome}\n'
                f'Banco: {self.banco.nome}\n'
                f'Nº da conta: {self.nro_conta}\n'
                f'Saldo: R${self.saldo:.2f}\n'
                f'Rendimentos: R${self.rendimentos:.2f}\n'
                f'Saques Mensais: {self.saques_mensais}\n')

    @classmethod
    def novo_mes(cls):

        nr_conta = input('informe o nº da conta: ')
        conta = ContaBancaria.buscar_conta(nr_conta)

        if conta and isinstance(conta, ContaPoupanca):
                saldo_calculado = conta.saldo * (0.5 / 100)

                conta.saldo += saldo_calculado
                conta.saques_mensais = 3

                Estoque.atualizar_estoque()
                return (f'\nNovo mês atualizado!\n'
                        f'Saldo anterior: {conta.saldo - saldo_calculado:.2f}\n'
                        f'Saldo atual (com rendimento de 0.5%): {conta.saldo:.2f}\n'
                        f'Saques disponíveis: {conta.saques_mensais}')

        return f'Conta não encontrada'

    @classmethod
    def saque(cls, nr_conta, senha, valor):

        try:
            valor = float(valor)

            if ContaBancaria.verifica_senha(nr_conta, senha):

                conta = ContaBancaria.buscar_conta(nr_conta)

                if conta and isinstance(conta, ContaPoupanca):

                    if conta.saques_mensais > 0 and conta.saldo > 0:
                        conta.saldo -= valor
                        conta.saques_mensais -= 1

                        return (f'Saque Realizado!\n'
                                f'Saldo atual: {conta.saldo:.2f}\n'
                                f'Qnt saques disponíveis: {conta.saques_mensais}\n\n')
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

                conta = ContaBancaria.buscar_conta(nr_conta)

                if conta and isinstance(conta, ContaPoupanca):

                    if conta.saques_mensais > 0 and conta.saldo > 0:
                        conta.saldo -= valor
                        conta.saques_mensais -= 1

                        return (f'Saque Realizado!\n'
                                f'Saldo atual: {conta.saldo:.2f}\n'
                                f'Qnt saques disponíveis: {conta.saques_mensais}\n\n')
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
        return re.fullmatch(r"[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}", valor)

    @staticmethod
    def validar_senha(valor):
        return re.fullmatch(r'[0-9]{4}', valor)

    @staticmethod
    def validar_cnpj(valor):
        return re.fullmatch(r"[0-9]{2}\.[0-9]{3}\.[0-9]{3}/[0-9]{4}-[0-9]{2}", valor)

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

    @staticmethod
    def atualizar_estoque():

        with open("banco_de_dados.txt", 'w', encoding='utf8') as arquivo:

            lista_pessoas = Pessoa.retornar_todas_pessoas()

            contas_pessoais = set()

            for pessoa in lista_pessoas:  # acesso todas as pessoas.

                if pessoa.contas_bancarias:

                    contas_pessoais = ContaBancaria.retorna_contas_bancarias(pessoa.contas_bancarias)

                    arquivo.write(f'#PESSOA {pessoa.nome},{pessoa.sobrenome},'
                                  f'{pessoa.cpf},{str(pessoa.idade)}\n'
                                  f'{"".join(contas_pessoais)}\n')

                else:
                    arquivo.write(f'#PESSOA {pessoa.nome},{pessoa.sobrenome},{pessoa.cpf},{str(pessoa.idade)}\n\n')

            lista_bancos = Banco.retornar_todos_os_bancos()

            for bancos in lista_bancos:

                if bancos.contas_bancarias:

                    conta_formatada = []

                    for conta in bancos.contas_bancarias:

                        titular = conta.titular.cpf
                        banco = conta.banco.nro_banco

                        if isinstance(conta, ContaCorrente):
                            conta_formatada.append(f'ContaCorrente({titular},'
                                                   f'{str(banco)},{str(conta.nro_conta)},{conta.senha},{str(conta.saldo)},'
                                                   f'{str(conta.taxas_mensais)})\n')

                        if isinstance(conta, ContaPoupanca):
                            conta_formatada.append(f'ContaPoupanca({titular},'
                                                   f'{str(banco)},{str(conta.nro_conta)},{conta.senha},{str(conta.saldo)},'
                                                   f'{str(conta.rendimentos)},{str(conta.saques_mensais)})\n')

                    arquivo.write(f'#BANCO {bancos.nome},{bancos.cnpj},{bancos.nro_banco},{"".join(conta_formatada)}\n')

                else:
                    arquivo.write(f'#BANCO {bancos.nome},{bancos.cnpj},{bancos.nro_banco}\n')


            lista_contas = ContaBancaria.retorna_conta()

            if lista_contas:

                for conta in lista_contas:
                    arquivo.write(f'{conta}\n')

    @staticmethod
    def carregar_estoque():
        lista_bancos = Banco.retornar_todos_os_bancos()
        lista_pessoas = Pessoa.retornar_todas_pessoas()
        lista_contas = ContaBancaria.todas_as_contas()

        with open('banco_de_dados.txt', 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()

        i = 0
        while i < len(linhas):
            linha = linhas[i].strip()
            if linha.startswith("#BANCO"):
                partes = linha[6:].split(",", 3)
                nome = partes[0].strip()
                cnpj = partes[1].strip()
                nro_banco = partes[2].strip()

                banco = Banco(nome, cnpj, nro_banco)
                lista_bancos.append(banco)

                i += 1
                while i < len(linhas):
                    linha_conta = linhas[i].strip()
                    if linha_conta.startswith("#BANCO") or linha_conta.startswith("#PESSOA") or linha_conta == '':
                        break

                    if "ContaCorrente" in linha_conta:
                        dados = linha_conta.replace("ContaCorrente(", "").replace(")", "").split(",")
                        titular_cpf = dados[0].strip()
                        nro_conta = dados[2].strip()
                        senha = dados[3].strip()
                        saldo = float(dados[4])
                        taxas_mensais = float(dados[5])

                        titular = Pessoa.buscar_cpf(titular_cpf)

                        conta = ContaCorrente(titular, banco, nro_conta, senha, saldo, taxas_mensais)
                        lista_contas.append(conta)
                        banco.contas_bancarias.append(conta)

                    elif "ContaPoupanca" in linha_conta:
                        dados = linha_conta.replace("ContaPoupanca(", "").replace(")", "").split(",")
                        titular_cpf = dados[0].strip()
                        nro_conta = dados[2].strip()
                        senha = dados[3].strip()
                        saldo = float(dados[4])
                        rendimentos = float(dados[5])
                        saques_mensais = int(float(dados[6]))

                        titular = Pessoa.buscar_cpf(titular_cpf)
                        if titular is None:
                            titular = Pessoa("Desconhecido", "", 0, titular_cpf)
                            lista_pessoas.append(titular)

                        conta = ContaPoupanca(titular, banco, nro_conta, senha, saldo, rendimentos, saques_mensais)
                        lista_contas.append(conta)
                        banco.contas_bancarias.append(conta)

                    i += 1

            else:
                i += 1

        i = 0
        while i < len(linhas):
            linha = linhas[i].strip()
            if linha.startswith("#PESSOA"):
                partes = linha[7:].split(",")
                nome = partes[0].strip()
                sobrenome = partes[1].strip()
                cpf = partes[2].strip()
                idade = int(partes[3].strip())

                pessoa = Pessoa(nome, sobrenome, idade, cpf)
                lista_pessoas.append(pessoa)

                i += 1
                while i < len(linhas):
                    linha_conta = linhas[i].strip()
                    if linha_conta.startswith("#BANCO") or linha_conta.startswith("#PESSOA") or linha_conta == '':
                        break

                    if "ContaCorrente" in linha_conta:
                        dados = linha_conta.replace("ContaCorrente(", "").replace(")", "").split(",")
                        banco_nro = dados[1].strip()
                        nro_conta = dados[2].strip()
                        senha = dados[3].strip()
                        saldo = float(dados[4])
                        taxas_mensais = float(dados[5])

                        banco_obj = next((b for b in lista_bancos if b.nro_banco == banco_nro), None)
                        if banco_obj is None:
                            banco_obj = Banco("Desconhecido", "000.000.000/0000-00", banco_nro)
                            lista_bancos.append(banco_obj)

                        conta_obj = next(
                            (c for c in banco_obj.contas_bancarias if c.nro_conta == nro_conta and c.senha == senha),
                            None)

                        if conta_obj:
                            conta_obj.titular = pessoa
                        else:
                            conta_obj = ContaCorrente(pessoa, banco_obj, nro_conta, senha, saldo, taxas_mensais)
                            banco_obj.contas_bancarias.append(conta_obj)
                            lista_contas.append(conta_obj)

                        pessoa.contas_bancarias.append(conta_obj)

                    elif "ContaPoupanca" in linha_conta:
                        dados = linha_conta.replace("ContaPoupanca(", "").replace(")", "").split(",")
                        banco_nro = dados[1].strip()
                        nro_conta = dados[2].strip()
                        senha = dados[3].strip()
                        saldo = float(dados[4])
                        rendimentos = float(dados[5])
                        saques_mensais = int(float(dados[6]))

                        banco_obj = next((b for b in lista_bancos if b.nro_banco == banco_nro), None)
                        if banco_obj is None:
                            banco_obj = Banco("Desconhecido", "000.000.000/0000-00", banco_nro)
                            lista_bancos.append(banco_obj)

                        conta_obj = next(
                            (c for c in banco_obj.contas_bancarias if c.nro_conta == nro_conta and c.senha == senha),
                            None)

                        if conta_obj:
                            conta_obj.titular = pessoa
                        else:
                            conta_obj = ContaPoupanca(pessoa, banco_obj, nro_conta, senha, saldo, rendimentos,
                                                      saques_mensais)
                            banco_obj.contas_bancarias.append(conta_obj)
                            lista_contas.append(conta_obj)

                        pessoa.contas_bancarias.append(conta_obj)

                    i += 1

            else:
                i += 1

class Interface:

    def __init__(self):
        pass

    def menu(self):

        print(f"\n 1 - Cadastrar Banco\n"
              f" 2 - Buscar Banco\n"
              f" 3 - Cadastrar Cliente\n"
              f" 4 - Buscar Cliente\n"
              f" 5 - Cadastrar Conta\n"
              f" 6 - Buscar Conta\n\n"
              f" 7 - Listar Bancos Cadastrados\n"
              f" 8 - Listar Pessoas Cadastradas\n"
              f" 9 - Listar Contas Cadastradas\n\n"
              f" 10 - Sacar\n"
              f" 11 - Depositar\n"
              f" 12 - Simular novo mês\n\n"
              f" 13 - Encerrar Sistema e Atualizar estoque\n")

        while True:

            try:
                pergunta_menu_1 = int(input('Digite a Opção desejada: \n'))

                match pergunta_menu_1:

                    case 1:
                        Banco.criar_banco()

                    case 2:
                        self.buscar_banco()

                    case 3:
                        Pessoa.criar_pessoa()

                    case 4:
                        self.buscar_cliente()

                    case 5:
                        ContaBancaria.cadastrar_conta()

                    case 6:
                        self.buscar_conta()

                    case 7:
                        Banco.listar_bancos()

                    case 8:
                        Pessoa.listar_pessoas()

                    case 9:
                        ContaBancaria.listar_contas()

                    case 10:
                        self.saque()

                    case 11:
                        ContaBancaria.deposito_input()

                    case 12:
                        self.novo_mes()

                    case 13:
                        self.encerrar_sistema()



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

        interface = Interface()

        print(f'\nBusca de cliente\n'
              f'Exemplo de CPF: 000.000.000-00\n\n')

        per = input('Digite o cpf do cliente: ')

        pessoa = Pessoa.buscar_cpf(per)

        if pessoa:
            print(pessoa.info())
            print(pessoa.info_contas(per))
            interface.menu()

        else:
            print(f'\nPessoa não encontrada\n')

    @staticmethod
    def buscar_banco():

        interface = Interface()

        per = input('\nDigite o Nº do banco: ')
        banco = Banco.buscar_banco(per)

        if banco:
            banco.info_banco()
            if banco.contas_bancarias:
                print(banco.info_contas(banco))
            interface.menu()

        else:
            print(f'banco não encontrado')

    @staticmethod
    def buscar_conta():
        interface = Interface()

        per = input('\nDigite o Nº da conta: ')
        conta = ContaBancaria.buscar_conta(per)

        if conta and isinstance(conta, ContaCorrente):
            conta.info()
            interface.menu()

        if conta and isinstance(conta, ContaPoupanca):
            conta.info()
            interface.menu()

        else:
            print(f'\nconta não existe\n')
            interface.menu()

    @staticmethod
    def encerrar_sistema():
        Estoque.atualizar_estoque()
        print(f'\nOBRIGADO\n')


if __name__ == '__main__':
    Estoque.carregar_estoque()

    #MÉTODO VALIDAR SENHA CLASSE CONTA BANCÁRIA:

    # conta = ContaBancaria

    # print(conta.verifica_senha("54321","4321"))
    # print()
    # print(conta.verifica_senha_input())
    # print()

    #MÉTODO DEPÓSITO E SAQUE DA CLASSE CONTA BANCÁRIA:

    # print(conta.deposito("54321","4321",50.00))
    # print()
    # print(conta.saque("54321","4321",10.00))
    # print()
    # print(conta.deposito_input())
    # print()
    # print(conta.saque_input())

    #MÉTODO NOVO_MES CONTA CORRENTE (nro_conta = 54321)

    # print(ContaCorrente.novo_mes())
    # print()

    #MÉTODO NOVO_MES CONTA POUPANÇA (EXEMPLO Nro_conta: 54322 senha: 4322)

    # print(ContaPoupanca.novo_mes())
    # print()

    # MÉTODO SAQUE POUPANÇA
    # print(ContaPoupanca.saque("54322", "4322", 15.11))
    # print()

    # print(ContaPoupanca.saque_input())
    # print()
    Interface().menu()
