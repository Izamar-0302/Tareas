class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def imprimir(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

def fusionar_listas(lista1, lista2):
    dummy = Nodo(0)  # Nodo temporal para construir la lista fusionada
    actual = dummy

    # Punteros a las cabezas de las listas
    nodo1 = lista1.cabeza
    nodo2 = lista2.cabeza

    # Recorremos ambas listas y fusionamos
    while nodo1 and nodo2:
        if nodo1.valor <= nodo2.valor:
            actual.siguiente = nodo1
            nodo1 = nodo1.siguiente
        else:
            actual.siguiente = nodo2
            nodo2 = nodo2.siguiente
        actual = actual.siguiente

    # Agregar los nodos restantes de cualquiera de las listas
    if nodo1:
        actual.siguiente = nodo1
    if nodo2:
        actual.siguiente = nodo2

    # Crear la nueva lista fusionada
    lista_fusionada = ListaEnlazada()
    lista_fusionada.cabeza = dummy.siguiente

    return lista_fusionada

# Ejemplo de uso
lista1 = ListaEnlazada()
lista1.agregar(7)
lista1.agregar(5)
lista1.agregar(3)

lista2 = ListaEnlazada()
lista2.agregar(6)
lista2.agregar(4)
lista2.agregar(2)

print("Lista 1:")
lista1.imprimir()

print("Lista 2:")
lista2.imprimir()

lista_fusionada = fusionar_listas(lista1, lista2)

print("Lista fusionada ordenada:")
lista_fusionada.imprimir()
