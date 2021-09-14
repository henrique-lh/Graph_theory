from __future__ import annotations
from typing import Dict, List, Set, Union
from bibgrafo.grafo_matriz_adj_dir import *
from bibgrafo.grafo_exceptions import *
import math
from collections import deque
from copy import deepcopy

class MeuGrafo(GrafoMatrizAdjacenciaDirecionado):
    def warshall(self) -> List[List]:
        """Retorna a matriz de alcançabilidade de grafo

        Returns:
            List[List]: Matriz de alcançabilidade
        """
        matriz_clone = [[0 if len(self.M[j][i]) == 0 else 1 for i in range(len(self.M))] for j in range(len(self.M))]
        qt_termos = len(self.M)
        for i in range(qt_termos):
            for j in range(qt_termos):
                if matriz_clone[j][i] == 1:
                    for k in range(qt_termos):
                        matriz_clone[j][k] = max(matriz_clone[j][k], matriz_clone[i][k])
        return matriz_clone
    
    def remover_paralelas(self, grafo: MeuGrafo) -> None:
        """
        Remove arestas paralelas de um grafo

        Args:
            grafo (MeuGrafo): Cópia do grafo original

        Return:
            None
        """
        tamanho = len(grafo.N)
        for i in range(tamanho):
            for j in range(tamanho):
                valor = grafo.M[i][j]
                if len(valor) > 1:
                    aux_key, aux_peso, aux_aresta = None, None, None
                    for key, aresta in valor.items():
                        if aux_peso:
                            if aresta.getPeso() < aux_peso:
                                aux_peso = aresta.getPeso()
                                aux_key = key
                                aux_aresta = aresta
                        else:
                            aux_key = key
                            aux_peso = aresta.getPeso()
                            aux_aresta = aresta
                    grafo.M[i][j] = {aux_key: aux_aresta}


    def remover_lacos(self, grafo: MeuGrafo) -> None:
        """Remove laços de um grafo

        Args:
            grafo (MeuGrafo): Cópia do grafo original
        """
        tamanho = len(grafo.N)
        for i in range(tamanho):
            if len(grafo.M[i][i]) > 0:
                grafo.M[i][i] = {}

    def caminho_dijkstra(self, atual: str, pi: Dict, path: List, grafo: MeuGrafo) -> None:
        """Forma o caminhho presente no grafo

        Args:
            atual (str): Vértice atual
            pi (Dict): Dicionário com menor caminho
            path (List): Contêiner que guarda o menor caminho
        """
        v1, v2 = atual, pi[atual]
        path.insert(0, v1)
        while v2 != 0:
            idx_v1, idx_v2 = grafo.N.index(v1), grafo.N.index(v2)
            for _, aresta in grafo.M[idx_v2][idx_v1].items(): pass
            path.insert(0, aresta.getRotulo())
            path.insert(0, v2)
            v1 = v2
            v2 = pi[v1]

    def dijkstra(self, v_inicial: str, v_final: str, carga_inical: int, carga_max: int, vertices_de_recarga: Union[List, Set]) -> Union[List, bool]:
        """Encontra o menor caminho entre dois vértices para um drone com uma carga de bateria inicial

        Args:
            v_inicial (str): Vértice inicial
            v_final (str): Vértice final
            carga_inical (int): Carga inicial do drone
            carga_max (int): Carga máxima permitida no drone
            vertices_de_recarga (List): Lista de vértices com ponto de recarga

        Raises:
            VerticeInvalidoException: Caso vértice não exista no graof

        Returns:
            Union[List, bool]: Vértices no menor caminho caso ele exista. Caso contrário é retornado um valor booleano
        """
        if v_inicial not in self.N or v_final not in self.N:
            raise VerticeInvalidoException

        if carga_inical < 0 :
            return False
        grafo = deepcopy(self)
        self.remover_paralelas(grafo)
        self.remover_lacos(grafo)
        INF = math.inf
        beta = {i: INF for i in grafo.N}
        beta[v_inicial] = 0
        fi = {i: 0 for i in grafo.N}
        fi[v_inicial] = 1
        pi = {i: 0 for i in grafo.N}
        gama = {i: INF for i in grafo.N}
        gama[v_inicial] = carga_max if v_inicial in vertices_de_recarga else carga_inical
        w = v_inicial
        w_index = grafo.N.index(w)
        while True:
            w_vizinhos = [grafo.M[w_index][a] for a in range(len(grafo.M)) if grafo.M[w_index][a]]
            for dicionario in w_vizinhos:
                for _, aresta in dicionario.items():
                    r = aresta.getV1() if aresta.getV1() != w else aresta.getV2()
                    alpha = aresta.getPeso()
                    condicional_1 = fi[r] == 0 and beta[r] > beta[w] + alpha and gama[w] - alpha >= 0
                    if condicional_1:
                        beta[r] = beta[w] + alpha
                        pi[r] = w
                        gama[r] = carga_max if r in vertices_de_recarga else gama[w] - alpha
            r_ast = None
            aux = INF
            for v in grafo.N:
                condicional_2 = fi[v] == 0 and beta[v] < INF and beta[v] < aux
                if condicional_2:
                    aux = beta[v]
                    r_ast = v
            if r_ast is None:
                return False
            else:
                fi[r_ast] = 1
                w = r_ast
                w_index = grafo.N.index(w)
            if w == v_final:
                break
        path = []
        self.caminho_dijkstra(v_final, pi, path, grafo)
        return path

