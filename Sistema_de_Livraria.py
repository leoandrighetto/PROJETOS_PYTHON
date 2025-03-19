class SistemaDeCadastros:
    def __init__(self):
        self.livros = []  
        //     ["001", "O Grande Gatsby", "F. Scott Fitzgerald", "Romance", 1925, 45.0, 80],
        //     ["002", "1984", "George Orwell", "Distopia", 1949, 55.5, 100],
        //     ["003", "Sapiens", "Yuval Noah Harari", "História", 2011, 60.0, 120],
        //     ["004", "A Guerra dos Tronos", "George R. R. Martin", "Fantasia", 1996, 90.0, 70],
        //     ["005", "O Pequeno Príncipe", "Antoine de Saint-Exupéry", "Infantil", 1943, 40.0, 150],
        //     ["006", "A Origem das Espécies", "Charles Darwin", "Ciência", 1859, 85.0, 200],
        //     ["007", "A Arte da Guerra", "Sun Tzu", "Estratégia", -500, 50.0, 90],
        //     ["008", "O Diário de Anne Frank", "Anne Frank", "Biografia", 1947, 35.0, 110],
        //     ["009", "O Alquimista", "Paulo Coelho", "Ficção", 1988, 45.0, 140],
        //     ["010", "O Senhor dos Anéis: A Sociedade do Anel", "J.R.R. Tolkien", "Fantasia", 1954, 80.0, 130],
        //     ["011", "O Caçador de Pipas", "Khaled Hosseini", "Drama", 2003, 60.0, 100],
        //     ["012", "O Nome da Rosa", "Umberto Eco", "Mistério", 1980, 70.0, 150],
        //     ["013", "Crime e Castigo", "Fiódor Dostoiévski", "Filosofia", 1866, 95.0, 90],
        //     ["014", "O Mundo de Sofia", "Jostein Gaarder", "Filosofia", 1991, 65.0, 110],
        //     ["015", "A Menina que Roubava Livros", "Markus Zusak", "Drama", 2005, 75.0, 130],
        //     ["016", "O Senhor dos Anéis: As Duas Torres", "J.R.R. Tolkien", "Fantasia", 1954, 85.0, 150],
        //     ["017", "O Guia do Mochileiro das Galáxias", "Douglas Adams", "Ficção", 1979, 72.5, 180],
        //     ["018", "A Revolução dos Bichos", "George Orwell", "Distopia", 1945, 40.0, 200],
        //     ["019", "O Hobbit", "J.R.R. Tolkien", "Ficção", 1937, 50.0, 90],
        //     ["020", "O Sol é para Todos", "Harper Lee", "Drama", 1960, 60.0, 100]
        //      # 0              1              2             3      4     5     6

    def info(self):

        for informacoes_livros in range(len(self.livros)):
            print()
            print(f">>>CÓDIGO: {self.livros[informacoes_livros][0]}\n"
                  f"Título/Editora: {self.livros[informacoes_livros][1]}/{self.livros[informacoes_livros][2]}\n"
                  f"Categoria: {self.livros[informacoes_livros][3]}\n"
                  f"Ano: {self.livros[informacoes_livros][4]}\n"
                  f"Valor: R$ {self.livros[informacoes_livros][5]}\n"
                  f"Estoque: {self.livros[informacoes_livros][6]} unidades\n"
                  f"Valor em Estoque: R$ {self.livros[informacoes_livros][6] * self.livros[informacoes_livros][5]}")

        print()
        print(5 * "-=")
        print("RESPONDA COM S / N:")
        pergunta_info = input('DESEJA CADASTRAR MAIS LIVROS? ')

        opcao_escolhida_info = self

        if pergunta_info.lower() == "s":
            opcao_escolhida_info.CadastrarNovoLivro()
        else:
            opcao_escolhida_info.MenuInterativo()

    def MenuInterativo(self):
        print()
        print(10 * "-=")
        print("--MENU PRINCIPAL--")
        print()
        print("> 1. CADASTRAR UM NOVO LIVRO")
        print("> 2. LISTAR LIVROS")
        print("> 3. BUSCAR LIVRO PELO NOME")
        print("> 4. BUSCAR LIVRO POR CATEGORIA")
        print("> 5. BUSCA LIVRO POR PREÇO DE LIVRO")
        print("> 6. BUSCA POR QUANTIDADE EM ESTOQUE")
        print("> 7. VALOR TOTAL EM ESTOQUE")
        print("> 0. ENCERRAR ATIVIDADES")
        print()
        print(5 * "-=")

        pergunta_menu_interativo = int(input("Digite a opção desejada (Ex.: 1) >>>> "))

        opcao_escolhida_menu_interativo = self

        if pergunta_menu_interativo == 1:
            opcao_escolhida_menu_interativo.CadastrarNovoLivro()  # CONDICIONA O USUÁRIO AO MENU DE CADASTRO

        elif pergunta_menu_interativo == 2:
            opcao_escolhida_menu_interativo.info()

        elif pergunta_menu_interativo == 3:
            opcao_escolhida_menu_interativo.BuscaPorNome()

        elif pergunta_menu_interativo == 4:
            opcao_escolhida_menu_interativo.BuscaPorCategoria()

        elif pergunta_menu_interativo == 5:
            opcao_escolhida_menu_interativo.BuscaPorPreco()

        elif pergunta_menu_interativo == 6:
            opcao_escolhida_menu_interativo.BuscaPorEstoque()

    def CadastrarNovoLivro(self):
        print()
        print(10 * "-=")
        print("--CADASTRO DE LIVROS--")

        while True:
            novo_livro = []
            print()

            codigo = input("> DIGITE O CÓDIGO DO LIVRO: ")
            novo_livro.append(codigo)

            titulo = input("> DIGITE O TÍTULO DO LIVRO: ")
            novo_livro.append(titulo)

            editora = input("> DIGITE A EDITORA DO LIVRO: ")
            novo_livro.append(editora)

            categoria = input("> DIGITE A CATEGORIA DO LIVRO: ")
            novo_livro.append(categoria)

            ano = int(input('> DIGITE O ANO DO LIVRO: '))
            novo_livro.append(ano)

            valor = int(input('> DIGITE O VALOR DO LIVRO: '))
            novo_livro.append(valor)

            quantidade_em_estoque = int(input('> DIGITE A QUANTIDADE EM ESTOQUE DO LIVRO: '))
            novo_livro.append(quantidade_em_estoque)

            self.livros.append(novo_livro)

            # INTERAÇÃO-#INTERAÇÃO-#INTERAÇÃO-#INTERAÇÃO

            print()
            print(5 * "-=")
            print("RESPONDA COM S / N:")
            pergunta_cadastro_novo_livro = input("DESEJA CADASTRAR MAIS LIVROS? ")

            opcao_escolhida_cadastrar_novo_livro = self

            if pergunta_cadastro_novo_livro.lower() == 'n':
                opcao_escolhida_cadastrar_novo_livro.MenuInterativo()
                break

    def BuscaPorNome(self):
        print()
        print(5 * "-=")
        print("--BUSCAR LIVRO POR NOME--")
        print()

        while True:
            pergunta_1_busca_por_nome = input("DIGITE O NOME DO LIVRO (0 - SAIR): ")

            opcao_escolhida_busca_por_nome = self

            if pergunta_1_busca_por_nome.lower() != "0":
                controle_de_iteracoes_busca_nome = 0
                for informacoes_livros in range(len(self.livros)):
                    if pergunta_1_busca_por_nome.lower() == self.livros[informacoes_livros][1].lower():
                        print()
                        print(f">>>CÓDIGO: {self.livros[informacoes_livros][0]}\n"
                              f"TÍTULO/Editora: {self.livros[informacoes_livros][1]}/{self.livros[informacoes_livros][2]}\n"
                              f"Categoria: {self.livros[informacoes_livros][3]}\n"
                              f"Ano: {self.livros[informacoes_livros][4]}\n"
                              f"Valor: R$ {self.livros[informacoes_livros][5]}\n"
                              f"Estoque: {self.livros[informacoes_livros][6]} unidades\n"
                              f"Valor em Estoque: R$ {self.livros[informacoes_livros][6] * self.livros[informacoes_livros][5]}")
                    else:
                        controle_de_iteracoes_busca_nome += 1
            if controle_de_iteracoes_busca_nome == len(self.livros):
                print("LIVRO NÃO ENCONTRADO")

            elif pergunta_1_busca_por_nome.lower() == "0":
                opcao_escolhida_busca_por_nome.MenuInterativo()
                break

            print()
            print(f"LIVROS ENCONTRADOS: {len(self.livros) - controle_de_iteracoes_busca_nome}")
            pergunta_2_busca_por_nome = input("GOSTARIA DE CONSULTAR OUTRO LIVRO (S/ N)? ")

            if pergunta_2_busca_por_nome.lower() == "n":
                opcao_escolhida_busca_por_nome.MenuInterativo()

    def BuscaPorCategoria(self):
        print()
        print(5 * "-=")
        print("--BUSCAR LIVRO POR CATEGORIA--")
        print()

        while True:
            pergunta_1_busca_por_categoria = input("DIGITE O NOME DA CATEGORIA (0 - SAIR): ")

            opcao_escolhida_busca_por_categoria = self

            if pergunta_1_busca_por_categoria.lower() != "0":
                controle_de_iteracoes_busca_categoria = 0
                for informacoes_livros in range(len(self.livros)):
                    if pergunta_1_busca_por_categoria.lower() == self.livros[informacoes_livros][3].lower():
                        print(f"{self.livros[informacoes_livros][1]}")

                    else:
                        controle_de_iteracoes_busca_categoria += 1

            if controle_de_iteracoes_busca_categoria == len(self.livros):
                print("CATEGORIA NÃO ENCONTRADA")

            elif pergunta_1_busca_por_categoria.lower() == "0":
                opcao_escolhida_busca_por_categoria.MenuInterativo()
                break

            print()
            print(f"TOTAL DE LIVROS POR CATEGORIA: {len(self.livros) - controle_de_iteracoes_busca_categoria}")
            pergunta_2_busca_por_categoria = input("GOSTARIA DE CONSULTAR OUTRA CATEGORIA (S/ N)? ")

            if pergunta_2_busca_por_categoria.lower() == "n":
                opcao_escolhida_busca_por_categoria.MenuInterativo()

    def BuscaPorPreco(self):
        print()
        print(5 * "-=")
        print("--BUSCAR LIVRO POR PRECO--")
        print()

        while True:
            pergunta_1_busca_por_preco = int(input("DIGITE O NOME DA CATEGORIA (0 - SAIR): "))

            opcao_escolhida_busca_por_preco = self

            if pergunta_1_busca_por_preco != 0:

                controle_de_iteracoes_busca_preco = 0

                for informacoes_livros in range(len(self.livros)):
                    if self.livros[informacoes_livros][5] <= pergunta_1_busca_por_preco:

                        print()
                        print(f">>>CÓDIGO: {self.livros[informacoes_livros][0]}\n"
                              f"TÍTULO/Editora: {self.livros[informacoes_livros][1]}/{self.livros[informacoes_livros][2]}\n"
                              f"Categoria: {self.livros[informacoes_livros][3]}\n"
                              f"Ano: {self.livros[informacoes_livros][4]}\n"
                              f"Valor: R$ {self.livros[informacoes_livros][5]}\n"
                              f"Estoque: {self.livros[informacoes_livros][6]} unidades\n"
                              f"Valor em Estoque: R$ {self.livros[informacoes_livros][6] * self.livros[informacoes_livros][5]}")
                    else:
                        controle_de_iteracoes_busca_preco += 1

            if controle_de_iteracoes_busca_preco == len(self.livros):
                print("PREÇO NÃO ENCONTRADO")

            elif pergunta_1_busca_por_preco == 0:
                opcao_escolhida_busca_por_preco.MenuInterativo()
                break

            print()
            print(f"TOTAL DE LIVROS ENCONTRADOS: {len(self.livros) - controle_de_iteracoes_busca_preco}")
            pergunta_2_busca_por_preco = input("GOSTARIA DE CONSULTAR OUTRO PREÇO (S/ N)? ")

            if pergunta_2_busca_por_preco == "n":
                opcao_escolhida_busca_por_preco.MenuInterativo()

    def BuscaPorEstoque(self):
        print()
        print(5 * "-=")
        print("--BUSCAR LIVRO POR QUANTIDADE EM ESTOQUE--")
        print()

        while True:
            pergunta_1_busca_por_estoque = int(input("DIGITE A QUANTIDADE NECESSÁRIA (0 - SAIR): "))

            opcao_escolhida_busca_por_estoque = self

            if pergunta_1_busca_por_estoque != 0:

                controle_de_iteracoes_busca_por_estoque = 0

                for informacoes_livros in range(len(self.livros)):
                    if self.livros[informacoes_livros][6] <= pergunta_1_busca_por_estoque:

                        print()
                        print(f"TÍTULO/Editora: {self.livros[informacoes_livros][1]}\n"
                              f"Quantidade Em Estoque: {self.livros[informacoes_livros][6]} unidades")
                    else:
                        controle_de_iteracoes_busca_por_estoque += 1

            if controle_de_iteracoes_busca_por_estoque == len(self.livros):
                print("ESTOQUE NÃO ENCONTRADO")

            elif pergunta_1_busca_por_estoque == 0:
                opcao_escolhida_busca_por_estoque.MenuInterativo()
                break

            print()
            print(f"TOTAL DE LIVROS ENCONTRADOS: {len(self.livros) - controle_de_iteracoes_busca_por_estoque}")
            pergunta_2_busca_por_estoque = input("GOSTARIA DE CONSULTAR OUTRA DEMANDA (S/ N)? ")

            if pergunta_2_busca_por_estoque == "n":
                opcao_escolhida_busca_por_estoque.MenuInterativo()

Sistema = SistemaDeCadastros()

Sistema.MenuInterativo()
