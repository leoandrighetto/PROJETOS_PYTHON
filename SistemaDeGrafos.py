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

    def cadastrar_cidade(self):

        print('\n*** Cadastro de cidades ***\n')

        while True:

            nome_cidade = input('Digite o nome da cidade: \n')

            self.cidades.append(Vertice(nome_cidade))               #Objeto vai para a Lista de Cidades (Vertices)

            pergunta_usuario = input('Deseja cadastrar mais cidades (s/n) ? \n')

            while True:
                if pergunta_usuario.lower() == "s":
                    break

                else:
                    self.menu()

    def cadastrar_conexao(self):
        print('\n*** Cadastro de conexão ***\n')


        while True:

            cidade_1 = input('Digite o nome da cidade 1: \n')
            cidade_2 = input('Digite o nome da cidade 2: \n')
            distancia = float(input('Digite a distância entre as cidades (ex: 219.8): \n'))

            self.conexoes.append(Arestas(cidade_1,cidade_2,distancia)) # Objeto vai para a Lista de Conexões (Aresta)

            pergunta_usuario = input('Deseja cadastrar mais conexões (s/n)? \n')

            while True:
                if pergunta_usuario.lower() == "s":
                    break

                else:
                    self.menu()

    def info_cidades(self):  # 3 - Listar Cidades
        print("\nLista de Cidades:\n")

        for i in self.cidades:
            print(i.info_vertice())
            print()


        self.menu()

    def info_conexoes(self):  # 4 - Listas conexões
        pass


class Vertice:

    def __init__(self,nome_cidade):
        self.nome_cidade = nome_cidade
        self.vizinhanca = []
        self.conexoes = []

    def info_vizinhos(self): pass

    def info_conexoes(self): pass

    def info_vertice(self):
        return self.nome_cidade

class Arestas:

    def __init__(self, cidade1, cidade2, distancia):
        self.cidade1 = cidade1
        self.cidade2 = cidade2
        self.distancia = distancia

    def info_aresta(self):
        return (f'Cidade 1: {self.cidade1}\n'
                f'Cidade 2: {self.cidade2}\n'
                f'Distância: {self.distancia}\n')


if __name__ == '__main__':
    Grafos().menu()
