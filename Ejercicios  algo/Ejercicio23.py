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

    def contar_hojas(self):
        return self._contar_hojas_recursivo(self.raiz)

    def _contar_hojas_recursivo(self, nodo):
        if nodo is None:
            return 0
        if nodo.izquierdo is None and nodo.derecho is None:
            return 1  # Es un nodo hoja
        # Suma las hojas de los subárboles izquierdo y derecho
        return self._contar_hojas_recursivo(nodo.izquierdo) + self._contar_hojas_recursivo(nodo.derecho)

# Ejemplo de uso
arbol = ArbolBinario()
arbol.insertar(50)
arbol.insertar(30)
arbol.insertar(70)
arbol.insertar(20)
arbol.insertar(40)
arbol.insertar(60)
arbol.insertar(80)

print("Número de hojas en el árbol binario:")
print(arbol.contar_hojas())  # Salida: 4
