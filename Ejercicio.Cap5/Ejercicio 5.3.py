class Node:
    """Clase para representar un nodo en una lista doblemente enlazada."""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Deque:
    """Clase Deque basada en una lista doblemente enlazada."""
    def __init__(self):
        self.front = None  # Nodo del frente del deque
        self.rear = None   # Nodo del final del deque
        self.size = 0      # Número de elementos en el deque

    def isEmpty(self):
        """Devuelve True si el deque está vacío."""
        return self.size == 0

    def insertLeft(self, item):
        """Inserta un elemento al frente del deque."""
        new_node = Node(item)
        if self.isEmpty():
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node
        self.size += 1

    def insertRight(self, item):
        """Inserta un elemento al final del deque."""
        new_node = Node(item)
        if self.isEmpty():
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def removeLeft(self):
        """Elimina y devuelve el elemento del frente del deque."""
        if self.isEmpty():
            raise Exception("Deque está vacío")
        data = self.front.data
        self.front = self.front.next
        if self.front is None:  # El deque queda vacío
            self.rear = None
        else:
            self.front.prev = None
        self.size -= 1
        return data

    def removeRight(self):
        """Elimina y devuelve el elemento del final del deque."""
        if self.isEmpty():
            raise Exception("Deque está vacío")
        data = self.rear.data
        self.rear = self.rear.prev
        if self.rear is None:  # El deque queda vacío
            self.front = None
        else:
            self.rear.next = None
        self.size -= 1
        return data

    def peekLeft(self):
        """Devuelve el elemento del frente del deque sin eliminarlo."""
        if self.isEmpty():
            raise Exception("Deque está vacío")
        return self.front.data

    def peekRight(self):
        """Devuelve el elemento del final del deque sin eliminarlo."""
        if self.isEmpty():
            raise Exception("Deque está vacío")
        return self.rear.data
