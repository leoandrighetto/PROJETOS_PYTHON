from nt import write

import sys

class Livro:

    def __init__(self, codigo, titulo, editora, categoria, ano, valor, quantidade_em_estoque):
        self.codigo = codigo
        self.titulo = titulo
        self.editora = editora
        self.categoria = categoria
        self.ano = ano
        self.valor = valor
        self.quantidade_em_estoque = quantidade_em_estoque


    def info(self):
        total_estoque = self.valor * self.quantidade_em_estoque

        print()
        return (f">>>CÓDIGO: {self.codigo}\n"
                f"Título/Editora: {self.titulo}/{self.editora}\n"
                f"Categoria: {self.categoria}\n"
                f"Ano: {self.ano}\n"
                f"Valor: R$ {self.valor}\n"
                f"Estoque: {self.quantidade_em_estoque} unidades\n"
                f"Valor Total em Estoque: R${total_estoque:.2f}")


class Filial:

    def __init__(self, codigo_filial, nome_filial, endereco, contato):
        self.codigo_filial = codigo_filial
        self.nome_filial = nome_filial
        self.endereco = endereco
        self.contato = contato

class SistemaDeLivraria:

    def __init__(self):

        self.livros = []
        self.filiais = []
        self.estoque_filiais = {}

    def ExibirMenuInterativo(self):
        print(18 * "-=")
        print(18 * "-=")
        print("        --MENU PRINCIPAL--")
        print()
        print("> 1  -  Cadastrar novo livro")
        print("> 2  -  Listar livros em cadastro")
        print("> 3  -  Buscar livros por nome")
        print("> 4  -  Buscar livros por categoria")
        print("> 5  -  Buscar livros por preço")
        print("> 6  -  Busca por quantidade em estoque")
        print("> 7  -  Valor total no estoque")
        print("> 8  -  Carregar estoque")
        print("> 9  -  Atualizar arquivo de estoque")
        print("> 10 -  Criar filial")
        print("> 11 -  Listagem de Estoque")
        print("> 12 -  Busca por Código")
        print("> 0  -  Encerrar atividades")
        print()
        print(18 * "-=")

        while True:

            try:
                print()
                pergunta_menu_interativo = int(input("Digite a opção desejada >>> "))

                match pergunta_menu_interativo:

                    case 1:
                        self.CadastrarNovoLivro()

                    case 2:
                        self.MostrarInfo()

                    case 3:
                        self.BuscarPorNome()

                    case 4:
                        self.BuscarPorCategoria()

                    case 5:
                        self.BuscarPorPreco()

                    case 6:
                        self.BuscarPorQuantidadeEmEstoque()

                    case 7:
                        self.ValorTotalEstoque()

                    case 8:
                        self.CarregarEstoque()

                    case 9:
                        self.AtualizarArquivo()

                    case 10:
                        self.CriarFilial()

                    case 11:
                        self.ListagemDeEstoque()

                    case 12:
                        self.BuscaPorCodigo()

                    case 0:
                        self.EncerrarSistema()

                    case _:
                        print()
                        print('OPÇÃO INVÁLIDA')

            except ValueError:
                print()
                print("OPÇÃO INVÁLIDA")

    def MostrarInfo(self):  # OPÇÃO 2 - MENU INTERATIVO

        filial_atual = None

        for registro in self.filiais:  # ACESSANDO A LISTA DE FILIAIS
            print()
            print(f'Filial: {registro.nome_filial} | Código: {registro.codigo_filial}')
            print()
            filial_atual = registro.nome_filial

            for filial, lista in self.estoque_filiais.items():
                if filial_atual == filial:

                    for livro in lista:
                        print(f">>>CÓDIGO: {livro.codigo}\n"
                        f"Título/Editora: {livro.titulo}/{livro.editora}\n"
                        f"Categoria: {livro.categoria}\n"
                        f"Ano: {livro.ano}\n"
                        f"Valor: R$ {livro.valor}\n"
                        f"Estoque: {livro.quantidade_em_estoque} unidades\n"
                        f"Valor total em estoque: R${livro.quantidade_em_estoque * livro.valor:.2f}\n")

        while True:
            print()
            print("RESPONDA COM S / N:")
            pergunta_MostrarInfo = input('DESEJA CADASTRAR MAIS LIVROS? ')

            if pergunta_MostrarInfo.lower() == "s":
                self.CadastrarNovoLivro()
                break

            elif pergunta_MostrarInfo.lower() == "n":
                self.ExibirMenuInterativo()
                break

            else:
                print()
                print('ENTRADA INVÁLIDA, digite apenas S para Sim e N para n!')

    def CadastrarNovoLivro(self):  # OPÇÃO 1 DO MENU INTERATIVO
        print()
        print(18 * "-=")
        print("     >> CADASTRO DE LIVROS <<")

        while True:

            print()
            codigo_livro = input(">> Código do livro: ")
            titulo_livro = input(">> Título do livro: ")
            editora_livro = input(">> Editora do livro: ")
            categoria_livro = input(">> Categoria do livro: ")
            ano_livro = input(">> Ano do livro: ")
            valor_livro = float(input('>> Valor do livro: '))
            quantidade_estoque_livro = int(input('>> Digite a quantidade em estoque do livro: '))
            nome_filial_livro = input(">> Digite o nome da filial: ")

            self.livros.append(Livro(codigo_livro, titulo_livro, editora_livro, categoria_livro, ano_livro,
                                     valor_livro, quantidade_estoque_livro))

            filial_encontrada = False

            for nome, livros in self.estoque_filiais.items():
                if nome_filial_livro.lower() == nome.lower():
                    filial_encontrada = True
                    livros.append(Livro(codigo_livro, titulo_livro, editora_livro, categoria_livro, ano_livro,
                                     valor_livro, quantidade_estoque_livro))
                    break

            if filial_encontrada == False:
                while True:
                    print()
                    print("Filial não encontrada.")

                    pergunta_1_cadastro_novo_livro = input('Tentar mais uma vez (s/n)? ')
                    if pergunta_1_cadastro_novo_livro.lower() == 's':
                        break

                    elif pergunta_1_cadastro_novo_livro.lower() == 'n':
                        self.ExibirMenuInterativo()

                    else:
                        print('ENTRADA INVÁLIDA')



            else:
                print()
                print(18 * "-=")
                print()
                print('    LIVRO CADASTRADO COM SUCESSO!')
                print()
                print('> OPÇÕES:')
                print("> 1. CADASTRAR NOVO LIVRO")
                print("> 2. VOLTAR AO MENU PRINCIPAL")
                print()

                while True:

                    pergunta_cadastro_novo_livro = input("Digite a opção desejada >>  ")

                    if pergunta_cadastro_novo_livro == "1":
                        break

                    elif pergunta_cadastro_novo_livro == "2":
                        self.ExibirMenuInterativo()
                        break

                    else:
                        print()
                        print('ENTRADA INVÁLIDA!')
                        print()

    def BuscarPorNome(self):  # OPÇÃO 3 DO MENU INTERATIVO
        print()
        print(18 * "-=")
        print("     --BUSCAR LIVRO POR NOME--")

        while True:
            print()
            pergunta_1_busca_por_nome = input("Digite o código da filial (ou 0 para sair): ")

            if pergunta_1_busca_por_nome != "0" :

                pergunta_2_busca_por_nome = input("Digite o título do livro: ")

                controle_nome_filial= None

                for filial in self.filiais:                                                 #ACESSANDO A LISTA DE FILIAIS
                    if pergunta_1_busca_por_nome.lower() == filial.codigo_filial.lower():
                        controle_nome_filial = filial.nome_filial
                        break

                filial_encontrada = False
                livro_encontrado = False

                for filial, lista_livros in self.estoque_filiais.items():                    #ACESSANDO O ESTOQUE DA FILIAL

                    if controle_nome_filial.lower() == filial.lower():
                        filial_encontrada = True

                        for livro in lista_livros:
                            if livro.titulo.lower() == pergunta_2_busca_por_nome.lower():
                                livro_encontrado = True

                                print(f">>>CÓDIGO: {livro.codigo}\n"
                                      f"Título/Editora: {livro.titulo}/{livro.editora}\n"
                                      f"Categoria: {livro.categoria}\n"
                                      f"Ano: {livro.ano}\n"
                                      f"Valor: R$ {livro.valor}\n"
                                      f"Estoque: {livro.quantidade_em_estoque} unidades"
                                      f"Valor total em estoque: R${livro.quantidade_em_estoque * livro.valor:.2f}\n")

                if not livro_encontrado:
                    print()
                    print("LIVRO NÃO ENCONTRADO!")
                    while True:
                        print()
                        print("> 1. Buscar novo livro")
                        print("> 2. Voltar ao menu principal")
                        print()

                        pergunta_2_busca_por_nome = input("Digite a opção desejada >>> ")

                        if pergunta_2_busca_por_nome == "1":
                            break

                        elif pergunta_2_busca_por_nome == "2":
                            self.ExibirMenuInterativo()
                            break

                        else:
                            print()
                            print('ENTRADA INVÁLIDA!')
                            print()

                else:
                    print(18 * "-=")
                    while True:
                        print()
                        pergunta_3_busca_por_nome = input("Gostaria de consultar outro livro (S/N)? ")

                        if pergunta_3_busca_por_nome.lower() == "s":
                            break

                        elif pergunta_3_busca_por_nome.lower() == "n":
                            self.ExibirMenuInterativo()
                            break

                        else:
                            print()
                            print("ENTRADA INVÁLIDA")

            else:
                self.ExibirMenuInterativo()

    def BuscarPorCategoria(self):  # OPÇÃO 4 DO MENU INTERATIVO
        print()
        print(18 * "-=")
        print("   --BUSCAR LIVRO POR CATEGORIA--")

        while True:
            print()
            pergunta_1_busca_por_categoria = input("Digite o código da filial (ou 0 para sair): ")

            if pergunta_1_busca_por_categoria != "0":

                pergunta_2_busca_por_categoria = input("Digite a categoria do livro: ")

                controle_nome_filial = None

                for filial in self.filiais:  # ACESSANDO A LISTA DE FILIAIS
                    if pergunta_1_busca_por_categoria.lower() == filial.codigo_filial.lower():
                        controle_nome_filial = filial.nome_filial
                        break

                filial_encontrada = False
                livro_encontrado = False

                for filial, lista_livros in self.estoque_filiais.items():  # ACESSANDO O ESTOQUE DA FILIAL

                    if controle_nome_filial.lower() == filial.lower():
                        filial_encontrada = True

                        for livro in lista_livros:
                            if livro.categoria.lower() == pergunta_2_busca_por_categoria.lower():
                                livro_encontrado = True

                                print(f">>>CÓDIGO: {livro.codigo}\n"
                                      f"Título/Editora: {livro.titulo}/{livro.editora}\n"
                                      f"Categoria: {livro.categoria}\n"
                                      f"Ano: {livro.ano}\n"
                                      f"Valor: R$ {livro.valor}\n"
                                      f"Estoque: {livro.quantidade_em_estoque} unidades\n"
                                      f"Valor total em estoque: R${livro.quantidade_em_estoque * livro.valor:.2f}\n")

                if not livro_encontrado:
                    print()
                    print("CATEGORIA NÃO ENCONTRADO!")
                    while True:
                        print()
                        print("> 1. Buscar nova categoria")
                        print("> 2. Voltar ao menu principal")
                        print()

                        pergunta_2_busca_por_categoria = input("Digite a opção desejada >>> ")

                        if pergunta_2_busca_por_categoria == "1":
                            break

                        elif pergunta_2_busca_por_categoria == "2":
                            self.ExibirMenuInterativo()
                            break

                        else:
                            print()
                            print('ENTRADA INVÁLIDA!')
                            print()

                else:
                    print(18 * "-=")
                    while True:
                        print()
                        pergunta_3_busca_por_categoria = input("Gostaria de consultar outra categoria (S/N)? ")

                        if pergunta_3_busca_por_categoria.lower() == "s":
                            break

                        elif pergunta_3_busca_por_categoria.lower() == "n":
                            self.ExibirMenuInterativo()
                            break

                        else:
                            print()
                            print("ENTRADA INVÁLIDA")

            else:
                self.ExibirMenuInterativo()

    def BuscarPorPreco(self):  # OPÇÃO 5 DO MENU INTERATIVO
        print()
        print(18 * "-=")
        print("   --BUSCAR LIVROS POR PREÇO--")
        print()

        while True:
            print()

            pergunta_1_busca_por_preco = input( 'Digite o código da filial (ou 0 para sair): ')
            if pergunta_1_busca_por_preco != "0":

                try:
                    pergunta_2_busca_por_preco = float(
                        input("Digite seu valor máximo (Exemplo: 10.99 | ou digite 0 para sair): "))

                    controle_nome_filial = None

                    for filial in self.filiais:  # ACESSANDO A LISTA DE FILIAIS
                        if pergunta_1_busca_por_preco.lower() == filial.codigo_filial.lower():
                            controle_nome_filial = filial.nome_filial
                            break

                    filial_encontrada = False
                    livro_encontrado = False

                    for filial, lista_livros in self.estoque_filiais.items():  # ACESSANDO O ESTOQUE DA FILIAL

                        if controle_nome_filial.lower() == filial.lower():
                            filial_encontrada = True

                            for livro in lista_livros:
                                if pergunta_2_busca_por_preco <= livro.valor:
                                    livro_encontrado = True
                                    print()
                                    print(f">>>CÓDIGO: {livro.codigo}\n"
                                          f"Título/Editora: {livro.titulo}/{livro.editora}\n"
                                          f"Categoria: {livro.categoria}\n"
                                          f"Ano: {livro.ano}\n"
                                          f"Valor: R$ {livro.valor}\n"
                                          f"Estoque: {livro.quantidade_em_estoque} unidades\n"
                                          f"Valor total em estoque: R${livro.quantidade_em_estoque * livro.valor:.2f}")

                    if not livro_encontrado:
                        print()
                        print("PREÇO ESTIMADO NÃO ENCONTRADO!")
                        while True:
                            print()
                            print("> 1. Buscar novamente")
                            print("> 2. Voltar ao menu principal")
                            print()

                            pergunta_2_busca_por_categoria = input("Digite a opção desejada >>> ")

                            if pergunta_2_busca_por_categoria == "1":
                                break

                            elif pergunta_2_busca_por_categoria == "2":
                                self.ExibirMenuInterativo()
                                break

                            else:
                                print()
                                print('ENTRADA INVÁLIDA!')
                                print()

                    else:
                        print(18 * "-=")
                        while True:
                            print()
                            pergunta_3_busca_por_categoria = input("Gostaria de consultar outro valor (S/N)? ")

                            if pergunta_3_busca_por_categoria.lower() == "s":
                                break

                            elif pergunta_3_busca_por_categoria.lower() == "n":
                                self.ExibirMenuInterativo()
                                break

                            else:
                                print()
                                print("ENTRADA INVÁLIDA")



                except ValueError:
                    print()
                    print("ENTRADA INVÁLIDA")
                    print('Exemplo de Formato Correto para preços > 10.99')

            else:
                self.ExibirMenuInterativo()

    def BuscarPorQuantidadeEmEstoque(self):  # OPÇÃO 6 DO MENU INTERATIVO
        print()
        print(10 * "-=")
        print("--BUSCAR LIVRO POR QUANTIDADE EM ESTOQUE--")
        print()

        while True:
            print()

            pergunta_1_busca_por_quantidade = input('Digite o código da filial (ou 0 para sair): ')
            if pergunta_1_busca_por_quantidade != "0":

                try:
                    pergunta_2_busca_por_quantidade = float(
                        input("Digite a quantidade desejada: "))

                    controle_nome_filial = None

                    for filial in self.filiais:  # ACESSANDO A LISTA DE FILIAIS
                        if pergunta_1_busca_por_quantidade.lower() == filial.codigo_filial.lower():
                            controle_nome_filial = filial.nome_filial
                            break

                    filial_encontrada = False
                    livro_encontrado = False

                    for filial, lista_livros in self.estoque_filiais.items():  # ACESSANDO O ESTOQUE DA FILIAL

                        if controle_nome_filial.lower() == filial.lower():
                            filial_encontrada = True

                            for livro in lista_livros:
                                if livro.quantidade_em_estoque <= pergunta_2_busca_por_quantidade :
                                    livro_encontrado = True
                                    print()
                                    print(f">>>CÓDIGO: {livro.codigo}\n"
                                          f"Título/Editora: {livro.titulo}/{livro.editora}\n"
                                          f"Categoria: {livro.categoria}\n"
                                          f"Ano: {livro.ano}\n"
                                          f"Valor: R$ {livro.valor}\n"
                                          f"Estoque: {livro.quantidade_em_estoque} unidades\n"
                                          f"Valor total em estoque: R${livro.quantidade_em_estoque * livro.valor:.2f}")

                    if not livro_encontrado:
                        print()
                        print("QUANTIDADE ESTIMADA NÃO ENCONTRADA!")
                        while True:
                            print()
                            print("> 1. Buscar novamente")
                            print("> 2. Voltar ao menu principal")
                            print()

                            pergunta_2_busca_por_quantidade = input("Digite a opção desejada >>> ")

                            if pergunta_2_busca_por_quantidade == "1":
                                break

                            elif pergunta_2_busca_por_quantidade == "2":
                                self.ExibirMenuInterativo()
                                break

                            else:
                                print()
                                print('ENTRADA INVÁLIDA!')
                                print()

                    else:
                        print(18 * "-=")
                        while True:
                            print()
                            pergunta_3_busca_por_quantidade = input("Gostaria de consultar outro valor (S/N)? ")

                            if pergunta_3_busca_por_quantidade.lower() == "s":
                                break

                            elif pergunta_3_busca_por_quantidade.lower() == "n":
                                self.ExibirMenuInterativo()
                                break

                            else:
                                print()
                                print("ENTRADA INVÁLIDA")



                except ValueError:
                    print()
                    print("ENTRADA INVÁLIDA")
                    print('Exemplo de Formato Correto para preços > 10.99')

            else:
                self.ExibirMenuInterativo()

    def ValorTotalEstoque(self):  # OPÇÃO 7 DO MENU INTERATIVO
        print()
        print(10 * "-=")
        print("--VALOR TOTAL EM ESTOQUE--")
        print()

        while True:

            pergunta_1_busca_por_valor_de_estoque = input('Digite o código da filial (ou 0 para sair): ')
            if pergunta_1_busca_por_valor_de_estoque != "0":

                try:
                    pergunta_2_busca_por_valor_de_estoque = float(
                        input("Digite o valor mínimo desejado: "))

                    controle_nome_filial = None



                    for filial in self.filiais:  # ACESSANDO A LISTA DE FILIAIS
                        if pergunta_1_busca_por_valor_de_estoque.lower() == filial.codigo_filial.lower():
                            controle_nome_filial = filial.nome_filial
                            break

                    filial_encontrada = False
                    livro_encontrado = False

                    for filial, lista_livros in self.estoque_filiais.items():  # ACESSANDO O ESTOQUE DA FILIAL

                        if controle_nome_filial.lower() == filial.lower():
                            filial_encontrada = True
                            for livro in lista_livros:
                                valor_total_estoque = livro.quantidade_em_estoque * livro.valor
                                if valor_total_estoque >= pergunta_2_busca_por_valor_de_estoque:
                                    livro_encontrado = True
                                    print()
                                    print(f">>>CÓDIGO: {livro.codigo}\n"
                                          f"Título/Editora: {livro.titulo}/{livro.editora}\n"
                                          f"Categoria: {livro.categoria}\n"
                                          f"Ano: {livro.ano}\n"
                                          f"Valor: R$ {livro.valor}\n"
                                          f"Estoque: {livro.quantidade_em_estoque} unidades\n"
                                          f"Valor total em estoque: R${valor_total_estoque:.2f}")

                    if not livro_encontrado:
                        print()
                        print("QUANTIDADE ESTIMADA NÃO ENCONTRADA!")
                        while True:
                            print()
                            print("> 1. Buscar novamente")
                            print("> 2. Voltar ao menu principal")
                            print()

                            pergunta_2_busca_por_quantidade = input("Digite a opção desejada >>> ")

                            if pergunta_2_busca_por_quantidade == "1":
                                break

                            elif pergunta_2_busca_por_quantidade == "2":
                                self.ExibirMenuInterativo()
                                break

                            else:
                                print()
                                print('ENTRADA INVÁLIDA!')
                                print()

                    else:
                        print(18 * "-=")
                        while True:
                            print()
                            pergunta_3_busca_por_quantidade = input("Gostaria de consultar outro valor (S/N)? ")

                            if pergunta_3_busca_por_quantidade.lower() == "s":
                                break

                            elif pergunta_3_busca_por_quantidade.lower() == "n":
                                self.ExibirMenuInterativo()
                                break

                            else:
                                print()
                                print("ENTRADA INVÁLIDA")



                except ValueError:
                    print()
                    print("ENTRADA INVÁLIDA")
                    print('Exemplo de Formato Correto para preços > 10.99')

            else:
                self.ExibirMenuInterativo()

    def CarregarEstoque(self):  # OPÇÃO 8

        self.filiais = []
        self.livros = []
        self.estoque_filiais = {}

        arquivo = open("BancoDeLivros.txt", "r", encoding="utf8")

        linha = arquivo.readline().replace("\n", "")

        filial_atual = None

        while linha:

            linha = linha.strip()
            if not linha:
                linha = arquivo.readline()
                continue

            linha_editada = [campo.strip() for campo in linha.split(",")]

            if linha_editada[0].strip().startswith("#"):

                nome_filial_atual = linha_editada[1]

                self.filiais.append (Filial(linha_editada[0],
                                            linha_editada[1],
                                            linha_editada[2],
                                            linha_editada[3]))

                self.estoque_filiais[nome_filial_atual] = []

            else:
                linha_editada[5] = linha_editada[5].replace("R$", "")
                linha_editada[5] = float(linha_editada[5])
                linha_editada[6] = int(linha_editada[6])

                novo_livro = Livro(linha_editada[0],
                                         linha_editada[1],
                                         linha_editada[2],
                                         linha_editada[3],
                                         linha_editada[4],
                                         linha_editada[5],
                                         linha_editada[6])

                self.livros.append(novo_livro)

                if nome_filial_atual:
                    self.estoque_filiais[nome_filial_atual].append(novo_livro)

            linha = arquivo.readline()

        for nome_filial, lista_de_livros in self.estoque_filiais.items():
            print(f'\n📚 {nome_filial}:')
            for livro in lista_de_livros:
                print(
                    f'  - {livro.titulo} ({livro.ano}) - {livro.editora} - R${livro.valor:.2f} - {livro.quantidade_em_estoque} unidade(s)')

        print()
        print("ESTOQUE CARREGADO!")
        print()

        self.ExibirMenuInterativo()

    def AtualizarArquivo(self):  # OPÇÃO 9

        while True:
            print()
            pergunta_atualizar_arquivo_1 = input('DESEJA ATUALIZAR O ESTOQUE? (S/N): ')

            if pergunta_atualizar_arquivo_1.lower() == "s":

                with  open("BancoDeLivros.txt", "w", encoding="UTF8") as arquivo:

                    for filial in self.filiais:
                        nome = filial.nome_filial
                        if nome in self.estoque_filiais:
                            linha_filial = (
                                f"{filial.codigo_filial},{filial.nome_filial},"
                                f"{filial.endereco},{filial.contato}\n")
                            arquivo.write(linha_filial)

                        for livro in self.estoque_filiais[nome]:

                            linha_livro = (f"{livro.codigo},{livro.titulo},{livro.editora},{livro.categoria}"
                                           f",{livro.ano},R${livro.valor},{livro.quantidade_em_estoque}\n")
                            arquivo.write(linha_livro)

                        arquivo.write("\n")

                print()
                print('Estoque Atualizado!')
                self.livros.clear()
                self.filiais.clear()
                self.CarregarEstoque()
                print()
                self.ExibirMenuInterativo()
                break


            elif pergunta_atualizar_arquivo_1.lower() == "n":
                self.ExibirMenuInterativo()

            else:
                print('ENTRADA INVÁLIDA!')

    def CriarFilial(self):
        print()
        pergunta_1_criar_filial = input('Deseja Criar uma Filial? (S/N): ')

        if pergunta_1_criar_filial.lower() == "s":

            print()
            while True:
                codigo_filial = input("Código da Filial (Ex: #FL01): ")
                nome_filial = input("Nome da Filial: ")
                endereco = input("Endereço da Filial: ")
                contato = input("Contato da Filial: ")

                self.filiais.append(Filial(codigo_filial,nome_filial,endereco,contato))

                self.estoque_filiais[nome_filial] = []

                print()
                print('Filial Criada Com Sucesso!')
                print()

                pergunta_2_criar_filial = input('Deseja criar mais uma filial (S/N)? ')

                if pergunta_2_criar_filial.lower() == "n":
                    self.ExibirMenuInterativo()

        else:
            self.ExibirMenuInterativo()

    def ListagemDeEstoque(self):

        while True:

            print()
            pergunta_1_listagem_estoque = input('Digite o nome da Filial: ')
            print()

            valor_total_estoque_filial = 0

            filial_encontrada = False

            for filial, lista_livros in self.estoque_filiais.items():

                if pergunta_1_listagem_estoque.lower() == filial.lower():

                    filial_encontrada = True
                    print(f'Filial {filial} |')
                    for livro in lista_livros:
                        print(f">>>CÓDIGO: {livro.codigo}\n"
                    f"Título/Editora: {livro.titulo}/{livro.editora}\n"
                    f"Categoria: {livro.categoria}\n"
                    f"Ano: {livro.ano}\n"
                    f"Valor: R$ {livro.valor}\n"
                    f"Estoque: {livro.quantidade_em_estoque} unidades")

                        valor_total_estoque_filial += (livro.quantidade_em_estoque + livro.valor)
                    print()
                    print(f'Valor total em estoque da filial: R${valor_total_estoque_filial:.2f}\n')


            if not filial_encontrada:
                while True:
                    print()
                    print('Filial Não encontrada!')
                    print()
                    pergunta_2_listagem_estoque = input('Deseja tentar mais uma busca (s/n)? ')

                    if pergunta_2_listagem_estoque.lower() == "n":
                        self.ExibirMenuInterativo()

                    elif pergunta_2_listagem_estoque.lower() == "s":
                        break

                    else:
                        print('ENTRADA INVÁLIDA')


            else:
                while True:

                    print()
                    pergunta_3_listagem_estoque = input('Gostaria de pesquisar outra filial (S/N)? ')
                    print()

                    if pergunta_3_listagem_estoque.lower() == 'n':
                        self.ExibirMenuInterativo()
                        break
                    elif pergunta_3_listagem_estoque.lower() == 's':
                        break
                    else:
                        print()
                        print("Entrada Inválida!")

    def BuscaPorCodigo(self):

        while True:
            print()
            pergunta_1_busca_por_codigo = input('Digite o Código do Livro: ')
            print()

            unidades_estoque = 0

            valor_em_estoque = 0

            livro_encontrado = False

            for livro in self.livros:
                if pergunta_1_busca_por_codigo.lower() == livro.codigo.lower():
                    livro_encontrado = True
                    print(f'>>>>>Código: {livro.codigo}\n'
                          f'Titulo/Editora: {livro.titulo} / {livro.editora}\n'
                          f'Categoria: {livro.categoria}\n'
                          f'Ano: {livro.ano}')
                    break
            if livro_encontrado == True:

                for filial, lista_livros in self.estoque_filiais.items():
                    for livro in lista_livros:
                        if livro.codigo.lower() == pergunta_1_busca_por_codigo.lower():
                            print(f'Valor: R${livro.valor:.2f}>>>Filial {filial}, Estoque: {livro.quantidade_em_estoque} unidades')
                            unidades_estoque += livro.quantidade_em_estoque
                            valor_em_estoque += livro.valor

                print()
                print(f"Valor Total em Estoque: R${unidades_estoque * valor_em_estoque:.2f}")
                print()

                while True:

                    pergunta_2_busca_por_codigo = input("Deseja realizar uma nova busca? (S/N): ")
                    if pergunta_2_busca_por_codigo.lower() == 'n':
                        self.ExibirMenuInterativo()
                        break
                    elif pergunta_2_busca_por_codigo.lower() == 's':
                        break
                    else:
                        print()
                        print("Entrada Inválida!")
            else:
                while True:
                    print()
                    print('Livro não encontrado!')
                    pergunta_3_busca_por_codigo = input('Deseja realizar uma nova busca? (S/N): ')

                    if pergunta_3_busca_por_codigo.lower() == 'n':
                        self.ExibirMenuInterativo()

                    if pergunta_3_busca_por_codigo.lower() == 's':
                        break
                    else:
                        print("entrada inválida")

    def EncerrarSistema(self):  # OPÇÃO 0
        print()
        print("DESEJA ATUALIZAR O ESTOQUE?")

        while True:
            print()
            pergunta_atualizar_arquivo_1 = input('RESPONDA (S/N): ')

            if pergunta_atualizar_arquivo_1.lower() == "s":

                with  open("BancoDeLivros.txt", "w", encoding="utf8") as arquivo:

                    for livro in self.livros:
                        linha = (f"\n{livro.codigo},{livro.titulo},{livro.editora},{livro.categoria}"
                                 f",{livro.ano},{livro.valor},{livro.quantidade_em_estoque}")

                        arquivo.write(linha)

                print()
                print('Estoque Atualizado! Obrigado e volte sempre!')
                sys.exit()

            elif pergunta_atualizar_arquivo_1.lower() == "n":
                print()
                print("Obrigado e volte sempre!")
                sys.exit()

            else:
                print('ENTRADA INVÁLIDA!')


if __name__ == '__main__':
    SistemaDeLivraria().ExibirMenuInterativo()
