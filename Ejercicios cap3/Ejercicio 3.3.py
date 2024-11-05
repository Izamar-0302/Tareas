class Array(object):
    def __init__(self, initialSize):  # Constructor
        self.__a = [None] * initialSize  # El array almacenado como lista
        self.__nItems = 0  # Sin elementos en el array inicialmente

    # Métodos anteriores (get, set, insert, find, delete, etc.)

    # Método para eliminar duplicados de un arreglo previamente ordenado
    def deduplicate(self):
        if self.__nItems < 2:  # No hay duplicados si hay 0 o 1 elementos
            return
        
        # Índice para almacenar el siguiente elemento único
        unique_index = 1

        for i in range(1, self.__nItems):
            # Solo copiamos el elemento si es diferente del último único almacenado
            if self.__a[i] != self.__a[unique_index - 1]:
                self.__a[unique_index] = self.__a[i]
                unique_index += 1
        
        # Actualizamos el tamaño para reflejar la eliminación de duplicados
        self.__nItems = unique_index

        # Opcional: Limpia el resto de los elementos redundantes
        for i in range(unique_index, len(self.__a)):
            self.__a[i] = None

    # Resto de métodos anteriores (traverse, bubbleSort, selectionSort, insertionSort, etc.)

# Ejemplo de prueba
if __name__ == "__main__":
    array = Array(10)
    array.insert(1)
    array.insert(2)
    array.insert(2)
    array.insert(3)
    array.insert(3)
    array.insert(3)
    array.insert(4)
    array.insert(5)
    print("Arreglo original con duplicados:", array)
    
    # Aplicamos deduplicate
    array.deduplicate()
    print("Arreglo después de deduplicate:", array)