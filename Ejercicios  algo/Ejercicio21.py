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

    def altura(self):
        return self._calcular_altura(self.raiz)

    def _calcular_altura(self, nodo):
        if nodo is None:
            return -1  # Altura de un árbol vacío es -1
        altura_izquierda = self._calcular_altura(nodo.izquierdo)
        altura_derecha = self._calcular_altura(nodo.derecho)
        return 1 + max(altura_izquierda, altura_derecha)

# Ejemplo de uso
arbol = ArbolBinario()
arbol.insertar(50)
arbol.insertar(30)
arbol.insertar(70)
arbol.insertar(20)
arbol.insertar(40)
arbol.insertar(60)
arbol.insertar(80)

print("Altura del árbol binario:")
print(arbol.altura())  # Salida: 2
