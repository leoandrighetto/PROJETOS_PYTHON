class Grafos:

    def __init__(self):
        self.cidades = []   #Lista de TODAS as cidades
        self.conexoes = []  #Lista de TODAS as Arestas

    def cadastrar_cidade(self): #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        print('\n*** Cadastro de cidades ***\n')

        while True:

            nome_cidade = input('Digite o nome da cidade: \n')

            self.cidades.append(Vertice(nome_cidade))               #Objeto vai para a Lista de Cidades (Vertices)

            while True:
                pergunta_usuario = input('Deseja cadastrar mais cidades (s/n) ? \n')

                if pergunta_usuario.lower() == "s":
                    break

                elif pergunta_usuario.lower() == "n":
                    self.menu()
                else:
                    print('\nentrada invalida\n')

    def cadastrar_conexao(self):
        print('\n*** Cadastro de conexão ***\n')

        while True:

            cidade1 = input('Digite o nome da cidade 1: \n')
            cidade2 = input('Digite o nome da cidade 2: \n')
            distancia = float(input('Digite a distância entre as cidades (ex: 200.1): \n'))

            nova_aresta1 = Aresta(cidade1,cidade2,distancia)
            nova_aresta2 = Aresta(cidade2, cidade1, distancia)

            self.conexoes.append(nova_aresta1) # Objeto vai para a Lista de Conexões (Aresta)

                                 ###    CADASTRO CIDADE:
            lista_cidades = [cidades.nome_cidade.lower() for cidades in self.cidades]

            if cidade1.lower() not in lista_cidades:
                self.cidades.append(Vertice(cidade1))

            if cidade2.lower() not in lista_cidades:
                self.cidades.append(Vertice(cidade2))

                        ###     CONEXÕES ESPECÍFICAS:

            d_c = Vertice.conexoes_especificas  #Dicionario de Conexoes (d_c)

            if not d_c:
                d_c[cidade1] = [nova_aresta1]
                d_c[cidade2] = [nova_aresta2]

            else:
                if cidade1 not in d_c:
                    d_c[cidade1] = [nova_aresta1]

                else:
                    if nova_aresta1 not in d_c[cidade1]:
                        d_c[cidade1].append(nova_aresta1)
                    else:
                        print('Conexão já existe\n')

                if cidade2 not in d_c:
                    d_c[cidade2] = [nova_aresta2]

                else:
                    if nova_aresta2 not in d_c[cidade2]:
                        d_c[cidade2].append(nova_aresta2)
                    else:
                        print('Conexão já existe\n')

                                ###     CIDADES VIZINHAS:

            d_v = Vertice.vizinhanca

            if not d_v:
                d_v[cidade1] = [cidade2]
                d_v[cidade2] = [cidade1]

            else:
                if cidade1 not in d_v:
                    d_v[cidade1] = [cidade2]

                else:
                    if cidade2 not in d_v[cidade1]:
                        d_v[cidade1].append(cidade2)

                if cidade2 not in d_v:
                    d_v[cidade2] = [cidade1]

                else:
                    if cidade1 not in d_v[cidade2]:
                        d_v[cidade2].append(cidade1)

            while True:
                per = input("deseja cadastrar mais conexões (s/n) ? \n")

                if per.lower() == "s":
                    break

                elif per.lower() == "n":
                    self.menu()
                    break
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
                  f'Distância: {i.distancia}Km\n\n')

        self.menu()

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
                        Vertice(None).info_vizinhos()

            except ValueError:
                print('\nEntrada inválida, digite apenas números.\n')

class Vertice:

    conexoes_especificas = {}
    vizinhanca = {}

    def __init__(self,nome_cidade,grafo=None):
        self.nome_cidade = nome_cidade
        self.grafo = grafo


    def info_vizinhos(self):

        while True:
            c_e = input('Digite o nome da cidade: \n')

            lista = self.vizinhanca

            if c_e.lower() in lista:
                distancias_vizinhos = [aresta.distancia for aresta in self.conexoes_especificas[c_e.lower()]]
                menor_distancias = sorted(distancias_vizinhos)

                for distancia in menor_distancias:

                    for arestas in self.conexoes_especificas[c_e.lower()]:
                        if arestas.distancia == distancia:
                            print(f'\n{arestas.cidade2} ->> {distancia} Km de distância\n')


                while True:
                    per = input('Gostaria de buscar novamente(s/n)? ')
                    if per.lower() == 's':
                        break
                    else:
                        Grafos().menu()

            else:
                print('cidade não encontrada\n')
                while True:
                    per = input('Gostaria de buscar novamente (s/n)? ')
                    if per.lower() == 's':
                        break
                    else:
                        Grafos().menu()


class Aresta:

    def __init__(self, cidade1, cidade2, distancia):
        self.cidade1 = cidade1
        self.cidade2 = cidade2
        self.distancia = distancia


if __name__ == '__main__':

    # grafo = Grafos()
    #
    # with open ("Banco_de_grafos.csv", "r", encoding="utf-8") as arquivo:
    #
    #     linha = arquivo.readline().replace('\n','')
    #     linha = linha.strip()
    #
    #     for linha in arquivo:
    #
    #         linha = linha.strip()
    #
    #         # partes = []
    #         # for p in linha.split(","):
    #         #     partes.append(p.strip())
    #
    #         partes = [i.strip() for i in linha.split(',')]
    #
    #         # distancia = partes[2].split("Km")
    #
    #         cidade1 = partes[0]
    #         cidade2 = partes[1]
    #         # distancia = float(partes[2])
    #
    #         distancia = float(partes[2].replace("km","").strip())
    #
    #
    #         grafo.conexoes.append(Aresta(cidade1,cidade2,distancia))
    #
    #         for i in grafo.cidades:
    #             if cidade1 not in i:
    #                 grafo.cidade.append(cidade1)
    #             if cidade2 not in i:
    #                 grafo.cidade.append(cidade2)
    #
    #     linha = "   Porto Alegre, Pelotas, 291.3km\n"
    #     linha_limpa = linha.strip()
    #
    #     print(repr(linha))  # '   Porto Alegre, Pelotas, 291.3km\n'
    #     print(repr(linha_limpa))  # 'Porto Alegre, Pelotas, 291.3km'

    Grafos().menu()
