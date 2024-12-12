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

    def eliminar_duplicados(self):
        valores_vistos = set()  # Conjunto para guardar los valores ya encontrados
        actual = self.cabeza
        previo = None
        while actual:
            if actual.valor in valores_vistos:
                # Si el valor ya está en el conjunto, eliminamos el nodo
                previo.siguiente = actual.siguiente
            else:
                # Si el valor no está en el conjunto, lo agregamos
                valores_vistos.add(actual.valor)
                previo = actual
            actual = actual.siguiente

# Ejemplo de uso
lista = ListaEnlazada()
lista.agregar(3)
lista.agregar(2)
lista.agregar(3)
lista.agregar(1)
lista.agregar(2)

print("Lista original:")
lista.imprimir()

lista.eliminar_duplicados()

print("Lista sin duplicados:")
lista.imprimir()
