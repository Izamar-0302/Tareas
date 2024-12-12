from collections import deque

class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = NodoArbol(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierdo is None:
                nodo.izquierdo = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo.izquierdo, valor)
        else:
            if nodo.derecho is None:
                nodo.derecho = NodoArbol(valor)
            else:
                self._insertar_recursivo(nodo.derecho, valor)

    def recorrido_por_niveles(self):
        if self.raiz is None:
            return []

        cola = deque([self.raiz])  # Inicializamos la cola con la raíz
        resultado = []

        while cola:
            nodo_actual = cola.popleft()  # Sacamos el nodo al frente de la cola
            resultado.append(nodo_actual.valor)  # Agregamos su valor al resultado

            # Agregamos los hijos del nodo a la cola (si existen)
            if nodo_actual.izquierdo:
                cola.append(nodo_actual.izquierdo)
            if nodo_actual.derecho:
                cola.append(nodo_actual.derecho)

        return resultado

# Ejemplo de uso
arbol = ArbolBinario()
arbol.insertar(50)
arbol.insertar(30)
arbol.insertar(70)
arbol.insertar(20)
arbol.insertar(40)
arbol.insertar(60)
arbol.insertar(80)

print("Recorrido por niveles (BFS):")
print(arbol.recorrido_por_niveles())  # Salida: [50, 30, 70, 20, 40, 60, 80]
