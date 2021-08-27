from meu_grafo import MeuGrafo

paraiba = MeuGrafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])
paraiba.adicionaAresta('a1', 'J', 'C')
paraiba.adicionaAresta('a2', 'C', 'E')
paraiba.adicionaAresta('a3', 'C', 'E')
paraiba.adicionaAresta('a4', 'P', 'C')
paraiba.adicionaAresta('a5', 'P', 'C')
paraiba.adicionaAresta('a6', 'M', 'C')
paraiba.adicionaAresta('a7', 'T', 'C')
paraiba.adicionaAresta('a8', 'M', 'T')
paraiba.adicionaAresta('a9', 'T', 'Z')
def separador():
    print("-"*159)

print("\nNós...", paraiba.N)
separador()

print("Arestas...")
for a in paraiba.A:
    print(paraiba.A[a])
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

print("BFS no grafo da paraiba (começando no vértice J)")
print(paraiba.BFS("J"))
separador()

print("DFS no grafo da paraiba (começando no vértice J)")
print(paraiba.DFS('J'))
separador()

if paraiba.ha_ciclo():
    print(f"Ciclo presente no grafo da paraiba: {paraiba.ha_ciclo()}")
else:
    print("Não há ciclo no grafo da paraiba")
separador()

for c in range(6):
    if paraiba.caminho(c):
        print(f"Caminho de tamanho {c} no grafo da paraiba: {paraiba.caminho(c)}")
    else:
        print(f"Não há um caminho de tamanho {c}")
separador()

if paraiba.conexo():
    print("O grafo da paraiba é conexo")
else:
    print("O grafo da paraiba não é conexo")
separador()