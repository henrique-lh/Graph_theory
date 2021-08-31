from bibgrafo.grafo_matriz_adj_dir import *
from bibgrafo.grafo_exceptions import *

class MeuGrafo(GrafoMatrizAdjacenciaDirecionado):
    def warshall(self):
        """
        Retorna a matriz de alcançabilidade de grafo
        :return: Lista de listas preenchidas com 1, em caso de caminho entre vértices e com 0 caso contrário
        """
        matriz_clone = [[0 if len(self.M[j][i]) == 0 else 1 for i in range(len(self.M))] for j in range(len(self.M))]
        qt_termos = len(self.M)
        for i in range(qt_termos):
            for j in range(qt_termos):
                if matriz_clone[j][i] == 1:
                    for k in range(qt_termos):
                        matriz_clone[j][k] = max(matriz_clone[j][k], matriz_clone[i][k])
        return matriz_clone
