from meu_grafo_matriz_adjacencia_nao_dir import MeuGrafo

paraiba = MeuGrafo()

paraiba.adicionaVertice("J")
paraiba.adicionaVertice("C")
paraiba.adicionaVertice("E")
paraiba.adicionaVertice("P")
paraiba.adicionaVertice("M")
paraiba.adicionaVertice("T")
paraiba.adicionaVertice("Z")
paraiba.adicionaAresta("a1", "J", "C")
paraiba.adicionaAresta("a2", "C", "E")
paraiba.adicionaAresta("a3", "C", "E")
paraiba.adicionaAresta("a4", "C", "P")
paraiba.adicionaAresta("a5", "C", "P")
paraiba.adicionaAresta("a6", "C", "M")
paraiba.adicionaAresta("a7", "C", "T")
paraiba.adicionaAresta("a8", "M", "T")
paraiba.adicionaAresta("a9", "T", "Z")
# paraiba.adicionaAresta("a10", "C", "C")


def separador():
    print("-"*50)

separador()

print(paraiba)
separador()

if paraiba.ha_laco():
    print("Há laços no grafo")
else:
    print("Não há laços nesse grafo")
separador()

if paraiba.ha_paralelas():
    print("Há retas paralelas")
else:
    print("Não há retas paralelas")
separador()

for n in paraiba.N:
    print(f"Grau do vértice {n} -> {paraiba.grau(n)}")
separador()

for n in paraiba.N:
    print(f"Arestas sobre o vértice {n}: {paraiba.arestas_sobre_vertice(n)}")
separador()

print(f"Lista de vértices não adjacentes: {paraiba.vertices_nao_adjacentes()}")
separador()

if paraiba.eh_completo():
    print("O grafo é completo")
else: 
    print("O grafo não é completo")
separador()