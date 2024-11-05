import random

class OrderedRecordArray:
    def __init__(self, initialSize, key=lambda x: x):  # Constructor con clave opcional
        self.__a = [None] * initialSize  # Arreglo para almacenar elementos
        self.__nItems = 0  # Número de elementos en el arreglo inicialmente
        self.__key = key  # Función para obtener la clave de un elemento

    def __len__(self):  # Retorna el número de elementos
        return self.__nItems

    def get(self, n):  # Retorna el valor en el índice n
        if 0 <= n < self.__nItems:  # Verifica si n está dentro de los límites
            return self.__a[n]  # Retorna el elemento solo si está en los límites
        raise IndexError("Index " + str(n) + " is out of range")

    def find(self, key):  # Encuentra el índice de un elemento o el punto de inserción
        lo = 0  # Límite inferior
        hi = self.__nItems - 1  # Límite superior
        while lo <= hi:
            mid = (lo + hi) // 2  # Selecciona el punto medio
            if self.__key(self.__a[mid]) == key:  # ¿Elemento encontrado?
                return mid  # Devuelve la posición del elemento
            elif self.__key(self.__a[mid]) < key:  # ¿Clave en la mitad superior?
                lo = mid + 1  # Ajusta el límite inferior
            else:
                hi = mid - 1  # Ajusta el límite superior
        return lo  # No encontrado, devuelve el punto de inserción

    def search(self, key):  # Busca un registro por su clave
        idx = self.find(key)  # Encuentra el índice probable
        if idx < self.__nItems and self.__key(self.__a[idx]) == key:  # Si está dentro de límites y coincide
            return self.__a[idx]  # Devuelve el elemento encontrado
        return None  # No encontrado

    def insert(self, item):  # Inserta un elemento en la posición correcta
        if self.__nItems >= len(self.__a):  # Verifica si el arreglo está lleno
            raise Exception("Array overflow")  # Lanza una excepción si no hay espacio
        j = self.find(self.__key(item))  # Encuentra dónde debe ir el elemento
        for k in range(self.__nItems, j, -1):  # Mueve los elementos mayores a la derecha
            self.__a[k] = self.__a[k - 1]
        self.__a[j] = item  # Inserta el elemento
        self.__nItems += 1  # Incrementa el número de elementos

    def delete(self, item):  # Elimina una ocurrencia del elemento
        j = self.find(self.__key(item))  # Busca el índice del elemento
        if j < self.__nItems and self.__a[j] == item:  # Verifica si el elemento existe
            self.__nItems -= 1  # Reduce el número de elementos
            for k in range(j, self.__nItems):  # Mueve los elementos mayores a la izquierda
                self.__a[k] = self.__a[k + 1]
            return True  # Devuelve True si se eliminó correctamente
        return False  # Elemento no encontrado, devuelve False

    def merge(self, arr):
        # Verifica que las funciones de clave sean iguales
        if self.__key != arr.__key:
            raise ValueError("Las funciones de clave de los objetos no son idénticas.")

        # Crear una nueva lista lo suficientemente grande para contener ambos arrays
        newSize = self.__nItems + arr.__nItems
        newArray = [None] * newSize

        # Índices para recorrer ambos arrays
        i, j, k = 0, 0, 0

        # Fusiona ambos arreglos en newArray
        while i < self.__nItems and j < arr.__nItems:
            if self.__key(self.__a[i]) <= self.__key(arr.__a[j]):
                newArray[k] = self.__a[i]
                i += 1
            else:
                newArray[k] = arr.__a[j]
                j += 1
            k += 1

        # Si quedan elementos en el array original, copiarlos
        while i < self.__nItems:
            newArray[k] = self.__a[i]
            i += 1
            k += 1

        # Si quedan elementos en el array a fusionar, copiarlos
        while j < arr.__nItems:
            newArray[k] = arr.__a[j]
            j += 1
            k += 1

        # Actualizar el array y el contador de elementos
        self.__a = newArray
        self.__nItems = newSize

    def __str__(self):  # Definición especial para la función str()
        ans = "["  # Inicia con corchete izquierdo
        for i in range(self.__nItems):  # Recorre todos los elementos
            if len(ans) > 1:  # Agrega coma solo si hay elementos previos
                ans += ", "
            ans += str(self.__a[i])  # Convierte el elemento a cadena
        ans += "]"  # Cierra con corchete derecho
        return ans


# Pruebas para el método merge()
array1 = OrderedRecordArray(10)
array2 = OrderedRecordArray(10)

# Insertar algunos números aleatorios en ambos arrays, asegurando orden
for num in sorted(random.sample(range(1, 50), 5)):
    array1.insert(num)
for num in sorted(random.sample(range(50, 100), 3)):
    array2.insert(num)

print("Array 1 antes de la fusión:", array1)
print("Array 2 antes de la fusión:", array2)

# Fusionar array2 en array1
array1.merge(array2)

print("Array 1 después de la fusión:", array1)