class OrderedRecordArray:
    def __init__(self, initialSize, key=lambda x: x, expansion_factor=1.5, fixed_increment=None):  
        self.__a = [None] * initialSize  # Inicializa el arreglo con el tamaño dado
        self.__nItems = 0  # Inicialmente no hay elementos en el arreglo
        self.__maxSize = initialSize  # Almacena el tamaño máximo actual del arreglo
        self.__key = key  # Función clave para ordenar los elementos
        self.__expansion_factor = expansion_factor  # Factor de expansión (para multiplicación)
        self.__fixed_increment = fixed_increment  # Incremento fijo (para adición)

    def __len__(self):  # Retorna el número de elementos
        return self.__nItems

    def get(self, n):  # Retorna el valor en el índice n
        if 0 <= n < self.__nItems:
            return self.__a[n]
        raise IndexError("Index " + str(n) + " is out of range")

    def find(self, key):  # Encuentra el índice de un elemento o el punto de inserción
        lo = 0
        hi = self.__nItems - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if self.__key(self.__a[mid]) == key:
                return mid
            elif self.__key(self.__a[mid]) < key:
                lo = mid + 1
            else:
                hi = mid - 1
        return lo

    def search(self, key):  # Busca un registro por su clave
        idx = self.find(key)
        if idx < self.__nItems and self.__key(self.__a[idx]) == key:
            return self.__a[idx]
        return None

    def insert(self, item):  # Inserta un elemento en la posición correcta
        if self.__nItems >= self.__maxSize:  # Si el arreglo está lleno, se expande
            self.__expand()  # Llama a la función de expansión
        j = self.find(self.__key(item))
        for k in range(self.__nItems, j, -1):  # Mueve los elementos mayores a la derecha
            self.__a[k] = self.__a[k - 1]
        self.__a[j] = item
        self.__nItems += 1

    def __expand(self):  # Expande el tamaño del arreglo
        if self.__fixed_increment is not None:  # Estrategia de incremento fijo
            newSize = self.__maxSize + self.__fixed_increment
        else:  # Estrategia de expansión por factor
            newSize = int(self.__maxSize * self.__expansion_factor)
        
        new_array = [None] * newSize  # Crea un nuevo arreglo más grande
        for i in range(self.__nItems):  # Copia los elementos existentes
            new_array[i] = self.__a[i]
        
        self.__a = new_array  # Reemplaza el arreglo viejo
        self.__maxSize = newSize  # Actualiza el tamaño máximo

    def delete(self, item):  # Elimina todas las ocurrencias de un elemento
        target_key = self.__key(item)
        original_size = self.__nItems
        idx = self.find(target_key)
        if idx < self.__nItems and self.__key(self.__a[idx]) == target_key:
            i = idx
            while i < self.__nItems and self.__key(self.__a[i]) == target_key:
                for k in range(i, self.__nItems - 1):
                    self.__a[k] = self.__a[k + 1]
                self.__nItems -= 1
                self.__a[self.__nItems] = None
            return True
        return False

    def __str__(self):
        ans = "["
        for i in range(self.__nItems):
            if len(ans) > 1:
                ans += ", "
            ans += str(self.__a[i])
        ans += "]"
        return ans


# Pruebas de expansión con ambas estrategias

# Prueba con incremento fijo
print("Prueba con incremento fijo:")
array_fixed = OrderedRecordArray(5, fixed_increment=5)  # Expande en bloques de 5
for i in range(20):
    array_fixed.insert(i)
    print(f"Insertando {i}: {array_fixed}")

# Prueba con multiplicación por factor
print("\nPrueba con expansión por factor:")
array_factor = OrderedRecordArray(5, expansion_factor=2)  # Duplica el tamaño cuando se llena
for i in range(20):
    array_factor.insert(i)
    print(f"Insertando {i}: {array_factor}")