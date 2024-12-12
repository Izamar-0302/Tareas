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

    def recorrido_inorden(self):
        resultado = []
        self._recorrido_inorden_recursivo(self.raiz, resultado)
        return resultado

    def _recorrido_inorden_recursivo(self, nodo, resultado):
        if nodo is not None:
            self._recorrido_inorden_recursivo(nodo.izquierdo, resultado)
            resultado.append(nodo.valor)
            self._recorrido_inorden_recursivo(nodo.derecho, resultado)

    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, nodo, valor):
        if nodo is None:
            return False
        if nodo.valor == valor:
            return True
        elif valor < nodo.valor:
            return self._buscar_recursivo(nodo.izquierdo, valor)
        else:
            return self._buscar_recursivo(nodo.derecho, valor)

# Ejemplo de uso
arbol = ArbolBinario()
arbol.insertar(50)
arbol.insertar(30)
arbol.insertar(70)
arbol.insertar(20)
arbol.insertar(40)
arbol.insertar(60)
arbol.insertar(80)

print("Recorrido en orden (inorder):")
print(arbol.recorrido_inorden())

print("Buscar elemento 40:")
print(arbol.buscar(40))  # True

print("Buscar elemento 90:")
print(arbol.buscar(90))  # False
