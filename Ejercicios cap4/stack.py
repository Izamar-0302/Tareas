class Stack(object):
    def __init__(self, max_size):  # Constructor
        self.__stackList = [None] * max_size  # La pila almacenada como lista
        self.__top = -1  # Sin elementos inicialmente

    def push(self, item):  # Insertar elemento en la parte superior de la pila
        if self.isFull():  # Verificar si la pila está llena
            raise OverflowError("No se puede insertar: la pila está llena.")
        self.__top += 1  # Avanzar el puntero
        self.__stackList[self.__top] = item  # Almacenar el elemento

    def pop(self):  # Quitar el elemento superior de la pila
        if self.isEmpty():  # Verificar si la pila está vacía
            raise IndexError("No se puede quitar: la pila está vacía.")
        top = self.__stackList[self.__top]  # Elemento en la parte superior
        self.__stackList[self.__top] = None  # Eliminar la referencia del elemento
        self.__top -= 1  # Disminuir el puntero
        return top  # Devolver el elemento superior

    def peek(self):  # Devolver el elemento superior
        if self.isEmpty():  # Verificar si la pila está vacía
            raise IndexError("No se puede consultar: la pila está vacía.")
        return self.__stackList[self.__top]  # Devolver el elemento superior

    def isEmpty(self):  # Verificar si la pila está vacía
        return self.__top < 0

    def isFull(self):  # Verificar si la pila está llena
        return self.__top >= len(self.__stackList) - 1

    def __len__(self):  # Devolver el número de elementos en la pila
        return self.__top + 1

    def __str__(self):  # Convertir la pila a cadena
        ans = "["  # Comenzar con corchete izquierdo
        for i in range(self.__top + 1):  # Recorrer elementos actuales
            if len(ans) > 1:  # Separar elementos con coma
                ans += ", "
            ans += str(self.__stackList[i])  # Añadir el elemento en forma de cadena
        ans += "]"  # Cerrar con corchete derecho
        return ans