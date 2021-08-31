from __future__ import annotations
from bibgrafo.aresta import Aresta
from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_exceptions import *
from collections import defaultdict, deque
from itertools import combinations
from typing import Dict, List, Union, Tuple
from copy import deepcopy

class MeuGrafo(GrafoListaAdjacencia):

    def vertices_nao_adjacentes(self) -> List[int]:
        '''Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...].
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.

        Returns:
            vertex_combinations(list)
        '''
        vertex_combinations = list(map(lambda x: x[0] + "-" + x[1], combinations(self.N, 2)))
        
        for a in self.A:
            v = self.A[a].getV1() + "-" + self.A[a].getV2()
            if v in vertex_combinations:
                vertex_combinations.remove(v)
            elif v[::-1] in vertex_combinations:
                vertex_combinations.remove(v[::-1])
        return vertex_combinations
                
    def ha_laco(self) -> bool:
        '''Verifica se existe algum laço no grafo.

        Returns:
            bool
        '''
        for a in self.A:
            if self.A[a].getV1() == self.A[a].getV2():
                return True
        return False

    def grau(self, V: str = '') -> int:
        '''Provê o grau do vértice passado como parâmetro.

        Args:
            V (str, optional): O rótulo do vértice a ser analisado.
        
        Returns:
            grau(int)
        
        Raises:
            VerticeInvalidoException: Erro caso não existe o vértice no grafo.
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

    def ha_paralelas(self) -> bool:
        ''' Verifica se há arestas paralelas no grafo

        Returns:
            bool
        '''
        edges = []
        for a in self.A:
            v = self.A[a].getV1() + self.A[a].getV2()
            if v in edges or v[::-1] in edges:
                return True
            else:
                edges.append(v)
        return False
            
    def arestas_sobre_vertice(self, V: str) -> List[str]:
        '''Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro

        Args:
            V (str): O vértice a ser analisado
        
        Returns:
            contem_no(list)

        Raises:
            VerticeInvalidoException: Erro caso não existe o vértice no grafo.
        '''
        if V not in self.N:
            raise VerticeInvalidoException
        contem_no = []
        for a in self.A:
            if self.A[a].getV1() == V or self.A[a].getV2() == V:
                contem_no.append(a)
        return contem_no

    def eh_completo(self) -> bool:
        '''Verifica se o grafo é completo.

        Returns: 
            bool
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

    def make_ajd_list(self) -> defaultdict[List]:
        '''Fornecee uma lista de adjacência a partir do dicionário de arestas

        Returns:
            adj_list(defaultdict[List])
        '''
        adj_list = defaultdict(list)
        for n in self.N:
            edges = self.arestas_sobre_vertice(n)
            for e in edges:
                v = self.A[e].getV1() if self.A[e].getV1() != n else self.A[e].getV2()
                adj_list[n].append(v)
        return adj_list
        
    def BFS(self, V: str = "") -> MeuGrafo:
        '''Executa a busca em largura em um grafo a partir de um nó dado

        Args:
            V(str, optional): Vértice por onde inicia a busca

        Returns:
            bsf(MeuGrafo): Um novo grafo com o caminho BFS

        Raises:
            VerticeInvalidoException: Erro caso não existe o vértice no grafo.
        '''
        if V not in self.N:
            raise VerticeInvalidoException
        queue = deque([V])
        visited = dict.fromkeys([V])
        adj_list = self.make_ajd_list()
        adj_dict = {i: self.arestas_sobre_vertice(i) for i in self.N}
        path = []
        while queue:
            v = queue.popleft()
            for neighbor in adj_list[v]:
                if neighbor not in visited:
                    visited[neighbor] = None
                    queue.append(neighbor)
                    set_1, set_2 = set(adj_dict[v]), set(adj_dict[neighbor])
                    intersection = sorted(list(set_1.intersection(set_2)))[0]
                    path.append((v, neighbor, intersection))
        bfs = MeuGrafo(list(visited.keys()))
        for v1, v2, e in path:
            bfs.adicionaAresta(e, v1, v2)
        return bfs

    def DFS_util(self, adj_list: defaultdict[List], visited: List, adj_dict: Dict, node: str, edges: List) -> None:
        '''Executa a busca em profundidade em um grafo a partir de um nó dado

        Args:
            adj_list(defaultdict[List]): Lista de adjacências
            visited(List): Lista com nós que já foram visitados
            adj_dict(Dict): Dicionário de aresta
            node(str): Vértice por onde inicia a busca
            edges(List): Lista que guarda uma tupla, com o vértice não visitado, seu vizinho e a aresta que incide sobre ambos
        '''
        visited.append(node)
        for neighbor in adj_list[node]:
            if neighbor not in visited:
                set_1, set_2 = set(adj_dict[node]), set(adj_dict[neighbor])
                intersection = sorted(list(set_1.intersection(set_2)))[0]
                edges.append((node, neighbor, intersection))
                self.DFS_util(adj_list, visited, adj_dict,neighbor, edges)

    def DFS(self, V: str = "") -> MeuGrafo:
        '''
        Fornece parâmetros necessários para execução do algoritmo DFS

        Args:
            V(str, optional): O vértice de onde inicia a busca

        Returns:
            dfs(MeuGrafo): Um novo grafo com o caminho percorrido na DFS

        Raises:
            VerticeInvalidoException: Erro caso não existe o vértice no grafo.
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

    def conexo(self):
        """Responde se um grafo é conexo ou não

        Returns:
            bool
        """
        vertices = deepcopy(self.N)
        dfs = self.DFS(vertices[0])
        qt_vert_dfs = len(dfs.N)
        qt_vert_grafo = len(vertices)
        return qt_vert_dfs == qt_vert_grafo

    def caminho_dois_vertices_dfs(self, u: str, d: str, visited: Dict, path: List, possible_paths: List[List], adj_list: defaultdict[List]) -> None:
        """Armazena todos os caminhos entre dois vértices

        Args:
            u(str): Vértice atual
            d(str): Vértice que queremos chegar
            visited(Dict): Dicionário no formato -> vértice (chave): Valor booleano que indica se esse vértice já foi visitado (valor)
            path(List): Lista com um caminhos entre dois vértices
            possible_paths(List[List]): Lista com a lista dos possíveis caminhos entre dois vértices
            adj_list(default[List]): Lista de adjacência 
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

    def caminho_dois_vertices(self, source: str, target: str, adj_list: defaultdict[List]) -> List:
        """Busca todos os caminhos existentes entre dois vértices

        Args:
            source(str): Vértice inicial
            target(str): Vértice final
            adj_list(str): Lista de adjacência
        
        Returns:
            possible_path(List): Lista contendo as listas dos possíveis caminhos
        """
        visited = {i: False for i in self.N}
        path = []
        possible_path = []
        self.caminho_dois_vertices_dfs(source, target, visited, path, possible_path, adj_list)
        return possible_path

    def caminho(self, n: int) -> Union[List, bool]:
        """Busca um caminho de tamanho n em um grafo

        Args:
            n(int): Tamanho do caminho que será buscado

        Returns:
            path(List) | bool: Caminho com o tamanho solicitado | False
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

    def ha_ciclo_dfs(self, v: str, visited: Dict, parent: Union[int, str], adj_list: defaultdict[List], path: List) -> bool:
        """Percorre o grafo buscando um ciclo

        Args:
            v: Vértice atual
            visited: Dicionário com chaves sendo os vértices do grafo e valor sendo um valor booleano
            parent: Vértice pai
            adj_list: Lista de adjacência
            path: Lista com vértices que pertecem ao ciclo

        Returns: 
            bool
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

    def ha_ciclo(self) -> Union[List, bool]:
        """Busca um ciclo em grafo

        Returns:
            path(List) | bool
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

    def add_edge(self, v: str, u: str, adj_list: defaultdict[List]) -> None:
        """Adiciona um vértice a lista de adjacências

        Args:
            v(str): Vértice que será adicionado
            u(str): Vértice que será adicionado
            adj_list(defaultdict[List]): lista de adjacências
        """
        adj_list[v].append(u)
        adj_list[u].append(v)

    def remove_edge(self, v: str, u: str, adj_list: defaultdict[List]):
        """Remove um vértice de uma lista de adjacência

        Args:
            v(str): Vértice que será adicionado
            u(str): Vértice que será adicionado
            adj_list(defaultdict[List]): lista de adjacências
        """
        for i in range(len(adj_list[v])):
            if adj_list[v][i] == u:
                adj_list[v][i], adj_list[v][len(adj_list[v]) - 1] = adj_list[v][len(adj_list[v]) - 1], adj_list[v][i]
                adj_list[v].pop()
                break

        for i in range(len(adj_list[u])):
            if adj_list[u][i] == v:
                adj_list[u][i], adj_list[u][len(adj_list[u]) - 1] = adj_list[u][len(adj_list[u]) - 1], adj_list[u][i]
                adj_list[u].pop()
                break

    def count_connected_vertecies(self, u: str, visited: Dict, adj_list: defaultdict[List]) -> int:
        """Conta a quantidade de vértices que estão conectados em um vértice inicial

        Args:
            u(str): Vértice atual
            visited(Dict): Dicionário com os vértices que foram visitados
            adj_list(defaultdict[List]): lista de adjacências

        Returns:
            Quantidade de vértices que estão conectados ao primeiro vértice
        """
        visited[u] = True
        count = 1
        for v in adj_list[u]:
            if not visited[v]:
                count += self.count_connected_vertecies(v, visited, adj_list)
        return count
    
    def is_valid_edge(self, v: str, u: str, adj_list: defaultdict[List]) -> bool:
        """Avalia se uma aresta é uma ponte ou não

        Args:
            v(str): Vértice de inicio
            u(str): Vértice que está ligado com v
            adj_list(defaultdict[List]): lista de adjacências

        Returns:
            bool 
        """
        c1, c2 = 0, 0
        self.remove_edge(v, u, adj_list)
        visited = {i: False for i in self.N}
        c1 = self.count_connected_vertecies(u, visited, adj_list)
        self.add_edge(v, u, adj_list)
        visited = {i: False for i in self.N}
        c2 = self.count_connected_vertecies(u, visited, adj_list)
        if c2 == c1: return True
        return False

    def get_vertex(self, v: str, adj_list: defaultdict[List], path: List) -> None:
        """Adiciona os vértices presentes no caminho euleriano

        Args:
            v(str): Vértice de inicio
            adj_list(defaultdict[List]): lista de adjacências
            path(List): Lista contendo os vértices presente no caminho euleriano
        """
        path.append(v)
        if len(adj_list[v]) == 0:
            return
        if len(adj_list[v]) == 1:
            u = adj_list[v][0]
            self.remove_edge(v, u, adj_list)
            self.get_vertex(u, adj_list, path)
            return 
        for u in adj_list[v]:
            if self.is_valid_edge(v, u, adj_list):
                self.remove_edge(v, u, adj_list)
                self.get_vertex(u, adj_list, path)
                return

    def make_a_path(self, v_list: List, adj_edge: defaultdict[List]) -> List:
        """Gera o caminho euleriano

        Args:
            v_list(List): Lista contendo os vértices do caminho euleriano
            adj_edge(defaultdict[List]): Dicionário contendo as arestas sobre o vértice

        Returns:
            path(List): Lista com os vértices do caminho euleriano
        """
        path = []
        for v in range(len(v_list)- 1):
            v1, v2 = v_list[v], v_list[v + 1]
            aresta_sobre_v1 = adj_edge[v1]
            aresta_sobre_v2 = adj_edge[v2]
            if v1 == v2:
                for a in aresta_sobre_v1:
                    if self.A[a].getV1() == self.A[a].getV2():
                        aresta_adj = a
                        break
            else:
                aresta_adj = sorted(list(set(aresta_sobre_v1).intersection(set(aresta_sobre_v2))))[0]
            if v == 0:
                path.append(v1)
            path.append(aresta_adj)
            path.append(v2)
            adj_edge[v1].remove(aresta_adj)
            if v1 != v2:
                adj_edge[v2].remove(aresta_adj)
        return path

    def euler_path_circuit(self) -> Union[List, bool]:
        """Função de setup para a busca do caminho euleriano

        Returns:
            List | False(bool)
        """
        if not self.conexo():
            return False
        odd, odd_vertex = 0, 0
        adj_list = self.make_ajd_list()
        adj_edge = {i: self.arestas_sobre_vertice(i) for i in self.N}
        for i in self.N:
            if self.grau(i) % 2 == 1:
                odd += 1
                odd_vertex = i
        aux = []
        if odd == 0:
            if len(self.N) == 1:
                self.get_vertex(self.N[0], adj_list, aux)
            else:
                self.get_vertex(self.N[1], adj_list, aux)
            return self.make_a_path(aux, adj_edge)
        elif odd == 2:
            self.get_vertex(odd_vertex, adj_list, aux)
            return self.make_a_path(aux, adj_edge)
        else:
            return False
