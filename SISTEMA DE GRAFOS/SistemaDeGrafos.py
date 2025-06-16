class Grafos:

    def __init__(self, vertice=None):
        self.cidades = []
        self.conexoes = []
        self.conexoes_especificas = {}
        self.vizinhanca = {}

    def cadastrar_cidade(self):

        print('\n*** Cadastro de cidades ***\n')

        while True:

            nome_cidade = input('Digite o nome da cidade: \n')

            if nome_cidade.lower() not in [vertice.nome_cidade.lower() for vertice in self.cidades]:
                self.cidades.append(Vertice(nome_cidade))

                pergunta_usuario = input('Deseja cadastrar mais cidades (s/n) ? \n')

                if pergunta_usuario.lower() == "s":
                    continue

                elif pergunta_usuario.lower() == "n":
                    self.menu()
                    break
                else:
                    print('\nentrada invalida\n')

            else:
                while True:
                    per = input('Cidade Já cadastrada. Deseja tentar de novo(s/n)? \n')
                    if per.lower() == "s":
                        break

                    elif per.lower() == "n":
                        self.menu()
                        return
                    else:
                        print('\nentrada invalida\n')

    def cadastrar_conexao(self):

        with open("Banco_de_grafos.csv", "a", encoding="utf-8") as arquivo:

            print('\n*** Cadastro de conexão ***\n')
            while True:

                cidade1 = input('Digite o nome da cidade 1: \n')
                cidade2 = input('Digite o nome da cidade 2: \n')

                while True:
                    try:
                        distancia = float(input('Digite a distância entre as cidades (ex: 200.1): \n'))
                        if distancia:
                            break
                    except ValueError:
                        print('\nentrada invalida\n')

                nova_aresta2 = Aresta(cidade2, cidade1, distancia)
                nova_aresta1 = Aresta(cidade1, cidade2, distancia)

                ### CADASTRO CIDADE
                lista_cidades = [cidades.nome_cidade.lower() for cidades in self.cidades]

                if cidade1.lower() == cidade2.lower():
                    print('não é possível conectar uma cidade à ela mesma')
                    continue

                if cidade1.lower() not in lista_cidades:
                    self.cidades.append(Vertice(cidade1))

                if cidade2.lower() not in lista_cidades:
                    self.cidades.append(Vertice(cidade2))

                ### LISTA CONEXÕES E ARQUIVO CSV:

                existe1 = False
                existe2 = False

                for aresta in self.conexoes:
                    if aresta == nova_aresta1:
                        existe1 = True
                    if aresta == nova_aresta2:
                        existe2 = True

                if existe1 == False:
                    self.conexoes.append(nova_aresta1)
                    linha = (f'{cidade1}, {cidade2}, {distancia:.1f}Km\n')
                    arquivo.write(linha)

                if existe2 == False:
                    self.conexoes.append(nova_aresta2)
                    linha = (f'{cidade2}, {cidade1}, {distancia:.1f}Km\n')
                    arquivo.write(linha)

                ### CONEXÕES ESPECÍFICAS
                d_c = self.conexoes_especificas  # d_c = dicionario de conexoes

                if not d_c:
                    d_c[cidade1.lower()] = [nova_aresta1]
                    d_c[cidade2.lower()] = [nova_aresta2]

                else:
                    if cidade1.lower() not in d_c:
                        d_c[cidade1.lower()] = [nova_aresta1]
                    else:
                        if nova_aresta1 not in d_c[cidade1.lower()]:
                            d_c[cidade1.lower()].append(nova_aresta1)
                        else:
                            print('Conexão já existe\n')

                    if cidade2.lower() not in d_c:
                        d_c[cidade2.lower()] = [nova_aresta2]
                    else:
                        if nova_aresta2 not in d_c[cidade2.lower()]:

                            d_c[cidade2.lower()].append(nova_aresta2)
                        else:
                            print('Conexão já existe\n')

                ### CIDADES VIZINHAS
                d_v = self.vizinhanca

                if not d_v:
                    d_v[cidade1.lower()] = [cidade2]
                    d_v[cidade2.lower()] = [cidade1]
                else:
                    if cidade1.lower() not in d_v:
                        d_v[cidade1.lower()] = [cidade2]
                    else:
                        if cidade2 not in d_v[cidade1.lower()]:
                            d_v[cidade1.lower()].append(cidade2)

                    if cidade2.lower() not in d_v:
                        d_v[cidade2.lower()] = [cidade1]
                    else:
                        if cidade1 not in d_v[cidade2.lower()]:
                            d_v[cidade2.lower()].append(cidade1)

                while True:
                    per = input("deseja cadastrar mais conexões (s/n) ? \n")

                    if per.lower() == "s":
                        break
                    elif per.lower() == "n":
                        self.menu()
                        return
                    else:
                        print('entrada inválida\n')

    def info_cidades(self):  # 3 - Listar Cidades
        print("\nLista de Cidades:\n")

        cidades_ordenadas = sorted(self.cidades, key=lambda cidade: cidade.nome_cidade)

        for i in cidades_ordenadas:
            print(f'{i.nome_cidade}')

        self.menu()

    def info_conexoes(self):  # 4 - Listas conexões - Lista TODAS as Arestas
        print("\nLista de Conexões:\n")

        for i in self.conexoes:
            print(f'Origem: {i.cidade1} \n'
                  f'Destino: {i.cidade2} \n'
                  f'Distância: {i.distancia:.1f}Km\n\n')

        self.menu()

    def info_vizinhos(self):

        while True:
            c_e = input('Digite o nome da cidade: ')

            lista = self.vizinhanca
            conexoes = self.conexoes_especificas

            if c_e.lower() in lista:

                distancias_ordenadas = sorted(conexoes[c_e.lower()], key=lambda aresta: aresta.distancia)

                for aresta in distancias_ordenadas:
                    print(f'\n\nVizinho: {aresta.cidade2} ->> {aresta.distancia:.1f}Km de distância\n\n')

                while True:
                    per = input('Gostaria de buscar novamente(s/n)? ')
                    if per.lower() == 's':
                        break
                    else:
                        self.menu()
                        return

            else:
                print('\n\ncidade não encontrada\n\n')
                while True:
                    per = input('Gostaria de buscar novamente (s/n)? ')
                    if per.lower() == 's':
                        break
                    else:
                        self.menu()
                        return

    def menu(self):

        print(f'*** Sistema de Grafos ***\n\n'
              '1 - Cadastrar cidade\n'
              '2 - Cadastrar conexão\n'
              '3 - Listar cidades\n'
              '4 - Listar conexões\n'
              '5 - Listar cidades vizinhas\n')

        while True:

            try:

                escolha_usuario = int(input(f'Digite a opção desejada: '))

                match escolha_usuario:

                    case 1:
                        self.cadastrar_cidade()

                    case 2:
                        self.cadastrar_conexao()

                    case 3:
                        self.info_cidades()

                    case 4:
                        self.info_conexoes()

                    case 5:
                        self.info_vizinhos()

            except ValueError:
                print('\nEntrada inválida, digite apenas números.\n')


class Vertice:

    def __init__(self, nome_cidade):
        self.nome_cidade = nome_cidade


class Aresta:

    def __init__(self, cidade1, cidade2, distancia):
        self.cidade1 = cidade1
        self.cidade2 = cidade2
        self.distancia = distancia

    def __eq__(self, other):
        if not isinstance(other, Aresta):
            return False
        return (self.cidade1 == other.cidade1 and
                self.cidade2 == other.cidade2 and
                self.distancia == other.distancia)


if __name__ == '__main__':

    grafo = Grafos()
    cidades = grafo.cidades
    conexoes = grafo.conexoes
    d_c = grafo.conexoes_especificas
    d_v = grafo.vizinhanca

    with open("Banco_de_grafos.csv", "r", encoding="utf-8") as arquivo:

        linha = arquivo.readline().strip()

        while linha:

            linha_editada = [index.strip() for index in linha.split(",")]

            linha_editada[2] = linha_editada[2].replace("Km", "")
            linha_editada[2] = float(linha_editada[2])

            ###CONEXÕES RECEBE A LISTA
            conexoes.append(Aresta(linha_editada[0], linha_editada[1], linha_editada[2]))

            ### CIDADES RECEBE A LISTA

            if linha_editada[0].lower() not in [cidades.nome_cidade.lower() for cidades in grafo.cidades]:
                grafo.cidades.append(Vertice(linha_editada[0]))

            if linha_editada[1].lower() not in [cidades.nome_cidade.lower() for cidades in grafo.cidades]:
                grafo.cidades.append(Vertice(linha_editada[1]))

            ### CONEXÕES ESPECÍFICAS RECEBE A LISTA:

            nova_aresta1 = Aresta(linha_editada[0], linha_editada[1], linha_editada[2])
            nova_aresta2 = Aresta(linha_editada[1], linha_editada[0], linha_editada[2])

            if not d_c:
                d_c[linha_editada[0].lower()] = [nova_aresta1]
                d_c[linha_editada[1].lower()] = [nova_aresta2]

            else:
                if linha_editada[0].lower() not in d_c:
                    d_c[linha_editada[0].lower()] = [nova_aresta1]
                else:
                    if nova_aresta1 not in d_c[linha_editada[0].lower()]:
                        d_c[linha_editada[0].lower()].append(nova_aresta1)

                if linha_editada[1].lower() not in d_c:
                    d_c[linha_editada[1].lower()] = [nova_aresta2]
                else:
                    if nova_aresta2 not in d_c[linha_editada[1].lower()]:
                        d_c[linha_editada[1].lower()].append(nova_aresta2)

                ### CIDADES VIZINHAS RECEBEM A LISTA:

                cidade1 = linha_editada[0]
                cidade2 = linha_editada[1]

                if not d_v:
                    d_v[cidade1.lower()] = [cidade2]
                    d_v[cidade2.lower()] = [cidade1]
                else:
                    if cidade1.lower() not in d_v:
                        d_v[cidade1.lower()] = [cidade2]
                    else:
                        if cidade2 not in d_v[cidade1.lower()]:
                            d_v[cidade1.lower()].append(cidade2)

                    if cidade2.lower() not in d_v:
                        d_v[cidade2.lower()] = [cidade1]
                    else:
                        if cidade1 not in d_v[cidade2.lower()]:
                            d_v[cidade2.lower()].append(cidade1)

            linha = arquivo.readline().strip()

    grafo.menu()
