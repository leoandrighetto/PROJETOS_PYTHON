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
        print()
        return (f">>>CÓDIGO: {self.codigo}\n"
                f"Título/Editora: {self.titulo}/{self.editora}\n"
                f"Categoria: {self.categoria}\n"
                f"Ano: {self.ano}\n"
                f"Valor: R$ {self.valor}\n"
                f"Estoque: {self.quantidade_em_estoque} unidades\n"
                f"Valor em Estoque: R$ {self.valor * self.quantidade_em_estoque}")


class SistemaDeLivraria:

    def __init__(self):

        self.livros = [
            Livro("001", "O Grande Gatsby", "F. Scott Fitzgerald", "Romance", 1925, 45.0, 80),
            Livro("002", "1984", "George Orwell", "Distopia", 1949, 55.5, 100),
            Livro("003", "Sapiens", "Yuval Noah Harari", "História", 2011, 60.0, 120),
            Livro("004", "A Guerra dos Tronos", "George R. R. Martin", "Fantasia", 1996, 90.0, 70),
            Livro("005", "O Pequeno Príncipe", "Antoine de Saint-Exupéry", "Infantil", 1943, 40.0, 150),
            Livro("006", "A Origem das Espécies", "Charles Darwin", "Ciência", 1859, 85.0, 200),
            Livro("007", "A Arte da Guerra", "Sun Tzu", "Estratégia", -500, 50.0, 90),
            Livro("008", "O Diário de Anne Frank", "Anne Frank", "Biografia", 1947, 35.0, 110),
            Livro("009", "O Alquimista", "Paulo Coelho", "Ficção", 1988, 45.0, 140),
            Livro("010", "O Senhor dos Anéis: A Sociedade do Anel", "J.R.R. Tolkien", "Fantasia", 1954, 80.0, 130),
            Livro("011", "O Caçador de Pipas", "Khaled Hosseini", "Drama", 2003, 60.0, 100),
            Livro("012", "O Nome da Rosa", "Umberto Eco", "Mistério", 1980, 70.0, 150),
            Livro("013", "Crime e Castigo", "Fiódor Dostoiévski", "Filosofia", 1866, 95.0, 90),
            Livro("014", "O Mundo de Sofia", "Jostein Gaarder", "Filosofia", 1991, 65.0, 110),
            Livro("015", "A Menina que Roubava Livros", "Markus Zusak", "Drama", 2005, 75.0, 130),
            Livro("016", "O Senhor dos Anéis: As Duas Torres", "J.R.R. Tolkien", "Fantasia", 1954, 85.0, 150),
            Livro("017", "O Guia do Mochileiro das Galáxias", "Douglas Adams", "Ficção", 1979, 72.5, 180),
            Livro("018", "A Revolução dos Bichos", "George Orwell", "Distopia", 1945, 40.0, 200),
            Livro("019", "O Hobbit", "J.R.R. Tolkien", "Ficção", 1937, 50.0, 90),
            Livro("020", "O Sol é para Todos", "Harper Lee", "Drama", 1960, 60.0, 100)
        ]  # 0              1              2             3      4     5     6

    def MostrarInfo(self):  # OPÇÃO 2 - MENU INTERATIVO

        for livro in self.livros:
            print(livro.info())

        print()
        print(5 * "-=")
        print("RESPONDA COM S / N:")

        pergunta_MostrarInfo = input('DESEJA CADASTRAR MAIS LIVROS? ')

        # opcao_escolhida_info = self

        if pergunta_MostrarInfo.lower() == "s":
            self.CadastrarNovoLivro()
        else:
            self.ExibirMenuInterativo()

    def ExibirMenuInterativo(self):
        print(18 * "-=")
        print(18 * "-=")
        print("        --MENU PRINCIPAL--")
        print()
        print("> 1. CADASTRAR NOVO LIVRO")
        print("> 2. LISTAR LIVROS")
        print("> 3. BUSCAR LIVROS POR NOME")
        print("> 4. BUSCAR LIVROS POR CATEGORIA")
        print("> 5. BUSCAR LIVROS POR PREÇO")
        print("> 6. BUSCA POR QUANTIDADE EM ESTOQUE")
        print("> 7. VALOR TOTAL NO ESTOQUE")
        print("> 0. ENCERRAR ATIVIDADES")
        print()
        print(18 * "-=")

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

            case 0:
                print()
                print(18 * "-=")
                print()
                print('             OBRIGADO')
                sys.exit()

    def CadastrarNovoLivro(self):  # OPÇÃO 1 DO MENU INTERATIVO
        print()
        print(18 * "-=")
        print("     >> CADASTRO DE LIVROS <<")

        while True:

            print()
            # codigo = input(">> Código do livro: ")
            # titulo = input(">> Título do livro: ")
            # editora = input(">> Editora do livro: ")
            # categoria = input(">> Categoria do livro: ")
            # ano = int(input('>> Ano do livro: '))
            # valor = int(input('>> Valor do livro: '))
            # quantidade_em_estoque = int(input('>> Digite a quantidade em estoque do livro: '))
            #
            # self.livros.append(Livro(codigo, titulo, editora, categoria, ano, valor, quantidade_em_estoque))

            self.livros.append(Livro(input(">> Código do livro: "),
                                     input(">> Título do livro: "),
                                     input(">> Editora do livro: "),
                                     input(">> Categoria do livro: "),
                                     input(">> Ano do livro: "),
                                     int(input('>> Valor do livro: ')),
                                     int(input('>> Digite a quantidade em estoque do livro: '))))

            # INTERAÇÃO-#INTERAÇÃO-#INTERAÇÃO-#INTERAÇÃO

            print()
            print(18 * "-=")
            print()
            print('    LIVRO CADASTRADO COM SUCESSO!')
            print()
            print('> OPÇÕES:')
            print("> 1. CADASTRAR NOVO LIVRO")
            print("> 2. VOLTAR AO MENU PRINCIPAL")
            print()

            pergunta_cadastro_novo_livro = int(input("Digite a opção desejada >>  "))

            if pergunta_cadastro_novo_livro == 2:
                self.ExibirMenuInterativo()
                break

    def BuscarPorNome(self):  # OPÇÃO 3 DO MENU INTERATIVO
        print()
        print(18 * "-=")
        print("     --BUSCAR LIVRO POR NOME--")

        while True:
            print()
            pergunta_1_busca_por_nome = input("Digite o nome do livro (ou 0 para sair): ")

            if pergunta_1_busca_por_nome.lower() != "0":  # Se o usuário digitou algum nome

                livro_encontrado = False  # Se continuar falso, significa que nenhum livro foi encontrado.
                for livro in self.livros:
                    if pergunta_1_busca_por_nome.lower() in livro.titulo.lower():
                        print(livro.info())
                        livro_encontrado = True

                if not livro_encontrado:
                    print()
                    print("LIVRO NÃO ENCONTRADO!")
                    print()
                    print("> 1. Buscar novo livro")
                    print("> 2. Voltar ao menu principal")
                    print()
                    pergunta_2_busca_por_nome = int(input("Digite a opção desejada >>> "))

                    if pergunta_2_busca_por_nome != 1:
                        self.ExibirMenuInterativo()


                else:
                    print(18 * "-=")
                    print()
                    pergunta_3_busca_por_nome = input("Gostaria de consultar outro livro (s/ n)? ")

                    if pergunta_3_busca_por_nome.lower() == "n":
                        self.ExibirMenuInterativo()

            else:
                self.ExibirMenuInterativo()

    def BuscarPorCategoria(self):  # OPÇÃO 4 DO MENU INTERATIVO
        print()
        print(18 * "-=")
        print("   --BUSCAR LIVRO POR CATEGORIA--")
        print()

        while True:
            pergunta_1_busca_por_categoria = input("Digite o nome da categoria (ou 0 para sair): ")

            if pergunta_1_busca_por_categoria.lower() != "0":

                categoria_encontrada = False
                for livro in self.livros:
                    if pergunta_1_busca_por_categoria.lower() == livro.categoria.lower():
                        print(livro.info())
                        categoria_encontrada = True

                if not categoria_encontrada:
                    print()
                    print("CATEGORIA NÃO ENCONTRADA!")
                    print()
                    print("> 1. Buscar nova categoria")
                    print("> 2. Voltar ao menu principal")
                    print()
                    pergunta_2_busca_por_categoria = int(input("Digite a opção desejada >>> "))

                    if pergunta_2_busca_por_categoria != 1:
                        self.ExibirMenuInterativo()


                else:
                    print(18 * "-=")
                    print()
                    pergunta_3_busca_por_categoria = input("Gostaria de consultar outra categoria (s/n)? ")

                    if pergunta_3_busca_por_categoria.lower() == "n":
                        self.ExibirMenuInterativo()

            else:
                if pergunta_1_busca_por_categoria == "0":
                    self.ExibirMenuInterativo()

    def BuscarPorPreco(self):  # OPÇÃO 5 DO MENU INTERATIVO
        print()
        print(18 * "-=")
        print("   --BUSCAR LIVROS POR PREÇO--")
        print()

        while True:
            print()
            pergunta_1_busca_por_preco = float(input("Digite seu valor máximo (ou 0 para sair): "))

            if pergunta_1_busca_por_preco != 0:

                for livro in self.livros:
                    if livro.valor <= pergunta_1_busca_por_preco:
                        print()
                        print(livro.info())
                    else:
                        controle_de_iteracoes_busca_preco += 1

                if controle_de_iteracoes_busca_preco == len(self.livros):
                    print()
                    print("PREÇO ESTIMADO INEXISTENTE!")
                    print()
                    print("> 1. Solicitar nova busca")
                    print("> 2. Voltar ao menu principal")
                    print()
                    pergunta_2_busca_por_preco = int(input("Digite a opção desejada >>> "))

                    if pergunta_2_busca_por_preco != 1:
                        self.ExibirMenuInterativo()


                else:
                    print(18 * "-=")
                    print()
                    pergunta_3_busca_por_preco = input("Gostaria de colicitar uma nova busca (s/n)? ")

                    if pergunta_3_busca_por_preco.lower() == "n":
                        self.ExibirMenuInterativo()

            else:
                if pergunta_1_busca_por_preco == 0:
                    self.ExibirMenuInterativo()

    def BuscarPorQuantidadeEmEstoque(self):  # OPÇÃO 6 DO MENU INTERATIVO
        print()
        print(10 * "-=")
        print("--BUSCAR LIVRO POR QUANTIDADE EM ESTOQUE--")
        print()

        while True:
            print()
            pergunta_1_busca_por_estoque = int(input("Digite a quantidade desejada (ou 0 para sair): "))

            if pergunta_1_busca_por_estoque != 0:

                controle_de_iteracoes_busca_por_estoque = 0

                for livro in self.livros:
                    if livro.quantidade_em_estoque <= pergunta_1_busca_por_estoque:
                        livro.info()


                    else:
                        controle_de_iteracoes_busca_por_estoque += 1

                if controle_de_iteracoes_busca_por_estoque == len(self.livros):
                    print()
                    print("QUANTIDADE ESTIMADA INEXISTENTE!")
                    print()
                    print("> 1. Solicitar nova busca")
                    print("> 2. Voltar ao menu principal")
                    print()
                    pergunta_2_busca_por_por_estoque = int(input("Digite a opção desejada >>> "))

                    if pergunta_2_busca_por_por_estoque != 1:
                        self.ExibirMenuInterativo()


                else:
                    print()
                    print(18 * "-=")
                    print(f"Quantidade informada: {pergunta_1_busca_por_estoque}")
                    print(
                        f"Total de livros com quantidade em estoque estimada: {len(self.livros) - controle_de_iteracoes_busca_por_estoque}")
                    print()
                    pergunta_3_busca_por_estoque = input("Gostaria de solicitar uma nova busca (s/n)? ")

                    if pergunta_3_busca_por_estoque.lower() == "n":
                        self.ExibirMenuInterativo()

            else:
                if pergunta_1_busca_por_estoque == 0:
                    self.ExibirMenuInterativo()

    def ValorTotalEstoque(self):  # OPÇÃO 7 DO MENU INTERATIVO
        print()
        print(10 * "-=")
        print("--VALOR TOTAL EM ESTOQUE--")
        print()

        valor_total_em_estoque = 0
        for livro in self.livros:
            valor_total_em_estoque += (livro.valor * livro.quantidade_em_estoque)

        print(f"O Valor total em estoque é de: R${valor_total_em_estoque}")
        print()
        print("> 1. Buscar livro por valor total em estoque")
        print("> 2. Voltar ao menu principal")
        print()

        pergunta_1_busca_por_valor_de_estoque = int(input("Digite a opção desejada: "))

        if pergunta_1_busca_por_valor_de_estoque == 1:

            while True:
                print()
                pergunta_2_busca_por_valor_de_estoque = int(input("Digite o valor mínimo da busca: (0 - SAIR): "))

                if pergunta_2_busca_por_valor_de_estoque != 0:

                    controle_de_iteracoes_busca_por_valor_de_estoque = 0

                    for livro in self.livros:
                        valor_total_de_estoque = livro.quantidade_em_estoque * livro.valor
                        if pergunta_2_busca_por_valor_de_estoque < valor_total_de_estoque:
                            livro.info()

                        else:
                            controle_de_iteracoes_busca_por_valor_de_estoque += 1

                    if controle_de_iteracoes_busca_por_valor_de_estoque == len(self.livros):
                        print()
                        print("VALOR ESTIMADO INEXISTENTE!")
                        print()
                        print("> 1. Solicitar nova busca")
                        print("> 2. Voltar ao menu principal")
                        print()
                        pergunta_3_busca_por_por_valor_de_estoque = int(input("Digite a opção desejada >>> "))

                        if pergunta_3_busca_por_por_valor_de_estoque != 1:
                            self.ExibirMenuInterativo()

                    else:
                        print()
                        print(18 * "-=")
                        print(f"Valor informado : {pergunta_2_busca_por_valor_de_estoque}")
                        print(f"Total de livros com valor estimado em estoque: "
                              f"{len(self.livros) - controle_de_iteracoes_busca_por_valor_de_estoque}")
                        print()
                        pergunta_4_busca_por_valor_de_estoque = input("Gostaria de solicitar uma nova busca (s/n)? ")

                        if pergunta_4_busca_por_valor_de_estoque.lower() == "n":
                            self.ExibirMenuInterativo()

                else:
                    if pergunta_2_busca_por_valor_de_estoque == 0:
                        self.ExibirMenuInterativo()
        else:
            self.ExibirMenuInterativo()


if __name__ == '__main__':
    SistemaDeLivraria().ExibirMenuInterativo()
