class nodo(object):
    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None 
        
        
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None  # Inicialmente la lista está vacía

    def agregar_al_inicio(self, dato):
        """Agrega un nodo al principio de la lista."""
        nuevo_nodo = nodo(dato)  # Crear un nuevo nodo
        nuevo_nodo.siguiente = self.cabeza  # Apunta al nodo actual (o None si está vacío)
        self.cabeza = nuevo_nodo  # Actualiza la cabeza de la lista

    def mostrar(self):
        """Muestra todos los elementos de la lista."""
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")  # Indica el final de la lista

    def buscar(self, dato):
        """Busca un nodo por su valor."""
        actual = self.cabeza
        while actual:
            if actual.dato == dato:
                return True  # Encontrado
            actual = actual.siguiente
        return False  # No encontrado

    def eliminar(self, dato):
        """Elimina el primer nodo que contiene el valor dado."""
        actual = self.cabeza
        previo = None
        while actual:
            if actual.dato == dato:
                if previo:  # Si no es el primer nodo
                    previo.siguiente = actual.siguiente
                else:  # Si es el primer nodo
                    self.cabeza = actual.siguiente
                return True  # Nodo eliminado
            previo = actual
            actual = actual.siguiente
        return False  # Si no se encuentra el valor

# Ejemplo de uso
lista = ListaEnlazada()
lista.agregar_al_inicio(10)
lista.agregar_al_inicio(20)
lista.agregar_al_inicio(30)

# Mostrar la lista
lista.mostrar()  # 30 -> 20 -> 10 -> None

# Buscar un elemento
print(lista.buscar(20))  # True
print(lista.buscar(40))  # False

# Eliminar un elemento
lista.eliminar(20)
lista.mostrar()  # 30 -> 10 -> None

