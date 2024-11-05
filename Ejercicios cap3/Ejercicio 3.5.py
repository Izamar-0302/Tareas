from audioop import reverse


class Array(object):
    def __init__(self, initialSize):  # Constructor
        self.__a = [None] * initialSize  # El array almacenado como lista
        self.__nItems = 0  # Sin elementos en el array inicialmente

    def __len__(self):  # Devuelve el número de elementos
        return self.__nItems

    def insert(self, item):  # Inserta un elemento al final
        if self.__nItems >= len(self.__a):  # Si el array está lleno
            raise Exception("Array overflow")
        self.__a[self.__nItems] = item  
        self.__a[self.__nItems] 
# Inserta el elemento
        self.__nItems += 1  # Incrementa el número de elementos

    

    
def insertionSort(self):
        copy_count = 0  # Contador de copias
        comparison_count = 0  # Contador de comparaciones

        for outer in range(1, self.__nItems):  # Comienza desde el segundo elemento
            temp = self.__a[outer]  
     
# Elemento a insertar
            inner = outer  # Índice interno para encontrar la posición correcta

            while inner > 0:  # Recorre hacia atrás para encontrar la posición
                comparison_count += 1  # Contar la comparación
                if temp < self.__a[inner - 1]:  # Si el elemento actual es menor
                    self.__a[inner] = self.__a[inner - 1] # Desplazar el elemento hacia la derecha
                    copy_count += 1  # Contar la copia
                    inner -= 1  # Mover hacia atrás
                else:
                    break  # Si no es menor, salir del bucle

            self.__a[inner] = temp  # Colocar el elemento en su posición correcta
            copy_count += 1  # Contar la copia del elemento temporal

        print(f"Número de copias: {copy_count}")
        print(f"Número de comparaciones: {comparison_count}")

def __str__(self):  # Método para imprimir el array
        return "[" + ", ".join(str(self.__a[i]) for i in range(self.__nItems)) + "]"

# Ejemplo de prueba
if __name__ == "__main__":
    # Caso de prueba para datos ordenados inversamente
    reverse_sorted_array = Array(
   
10)
    for i in range(10, 0, -1):  # Insertar datos en orden inverso
        reverse_sorted_array.insert(i)

    
        reverse_sorted_array.insert(i)
    print("Arreglo inversamente ordenado:")
    print(reverse_sorted_array)
    reverse_sorted_array.insertionSort()

    
reverse
# Caso de prueba para datos casi ordenados
almost_sorted_array = Array(10)
for i in range(1, 10):  # Insertar datos casi ordenados
        almost_sorted_array.insert(i)
almost_sorted_array.insert(5)  # Duplicado para provocar desorden

print("\nArreglo casi ordenado:")
print(almost_sorted_array)
almost_sorted_array.insertionSort()

almost # type: ignore