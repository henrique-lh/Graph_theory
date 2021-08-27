from bibgrafo.grafo_matriz_adj_nao_dir import GrafoMatrizAdjacenciaNaoDirecionado
from bibgrafo.grafo_exceptions import *


class MeuGrafo(GrafoMatrizAdjacenciaNaoDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''
        lista_nao_adj = []
        for i in range(len(self.M)):
            v1 = str(self.N[i])
            for j in range(i, len(self.M)):
                if i != j and len(self.M[i][j]) == 0:                
                    v2 = str(self.N[j])
                    f = v1 + "-" + v2
                    if f not in lista_nao_adj and f[::-1] not in lista_nao_adj:
                        lista_nao_adj.append(f)
        return lista_nao_adj

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for i in range(len(self.M)):
            if len(self.M[i][i]) > 0:
                return True
        return False


    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if V not in self.N:
            raise VerticeInvalidoException()
        i_v = self.N.index(V)
        grau = 0
        for i in range(i_v, len(self.M)):
            if i_v == i:
                grau += len(self.M[i_v][i]) * 2
            else:
                grau += len(self.M[i_v][i])
        
        for j in range(i_v):
            grau += len(self.M[j][i_v])
        return grau

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        for i in range(len(self.M)):
            for j in range(len(self.M)):
                valor = self.M[i][j]
                if len(valor) > 1:
                    return True
        return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if V not in self.N:
            raise VerticeInvalidoException()
        i_v = self.N.index(V)
        arestas_incidentes = []
        for j in range(i_v, len(self.M)):
            if self.M[i_v][j]:
                for a in self.M[i_v][j]:
                    arestas_incidentes.append(a)
        for j in range(i_v):
            if self.M[j][i_v]:
                for a in self.M[j][i_v]:
                    arestas_incidentes.append(a)
        return arestas_incidentes
        

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        if self.ha_laco():
            return False
        if self.ha_paralelas():
            return False
        all_graus = []
        for n in self.N:
            grau_n = self.grau(n)
            if all_graus:
                if grau_n != all_graus[0]:
                    return False
            else:
                all_graus.append(grau_n)
        return True

