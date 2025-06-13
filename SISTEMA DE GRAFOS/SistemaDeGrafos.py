class Grafos:

    def __init__(self):
        self.cidades = []   #Lista de TODAS as cidades
        self.conexoes = []  #Lista de TODAS as Arestas

    def cadastrar_cidade(self): #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

        print('\n*** Cadastro de cidades ***\n')

        while True:

            nome_cidade = input('Digite o nome da cidade: \n')

            self.cidades.append(Vertice(nome_cidade))               #Objeto vai para a Lista de Cidades (Vertices)

            pergunta_usuario = input('Deseja cadastrar mais cidades (s/n) ? \n')

            while True:
                if pergunta_usuario.lower() == "s":
                    break

                else:
                    for cidade in self.cidades:
                        print(f'>>>>>{nome_cidade}')
                    self.menu()

    def cadastrar_conexao(self):
        print('\n*** Cadastro de conexão ***\n')


        while True:

            cidade_1 = input('Digite o nome da cidade 1: \n')
            cidade_2 = input('Digite o nome da cidade 2: \n')
            distancia = float(input('Digite a distância entre as cidades (ex: 219.8): \n'))

            self.conexoes.append(Aresta(cidade_1,cidade_2,distancia)) # Objeto vai para a Lista de Conexões (Aresta)

            '''
            Implementar inserção automatica Conexões específicas e cidades vizinhas.
            '''

            pergunta_usuario = input('Deseja cadastrar mais conexões (s/n)? \n')

            while True:
                if pergunta_usuario.lower() == "s":
                    break

                else:
                    for conexao in self.conexoes:
                        self.menu()

    def info_cidades(self):  # 3 - Listar Cidades
        print("\nLista de Cidades:\n")

        cidades_ordenadas = sorted(self.cidades, key=lambda cidade: cidade.nome_cidade)

        for i in cidades_ordenadas:
            print(f'{i.nome_cidade}\n')

        self.menu() #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    def info_conexoes(self):  # 4 - Listas conexões - Lista TODAS as Arestas
        pass

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

    def __init__(self,nome_cidade):
        self.nome_cidade = nome_cidade
        self.vizinhanca = []    #Lista Vazia, para armazenar cidades conectadas a uma cidade específica

        '''self.vizinhos = {
    "Pelotas": ["Canoas", "Porto Alegre"],
    "Porto Alegre": ["Canoas", "Pelotas"],
    "Canoas": ["Pelotas", "Porto Alegre"]
}'''

         #Lista CONEXÕES de uma cidade específica

    def info_vizinhos(self):

        cidade_escolhida = input('Digite o nome da cidade: \n')


    def info_conexoes(self):
        return self.conexoes

    def info_vertice(self):
        return self.nome_cidade

class Aresta:

    def __init__(self, cidade1, cidade2, distancia):
        self.cidade1 = cidade1
        self.cidade2 = cidade2
        self.distancia = distancia

    def info_aresta(self):
        return (f'Cidade 1: {self.cidade1}\n'
                f'Cidade 2: {self.cidade2}\n'
                f'Distância: {self.distancia}\n')



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
