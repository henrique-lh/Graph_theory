from bibgrafo.aresta import Aresta
from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_exceptions import *
from collections import defaultdict

class MeuGrafo(GrafoListaAdjacencia):

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''
        permutations = []
        for n1 in self.N:
            for n2 in self.N:
                if n1 != n2:
                    v = n1 + "-" + n2
                    if v not in permutations and v[::-1] not in permutations:
                        permutations.append(v)
        for a in self.A:
            v = self.A[a].getV1() + "-" + self.A[a].getV2()
            if v in permutations:
                permutations.remove(v)
            elif v[::-1] in permutations:
                permutations.remove(v[::-1])
        return permutations
                
    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for a in self.A:
            if self.A[a].getV1() == self.A[a].getV2():
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
            raise VerticeInvalidoException
        grau = 0
        for a in self.A:
            if self.A[a].getV1() == V or self.A[a].getV2() == V:
                if self.A[a].getV1() == self.A[a].getV2() == V:
                    grau += 2
                else:
                    grau += 1
        return grau

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        edges = []
        for a in self.A:
            v = self.A[a].getV1() + self.A[a].getV2()
            if v in edges or v[::-1] in edges:
                return True
            else:
                edges.append(v)
        return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if V not in self.N:
            raise VerticeInvalidoException
        contem_no = []
        for a in self.A:
            if self.A[a].getV1() == V or self.A[a].getV2() == V:
                contem_no.append(a)
        return contem_no

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

    def make_ajd_list(self):
        '''
        Fornecee uma lista de adjacência a partir do dicionário de arestas
        :return: Uma lista com as adjacências de cada vértice
        '''
        adj_list = defaultdict(list)
        for n in self.N:
            edges = self.arestas_sobre_vertice(n)
            for e in edges:
                v = self.A[e].getV1() if self.A[e].getV1() != n else self.A[e].getV2()
                if v not in adj_list[n]:
                    adj_list[n].append(v)
        return adj_list
        
    def BFS(self, V=""):
        '''
        Executa a busca em largura em um grafo a partir de um nó dado
        :param V: Vértice por onde inicia a busca
        :return: Retorna um grafo com o caminho percorrido na busca
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if V not in self.N:
            raise VerticeInvalidoException
        queue = [V]
        visited = [V]
        adj_list = self.make_ajd_list()
        adj_dict = {i: self.arestas_sobre_vertice(i) for i in self.N}
        path = []
        while queue:
            v = queue.pop(0)
            for neighbor in adj_list[v]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)
                    set_1, set_2 = set(adj_dict[v]), set(adj_dict[neighbor])
                    intersection = sorted(list(set_1.intersection(set_2)))[0]
                    path.append((v, neighbor, intersection))
        bfs = MeuGrafo(list(visited))
        for v1, v2, e in path:
            bfs.adicionaAresta(e, v1, v2)
        return bfs

    def DFS_util(self, adj_list, visited, adj_dict,node, edges):
        '''
        Executa a busca em profundidade em um grafo a partir de um nó dado
        :param adj_list: Lista de adjacências
        :param visited: Lista com nós que já foram visitados
        :param adj_dict: Dicionário de aresta
        :param node: Vértice por onde inicia a busca
        :param edges: Lista que guarda uma tupla, com o vértice não visitado, seu vizinho e a aresta que incide sobre ambos
        :return visited: Lista com nós que já foram visitados
        :return edges: Lista com tuplas guardando vértices vizinhos e arestas incidentes
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        visited.append(node)
        for neighbor in adj_list[node]:
            if neighbor not in visited:
                set_1, set_2 = set(adj_dict[node]), set(adj_dict[neighbor])
                intersection = sorted(list(set_1.intersection(set_2)))[0]
                edges.append((node, neighbor, intersection))
                self.DFS_util(adj_list, visited, adj_dict,neighbor, edges)
        return visited, edges

    def DFS(self, V=""):
        '''
        Fornece parâmetros necessários para execução do algoritmo DFS
        :param V: O vértice de onde inicia a busca
        :return: Retorna um grafo com o caminho percorrido na busca
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        if V not in self.N:
            raise VerticeInvalidoException
        adj_list = self.make_ajd_list()
        adj_dict = {i: self.arestas_sobre_vertice(i) for i in self.N}
        visited = list()
        edges = list()
        self.DFS_util(adj_list, visited, adj_dict,V, edges)
        
        dfs = MeuGrafo(list(visited))
        for v1, v2, e in edges:
            dfs.adicionaAresta(e, v1, v2)
        return dfs

        