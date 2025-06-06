''''Para este trabalho deve ser construido um programa cuja funcionalidade principal é construir um grafo.
O programa deve ter uma interface com as seguintes opções:

Cadastrar cidade - instancia um objeto do tipo Vertice
Cadastra conexão - instancia um objeto do tipo Aresta

Listar cidades - lista todos os vertices do grafo
    * Deve aparecer em ordem alfabética.

Listar conexões - lista todas as arestas do grafo
    * Deve ser informada a distancia entre as cidades da conexão.

Listar cidades vizinhas - lista todas as cidades conectadas à uma cidade específica
    * Também deve ser informada a distancia entre a cidade e suas cidades vizinhas
    * Deve ser ordenada pela menor distancia

A entrada de dados deve ser feita por interface e também por um arquivo csv unico contendo dados no seguinte formato:

<nome da cidade1>,  <nome da cidade 2>, <distancia entre as cidades em km>
Porto Alegre, Pelotas, 291.3km
'''


class Grafos:

    def __init__(self):
        self.cidades = []
        self.conexoes = []

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
                        Grafos().cadastrar_cidade()

                    case 2:
                        Grafos().cadastrar_conexao()

                    case 3:
                        Grafos().info_cidades()

                    case 4:
                        Grafos().info_conexoes()

                    case 5:
                        Vertices().info_vizinhos()

            except ValueError:
                print('\nEntrada inválida, digite apenas números.\n')

    def cadastrar_cidade(self):
        print('\n*** Cadastro de cidades ***\n')

        while True:

            nome_cidade = input('Digite o nome da cidade: \n')
            self.cidades.append(nome_cidade)

            pergunta_usuario = input('Deseja cadastrar mais cidades (s/n) ? \n')

            while True:
                if pergunta_usuario.lower() == "s":
                    break

                else:
                    Grafos().menu()

    def cadastrar_conexao(self):
        pass

    def info_cidades(self):  # 3 - Listar Cidades
        pass

    def info_conexoes(self):  # 4 - Listas conexões
        pass


class Vertices:

    def __init__(self,nome_cidade,vizinhanca,conexoes):
        self.nome_cidade = None
        self.vizinhanca = []
        self.conexoes = conexoes

    def info_vizinhos(self): pass

    def info_conexoes(self): pass

    def info_vertice(self): pass


class Arestas:

    def __init__(self, cidade1, cidade2, distancia=0):
        self.cidade1 = cidade1
        self.cidade2 = cidade2
        self.distancia = distancia

    def info_aresta(self): pass


if __name__ == '__main__':
    Grafos().menu()
