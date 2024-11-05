class Array:
    def __init__(self, capacity):
        self.__a = [None] * capacity  # Inicializa el array con tamaño fijo
        self.__nItems = 0  # Contador de elementos en el array

    def insert(self, value):
        if self.__nItems < len(self.__a):  # Verifica si hay espacio en el array
            self.__a[self.__nItems] = value
            self.__nItems += 1  # Aumenta el contador de elementos
        else:
            print("Array is at full capacity.")

    def bubbleSort(self):
        for last in range(self.__nItems - 1, 0, -1):
            for inner in range(last):
                if self.__a[inner] > self.__a[inner + 1]:
                    # Intercambio sin un método swap adicional
                    self.__a[inner], self.__a[inner + 1] = self.__a[inner + 1], self.__a[inner]
        # Retorna solo los elementos válidos, sin incluir posiciones vacías
        return self.__a[:self.__nItems]
    
    def mediana(self):
       if self.__nItems == 0:  # Si no hay elementos, la mediana no está definida
            return None
       n = self.bubbleSort
       mit= self.__nItems/2
       if self.__nItems % 2 == 0:
           return (n[mit -1]+n[mit])/ 2.0
       else:
           return n[mit]
        
        
    def median(self):
        if self.__nItems == 0:  # Si no hay elementos, la mediana no está definida
            return None

        # Primero, ordenamos el array
        sorted_array = self.bubbleSort()  # O también puedes usar cocktailSort()
        
        mid_index = self.__nItems // 2
        if self.__nItems % 2 == 0:  # Si el número de elementos es par
            
            return (sorted_array[mid_index - 1] + sorted_array[mid_index]) / 2.0 
        else:  # Si el número de elementos es impar
            return sorted_array[mid_index]
        
        
    def cocktailSort(self):
        start = 0
        end = self.__nItems - 1
        swapped = True
        while swapped:
            swapped = False
            # Movimiento de izquierda a derecha
            for i in range(start, end):
                if self.__a[i] > self.__a[i + 1]:
                    self.__a[i], self.__a[i + 1] = self.__a[i + 1], self.__a[i]
                    swapped = True
            # Reducimos el rango final
            end -= 1

            # Si no hubo intercambios, el array ya está ordenado
            if not swapped:
                break

            swapped = False
            # Movimiento de derecha a izquierda
            for i in range(end, start, -1):
                if self.__a[i] < self.__a[i - 1]:
                    self.__a[i], self.__a[i - 1] = self.__a[i - 1], self.__a[i]
                    swapped = True
            # Incrementamos el rango inicial
            start += 1

        return self.__a[:self.__nItems]