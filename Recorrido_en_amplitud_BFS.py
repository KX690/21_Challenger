
visitados =set()


# Crear el grafo como un diccionario
grafo = {
    0: [1,2],
    1: [0,3,4],
    2: [0,4],
    3: [1],
    4: [1,2]
}

# Función para realizar el recorrido DFS
def bfs(grafo, nodo_inicial,visitados):
    visitados.add(nodo_inicial)
    
    print(nodo_inicial, end=' ')
    
    for vecino in grafo[nodo_inicial]:
        
        if vecino not in visitados:
            
            bfs(grafo, vecino, visitados)

# Realizar el recorrido DFS
print("Recorrido DFS del grafo comenzando desde el nodo 0:")
bfs(grafo, 0,visitados)
print()
