class Nodo:
    def __init__(self, dato, padre=None):
        self.dato = dato
        self.izquierda = None
        self.derecha = None
        self.padre = padre

class Arbol:
    def __init__(self):
        self.raiz = None

    def insertar(self, dato):
        if self.raiz is None:
            self.raiz = Nodo(dato)
        else:
            self._insertar_recursivo(self.raiz, dato)

    def _insertar_recursivo(self, nodo, dato):
        if dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(dato, nodo)
            else:
                self._insertar_recursivo(nodo.izquierda, dato)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(dato, nodo)
            else:
                self._insertar_recursivo(nodo.derecha, dato)

    def imprimir_en_orden(self, nodo):
        if nodo is not None:
            self.imprimir_en_orden(nodo.izquierda)
            print(nodo.dato, end=' ')
            self.imprimir_en_orden(nodo.derecha)


if __name__ == "__main__":
    arbol = Arbol()
    valores=[]
    for i in range(5):
        valor = int(input("Introduzca un valor: "))
        valores.append(valor)
    
    for valor in valores:
        arbol.insertar(valor)

    print("Árbol BST en orden:")
    arbol.imprimir_en_orden(arbol.raiz)
