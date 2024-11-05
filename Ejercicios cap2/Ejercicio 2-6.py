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

    def delete(self, item):  # Elimina todas las ocurrencias de un elemento
        target_key = self.__key(item)
        original_size = self.__nItems  # Guardar el tamaño original para verificar cambios

        # Encuentra el índice del primer elemento que coincide con la clave
        idx = self.find(target_key)

        # Si el elemento en idx coincide con el elemento de destino, elimina todas sus ocurrencias
        if idx < self.__nItems and self.__key(self.__a[idx]) == target_key:
            # Elimina todas las ocurrencias moviendo los elementos a la izquierda
            i = idx
            while i < self.__nItems and self.__key(self.__a[i]) == target_key:
                for k in range(i, self.__nItems - 1):
                    self.__a[k] = self.__a[k + 1]
                self.__nItems -= 1  # Reducir el tamaño después de eliminar
                self.__a[self.__nItems] = None  # Limpiar el último elemento
            return True  # Devolvemos True si hubo eliminaciones

        return False  # Devuelve False si no se encontró el elemento y no se hicieron cambios

    def __str__(self):  # Definición especial para la función str()
        ans = "["  # Inicia con corchete izquierdo
        for i in range(self.__nItems):  # Recorre todos los elementos
            
         if len(ans) > 1:  # Agrega coma solo si hay elementos previos
                ans += ", "
         ans += str(self.__a[i])  # Convierte el elemento a cadena
        ans += "]"  # Cierra con corchete derecho
        return ans


# Pruebas para eliminar duplicados
array = OrderedRecordArray(10)

# Insertar elementos, incluidos duplicados
array.insert(10)
array.insert(20)
array.insert(20)
array.insert(30)
array.insert(40)
array.insert(20)  # Otro duplicado de 20

print("Array antes de eliminar duplicados:", array)

# Eliminar todas las ocurrencias de 20
deleted = array.delete(20)

print("Array después de eliminar duplicados de 20:", array)
print("¿Se eliminaron elementos?", deleted)

# Intento de eliminar un elemento inexistente
deleted_nonexistent = array.delete(50)
print("Array después de intentar eliminar 50:", array)
print("¿Se eliminaron elementos?", deleted_nonexistent)