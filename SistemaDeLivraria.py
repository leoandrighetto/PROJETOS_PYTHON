from ntpath import split

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
                f"Valor Total em Estoque: R$ {self.valor * self.quantidade_em_estoque}")

class SistemaDeLivraria:

    def __init__(self):

        self.Livros = []


    def MostrarInfo(self):  # OPÇÃO 2 - MENU INTERATIVO

        banco_de_livros = open("Livros.txt", "r")

        linha_do_banco = banco_de_livros.readline().replace("\n","")

        banco_editado = linha_do_banco.split(",")

        while linha_do_banco:

            novo_livro = Livro(banco_editado[0],banco_editado[1],banco_editado[2],banco_editado[3],int(banco_editado[4]),float(banco_editado[5]),int(banco_editado[6]))
            self.Livros.append(novo_livro)

            linha_do_banco = banco_de_livros.readline().replace("\n", "")
            banco_editado = linha_do_banco.split(",")



        for livro in self.Livros:
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

            case 8:
                self.CarregarEstoque()

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

                controle_iteracoes_busca_por_categoria = 0
                categoria_encontrada = False
                for livro in self.livros:
                    if pergunta_1_busca_por_categoria.lower() == livro.categoria.lower():
                        categoria_encontrada = True
                        print(livro.info())
                        controle_iteracoes_busca_por_categoria += 1

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
                    print(f"Quantidade de livros por categoria encontrados: {controle_iteracoes_busca_por_categoria}")
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

                preco_encontrado = False
                controle_de_iteracoes_busca_por_preco = 0
                for livro in self.livros:
                    if livro.valor <= pergunta_1_busca_por_preco:
                        preco_encontrado = True
                        print()
                        print(livro.info())
                        controle_de_iteracoes_busca_por_preco += 1

                if preco_encontrado == False:
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
                    print(f"Quantidade de livros com preço estimado: {controle_de_iteracoes_busca_por_preco}")
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
                quantidade_em_estoque_encontrada = False
                for livro in self.livros:
                    if livro.quantidade_em_estoque <= pergunta_1_busca_por_estoque:
                        quantidade_em_estoque_encontrada = True
                        print(livro.info())
                        controle_de_iteracoes_busca_por_estoque += 1

                if quantidade_em_estoque_encontrada == False:
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
                        f"Total de livros com quantidade em estoque estimada: {controle_de_iteracoes_busca_por_estoque}")
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

        while True:
            print()
            pergunta_busca_por_valor_de_estoque = int(input("Digite o valor mínimo procurado: (0 - SAIR): "))

            if pergunta_busca_por_valor_de_estoque != 0:

                controle_de_iteracoes_busca_por_valor_de_estoque = 0
                valor_encontrado = False

                for livro in self.livros:
                    valor_total = livro.quantidade_em_estoque * livro.valor
                    if pergunta_busca_por_valor_de_estoque < valor_total:
                        valor_encontrado = True
                        print(livro.info())
                        controle_de_iteracoes_busca_por_valor_de_estoque += 1

                if valor_encontrado == False:
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
                    print(f"Valor informado : {pergunta_busca_por_valor_de_estoque}")
                    print(
                        f"Total de livros com valor estimado em estoque: {controle_de_iteracoes_busca_por_valor_de_estoque}")
                    print()
                    pergunta_4_busca_por_valor_de_estoque = input("Gostaria de solicitar uma nova busca (s/n)? ")

                    if pergunta_4_busca_por_valor_de_estoque.lower() == "n":
                        self.ExibirMenuInterativo()

            else:
                if pergunta_2_busca_por_valor_de_estoque == 0:
                    self.ExibirMenuInterativo()

    def CarregarEstoque():

# O cliente deseja que seja implementada uma funcionalidade para
# carregar os livros cadastrados através de um arquivo txt (nova opção 8 - carregar
# estoque). Quando indagado sobre como as informações serão postas no arquivo eles
# passaram o seguinte exemplo:
#   3426,compiladores,2012,computação,pearson,R$135.50,50
#   2631,sistemas digitais,2017,computação,liber,R$99.90,30
#   9680,senhor dos aneis: a sociedade do anel,2005,fantasia,harper,R$35.00,120

# ou seja o formato pode ser visto como:

#   <codigo>,<titulo>,<ano>,<área/gênero>,<editora>,R$<valor>,<qtd em estoque>






#OU SEJA:

# OS LIVROS NÃO SERÃO MAIS ARMAZENADOS EM UMA LISTA DENTRO DA CLASSE, E SIM DENTRO DO ARQUIVO txt.
#












        pass


if __name__ == '__main__':
    SistemaDeLivraria().ExibirMenuInterativo()
