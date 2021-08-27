from bibgrafo.aresta import Aresta
from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_exceptions import *
from collections import defaultdict
from copy import deepcopy
from itertools import combinations

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
        :param node: Vértice atual
        :param edges: Lista que guarda uma tupla, com o vértice não visitado, seu vizinho e a aresta que incide sobre ambos
        '''
        visited.append(node)
        for neighbor in adj_list[node]:
            if neighbor not in visited:
                set_1, set_2 = set(adj_dict[node]), set(adj_dict[neighbor])
                intersection = sorted(list(set_1.intersection(set_2)))[0]
                edges.append((node, neighbor, intersection))
                self.DFS_util(adj_list, visited, adj_dict,neighbor, edges)

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
        
        dfs = MeuGrafo(visited)
        for v1, v2, e in edges:
            dfs.adicionaAresta(e, v1, v2)
        return dfs

    def conexo(self):
        """
        Responde se um grafo é conexo ou não
        :return: Um valor booleano que indica se o grafo é conexo
        """
        vertices = deepcopy(self.N)
        dfs = self.DFS(vertices[0])
        qt_vert_dfs = len(dfs.N)
        qt_vert_grafo = len(vertices)
        return qt_vert_dfs == qt_vert_grafo

    def caminho_dois_vertices_dfs(self, u, d, visited, path, possible_paths, adj_list):
        """
        Armazena todos os caminhos entre dois vértices
        :param u: Vértice atual
        :param d: Vértice que queremos chegar
        :param visited: Dicionário no formato -> vértice (chave): Valor booleano que indica se esse vértice já foi visitado (valor)
        :param path: Lista com um caminhos entre dois vértices
        :param possible_paths: Lista com a lista dos possíveis caminhos entre dois vértices
        :param adj_list: Lista de adjacência 
        """
        visited[u] = True
        path.append(u)
        if u == d:
            possible_paths.append(path.copy())
        else:
            for i in adj_list[u]:
                if visited[i] == False:
                    self.caminho_dois_vertices_dfs(i, d, visited, path, possible_paths, adj_list)
        path.pop()
        visited[u] = False

    def caminho_dois_vertices(self, source, target, adj_list):
        """
        Busca todos os caminhos existentes entre dois vértices
        :param source: Vértice inicial
        :param target: Vértice final
        :param adj_list: Lista de adjacência
        :return: Lista contendo as listas dos possíveis caminhos
        """
        visited = {i: False for i in self.N}
        path = []
        possible_path = []
        self.caminho_dois_vertices_dfs(source, target, visited, path, possible_path, adj_list)
        return possible_path

    def caminho(self, n):
        """
        Busca um caminho de tamanho n em um grafo
        :param n: Tamanho do caminho que será buscado
        :return: Se houver um caminho com o tamanho solicitado é retornado esse caminho. Senão, é retornado um valor booleano
        """
        vertices = deepcopy(self.N)
        comb_vertices = list(combinations(vertices, 2))
        adj_list = self.make_ajd_list()
        aresta_v = {i: self.arestas_sobre_vertice(i) for i in self.N}
        for v1, v2 in comb_vertices:
            path_lenght = 0
            all_paths = self.caminho_dois_vertices(v1, v2, adj_list)
            for path in all_paths:
                path_n = []
                path_lenght = 0
                for p in range(len(path) - 1):
                    va, vb = path[p], path[p + 1]
                    aresta_sobre_va = aresta_v[va]
                    aresta_sobre_vb = aresta_v[vb]
                    aresta_liga = sorted(list(set(aresta_sobre_va).intersection(set(aresta_sobre_vb))))[0]
                    if p == 0:
                        path_n.append(va)
                    path_n.append(aresta_liga)
                    path_lenght += 1
                    path_n.append(vb)
                if path_lenght == n:
                    break
            if path_lenght == n:
                break
        if path_lenght == n:
            return path_n
        return False

    def ha_ciclo_dfs(self, v, visited, parent, adj_list, path):
        """
        Percorre o grafo buscando um ciclo
        :param v: Vértice atual
        :param visited: Dicionário com chaves sendo os vértices do grafo e valor sendo um valor booleano
        :param parent: Lista com com os vértices visitados
        :param adj_list: Lista de adjacência
        :param path: Lista com vértices que pertecem ao ciclo
        """
        visited[v] = True
        for i in adj_list[v]:
            if visited[i] == False:
                if self.ha_ciclo_dfs(i, visited, v, adj_list, path):
                    path.append(i)
                    return True
            elif parent != i:
                path.append(i)
                return True
        return False

    def ha_ciclo(self):
        """
        Busca um ciclo em grafo
        :return: Se houver um ciclo, ele será retornado. Caso contrário, é retornado um valor booleano
        """
        adj_list = self.make_ajd_list()
        visited = {i: False for i in adj_list.keys()}
        achou_ciclo = False
        caminho_vertices = []
        for n in adj_list.keys():
            if visited[n] == False:
                if (self.ha_ciclo_dfs(n, visited, -1, adj_list, caminho_vertices)) == True:
                    achou_ciclo = True
                    break
        if achou_ciclo:
            path = []
            caminho_limpo = []
            v_inicio = caminho_vertices[0]
            count = 0
            for k in caminho_vertices:
                if k == v_inicio:
                    count += 1
                    caminho_limpo.append(k)
                    if count == 2:
                        break
                else:
                    caminho_limpo.append(k)
            adj_a = {i: self.arestas_sobre_vertice(i) for i in self.N}
            if caminho_limpo[0] != caminho_limpo[-1]:
                caminho_limpo.append(caminho_limpo[0])
            for a in range(len(caminho_limpo) - 1):
                v1, v2 = caminho_limpo[a], caminho_limpo[a + 1]
                aresta_sobre_v1 = adj_a[v1]
                aresta_sobre_v2 = adj_a[v2]
                aresta_adj = sorted(list(set(aresta_sobre_v1).intersection(set(aresta_sobre_v2))))
                if a == 0:
                    path.append(v1)
                path.append(aresta_adj[0])
                path.append(v2)
            return path
        return False
        