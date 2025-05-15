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
                f"Valor Total em Estoque: R$ {total_estoque:.2f}")


class SistemaDeLivraria:

    def __init__(self):

        self.livros = []

    def MostrarInfo(self):  # OPÇÃO 2 - MENU INTERATIVO

        if self.livros:

            for livro in self.livros:
                print(livro.info())
        else:
            print()
            print('NÃO HÁ LIVROS EM PROCESSO DE CADASTRO!')

        print()
        print(5 * "-=")

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

    def ExibirMenuInterativo(self):
        print(18 * "-=")
        print(18 * "-=")
        print("        --MENU PRINCIPAL--")
        print()
        print("> 1. Cadastrar novo livro")
        print("> 2. Listar livros em cadastro")
        print("> 3. Buscar livros por nome")
        print("> 4. Buscar livros por categoria")
        print("> 5. Buscar livros por preço")
        print("> 6. Busca por quantidade em estoque")
        print("> 7. Valor total no estoque")
        print("> 8. Carregar estoque")
        print("> 9. Atualizar arquivo de estoque")
        print("> 0. Encerrar atividades")
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

                    case 0:
                        self.EncerrarSistema()

                    case _:
                        print()
                        print('OPÇÃO INVÁLIDA')

            except ValueError:
                print()
                print("OPÇÃO INVÁLIDA")

    def CadastrarNovoLivro(self):  # OPÇÃO 1 DO MENU INTERATIVO
        print()
        print(18 * "-=")
        print("     >> CADASTRO DE LIVROS <<")

        while True:

            print()
            self.livros.append(Livro(input(">> Código do livro: "),
                                     input(">> Título do livro: "),
                                     input(">> Editora do livro: "),
                                     input(">> Categoria do livro: "),
                                     input(">> Ano do livro: "),
                                     float(input('>> Valor do livro: ')),
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
                            print('ENTRADA INVÁLIDA!')

                else:
                    print(18 * "-=")

                    print()
                    print(f"Quantidade de livros por categoria encontrados: {controle_iteracoes_busca_por_categoria}")
                    while True:
                        pergunta_3_busca_por_categoria = input("Gostaria de consultar outra categoria (s/n)? ")
                        if pergunta_3_busca_por_categoria.lower() == "s":
                            break
                        elif pergunta_3_busca_por_categoria.lower() == "n":
                            self.ExibirMenuInterativo()
                            break
                        else:
                            print()
                            print('RESPOSTA INVÁLIDA')
                            print()

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
            try:
                pergunta_1_busca_por_preco = float(
                    input("Digite seu valor máximo (Exemplo: 10.99 | ou digite 0 para sair): "))

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

                        while True:
                            print()
                            print("> 1. Solicitar nova busca")
                            print("> 2. Voltar ao menu principal")
                            print()
                            pergunta_2_busca_por_preco = input("Digite a opção desejada >>> ")

                            if pergunta_2_busca_por_preco == "1":
                                break
                            elif pergunta_2_busca_por_preco == "2":
                                self.ExibirMenuInterativo()
                            else:
                                print()
                                peinr('OPÇÃO INVÁLIDA')

                    else:
                        print(18 * "-=")

                        while True:
                            print()
                            print(f"Quantidade de livros com preço estimado: {controle_de_iteracoes_busca_por_preco}")
                            print()
                            pergunta_3_busca_por_preco = input("Gostaria de colicitar uma nova busca (s/n)? ")

                            if pergunta_3_busca_por_preco.lower() == "s":
                                break

                            elif pergunta_3_busca_por_preco.lower() == 'n':
                                self.ExibirMenuInterativo()
                                break

                            else:
                                print()
                                print('ENTRADA INVÁLIDA')

                else:
                    if pergunta_1_busca_por_preco == 0:
                        self.ExibirMenuInterativo()

            except ValueError:
                print()
                print("ENTRADA INVÁLIDA")
                print('Exemplo de Formato Correto para preços > 10.99')

    def BuscarPorQuantidadeEmEstoque(self):  # OPÇÃO 6 DO MENU INTERATIVO
        print()
        print(10 * "-=")
        print("--BUSCAR LIVRO POR QUANTIDADE EM ESTOQUE--")
        print()

        while True:
            print()
            try:
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
                        while True:
                            print()
                            print("> 1. Solicitar nova busca")
                            print("> 2. Voltar ao menu principal")
                            print()
                            pergunta_2_busca_por_por_estoque = input("Digite a opção desejada >>> ")

                            if pergunta_2_busca_por_por_estoque == "1":
                                break

                            elif pergunta_2_busca_por_por_estoque == "2":
                                self.ExibirMenuInterativo()

                            else:
                                print()
                                print('ENTRADA INVÁLIDA')

                    else:
                        print()
                        print(18 * "-=")
                        print(f"Quantidade informada: {pergunta_1_busca_por_estoque}")
                        print(
                            f"Total de livros com quantidade em estoque estimada: {controle_de_iteracoes_busca_por_estoque}")
                        while True:
                            print()
                            pergunta_3_busca_por_estoque = input("Gostaria de solicitar uma nova busca (s/n)? ")

                            if pergunta_3_busca_por_estoque.lower() == "s":
                                break
                            elif pergunta_3_busca_por_estoque.lower() == "n":
                                self.ExibirMenuInterativo()
                            else:
                                print()
                                print('ENTRADA INVÁLIDA')

                else:
                    if pergunta_1_busca_por_estoque == 0:
                        self.ExibirMenuInterativo()

            except ValueError:
                print()
                print('ENTRADA INVÁLIDA! DIGITE APENAS NÚMEROS')

    def ValorTotalEstoque(self):  # OPÇÃO 7 DO MENU INTERATIVO
        print()
        print(10 * "-=")
        print("--VALOR TOTAL EM ESTOQUE--")
        print()

        while True:

            try:
                print()
                pergunta_busca_por_valor_de_estoque = float(
                    input("Digite seu valor mínimo (Exemplo: 10.99 | ou digite 0 para sair): "))

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
                        while True:
                            print()
                            print("> 1. Solicitar nova busca")
                            print("> 2. Voltar ao menu principal")
                            print()
                            pergunta_2_busca_por_por_valor_de_estoque = input("Digite a opção desejada >>> ")

                            if pergunta_2_busca_por_por_valor_de_estoque == "1":
                                break

                            elif pergunta_2_busca_por_por_valor_de_estoque == "2":
                                self.ExibirMenuInterativo()

                            else:
                                print()
                                print('ENTRADA INVÁLIDA')

                    else:
                        print()
                        print(18 * "-=")
                        print(f"Valor informado : {pergunta_busca_por_valor_de_estoque}")
                        print(
                            f"Total de livros com valor estimado em estoque: {controle_de_iteracoes_busca_por_valor_de_estoque}")
                        while True:

                            print()
                            pergunta_3_busca_por_valor_de_estoque = input(
                                "Gostaria de solicitar uma nova busca (s/n)? ")

                            if pergunta_3_busca_por_valor_de_estoque.lower() == "s":
                                break
                            elif pergunta_3_busca_por_valor_de_estoque.lower() == "n":
                                self.ExibirMenuInterativo()
                            else:
                                print()
                                print('ENTRADA INVÁLIDA')

                else:
                    if pergunta_2_busca_por_valor_de_estoque == 0:
                        self.ExibirMenuInterativo()
            except ValueError:
                print()
                print('ENTRADA INVÁLIDA')

    def CarregarEstoque(self):  # OPÇÃO 8

        arquivo = open("BancoDeLivros.txt", "r", encoding="utf8")

        linha = arquivo.readline().replace("\n", "")

        while linha:
            linha_editada = linha.split(",")

            linha_editada[5] = linha_editada[5].replace("R$", "")
            linha_editada[5] = float(linha_editada[5])
            linha_editada[6] = int(linha_editada[6])

            novo_livro = Livro(linha_editada[0], linha_editada[1], linha_editada[2], linha_editada[3], linha_editada[4],
                               linha_editada[5], linha_editada[6])

            self.livros.append(novo_livro)

            linha = arquivo.readline().replace("\n", "")

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

                    for livro in self.livros:
                        linha = (f"{livro.codigo},{livro.titulo},{livro.editora},{livro.categoria}"
                                 f",{livro.ano},R${livro.valor},{livro.quantidade_em_estoque}\n")

                        arquivo.write(linha)

                print()
                print('Estoque Atualizado!')
                self.livros.clear()
                print()
                self.ExibirMenuInterativo()
                break


            elif pergunta_atualizar_arquivo_1.lower() == "n":
                self.ExibirMenuInterativo()

            else:
                print('ENTRADA INVÁLIDA!')

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
