from bibgrafo.aresta import Aresta
from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from bibgrafo.grafo_exceptions import *
from itertools import combinations
from typing import List, Union


class MeuGrafo(GrafoListaAdjacencia):

    def vertices_nao_adjacentes(self) -> List[int]:
        '''Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...].
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.

        Returns:
            list
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
            int
        
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
            list

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
        
