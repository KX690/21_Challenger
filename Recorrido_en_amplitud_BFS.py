from collections import deque
visitados =set()


# Crear el grafo como un diccionario
grafo = {
    0: [1,2],
    1: [0,3,4],
    2: [0,4],
    3: [1],
    4: [1,2]
}

# Función para realizar el recorrido BFS
def bfs(grafo, nodo_inicial):
    cola = deque([nodo_inicial])
    visitados.add(nodo_inicial)
    
    while cola:
        nodo = cola.popleft()
        print(nodo, end=' ')
        
        for vecino in grafo[nodo]:
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append(vecino)
                
# Realizar el recorrido DFS
print("Recorrido bFS del grafo comenzando desde el nodo 0:")
bfs(grafo, 0,visitados)
print()
