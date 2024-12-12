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

    def invertir(self):
        anterior = None
        actual = self.cabeza
        while actual:
            siguiente = actual.siguiente  # Guardamos el siguiente nodo
            actual.siguiente = anterior   # Invertimos la referencia
            anterior = actual             # Nos movemos hacia adelante
            actual = siguiente            # Continuamos con el siguiente nodo
        self.cabeza = anterior             # La cabeza ahora es el último nodo invertido

# Ejemplo de uso
lista = ListaEnlazada()
lista.agregar(1)
lista.agregar(2)
lista.agregar(3)
lista.agregar(4)

print("Lista original:")
lista.imprimir()

lista.invertir()

print("Lista invertida:")
lista.imprimir()
