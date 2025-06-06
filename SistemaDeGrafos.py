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
        self.conexos = []

    def Linha(self):
        print(34*"*")

    def Menu(self):
        Grafos.Linha(self)
        print(f'BEM-VINDO ao meu sistema de Grafos\n')
        print(f'Digite a opção desejada:\n')
        print('1 - Cadastrar cidade')
        print('2 - Cadastrar conexão')
        print('3 - Listar cidades')
        print('4 - Listar conexões')
        print('5 - Listar cidades vizinhas\n')

    def CadastrarCidade(self):
        pass

    def CadastrarConexao(self):
        pass

    def infoCidades(self): # 3 - Listar Cidades
        pass

    def infoConexoes(self): # 4 - Listas conexões
        pass


class Vertices:

    def __init__(self):

        self.nome_cidade = None
        self.vizinhanca = []
        self.conexoes = []


    def infoVizinhos(self): pass

    def infoConexoes(self): pass

    def infoVertice(self): pass


class Arestas:

    def __init__(self):
        self.cidade1 = self.nome_cidade
        self.cidade2 = self.nome_cidade
        self.distancia = None

    def infoAresta(self): pass




if __name__ == '__main__':
    Grafos().Menu()