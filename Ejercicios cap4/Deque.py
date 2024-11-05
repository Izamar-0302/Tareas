class Deque:
    def __init__(self, max_size):
        self.__dequeList = [None] * max_size  # Crear lista para almacenar elementos
        self.__max_size = max_size  # Tamaño máximo de la cola
        self.__front = 0  # Índice del frente
        self.__rear = -1  # Índice de la parte trasera
        self.__count = 0  # Contador de elementos actuales en la deque

    def insertLeft(self, item):
        if self.isFull():
            raise OverflowError("No se puede insertar a la izquierda: la deque está llena.")
        self.__front = (self.__front - 1) % self.__max_size  # Ajustar el índice del frente con envoltura
        self.__dequeList[self.__front] = item
        self.__count += 1

    def insertRight(self, item):
        if self.isFull():
            raise OverflowError("No se puede insertar a la derecha: la deque está llena.")
        self.__rear = (self.__rear + 1) % self.__max_size  # Ajustar el índice de la parte trasera con envoltura
        self.__dequeList[self.__rear] = item
        self.__count += 1

    def removeLeft(self):
        if self.isEmpty():
            raise IndexError("No se puede eliminar desde la izquierda: la deque está vacía.")
        item = self.__dequeList[self.__front]
        self.__dequeList[self.__front] = None  # Limpiar referencia
        self.__front = (self.__front + 1) % self.__max_size  # Ajustar el índice del frente con envoltura
        self.__count -= 1
        return item

    def removeRight(self):
        if self.isEmpty():
            raise IndexError("No se puede eliminar desde la derecha: la deque está vacía.")
        item = self.__dequeList[self.__rear]
        self.__dequeList[self.__rear] = None  # Limpiar referencia
        self.__rear = (self.__rear - 1) % self.__max_size  # Ajustar el índice de la parte trasera con envoltura
        self.__count -= 1
        return item

    def peekLeft(self):
        if self.isEmpty():
            raise IndexError("No se puede ver desde la izquierda: la deque está vacía.")
        return self.__dequeList[self.__front]

    def peekRight(self):
        if self.isEmpty():
            raise IndexError("No se puede ver desde la derecha: la deque está vacía.")
        return self.__dequeList[self.__rear]

    def isEmpty(self):
        return self.__count == 0

    def isFull(self):
        return self.__count == self.__max_size

    def __str__(self):
        return str([self.__dequeList[(self.__front + i) % self.__max_size] for i in range(self.__count)])
    