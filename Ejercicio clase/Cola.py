import random
class Cola:
    
    def __init__(self):
        self.elementos = []  # Lista que almacena los elementos
        self.__nItems = 0  # Número de elementos en la cola

    # Método para añadir un elemento a la cola
    def apilar(self, elemento):
        self.elementos.append(elemento)
        self.__nItems += 1  # Aumentar el número de elementos
        
    def __len__(self):  # Special def for len() function
        return self.__nItems  # Return number of items
        
    # Método para obtener el valor en un índice n
    def get(self, n):  # Retornar el valor en el índice n
        if 0 <= n < self.__nItems:  # Verificar que el índice está dentro de los límites
            return self.elementos[n]  # Retornar el elemento en la posición n
        return None  # Si el índice está fuera de los límites, devolver None

    # Método para recorrer todos los elementos y aplicar una función (por defecto print)
    def traverse(self, function=print):  
        for j in range(self.__nItems):  # Recorrer todos los elementos
            function(self.elementos[j])  # Aplicar la función a cada elemento

    # Método para eliminar un elemento específico
    def ten(self, item):  
        for j in range(self.__nItems):  # Buscar el elemento en la lista
            if self.elementos[j] == item:  # Si el elemento coincide
                ten_item = self.elementos[j]  # Guardar el elemento a eliminar
                self.__nItems -= 1  # Reducir el número de elementos
                # Mover los elementos hacia la izquierda
                for k in range(j, self.__nItems):
                    self.elementos[k] = self.elementos[k + 1]
                self.elementos.pop()  # Eliminar el último elemento de la lista
                return ten_item  # Devolver el elemento eliminado
        return None  # Si no encuentra el elemento, devuelve None
    
    # Método para sacar el primer elemento (desencolar)
    def desencolar(self):
        #sum = 0
        #cuenta = 0
        for j in range (self.__nItems):  # Si la cola no está vacía
          elemnt = self.elementos  # Sacar el primer elemento
          
          self.__nItems -= 1  # Reducir el número de elementos
        print(elemnt)
        
        
    
    def tamano(self):
        return len(self.elementos)
    
    def llenar_con_aleatorios(self, cantidad):
        if cantidad <= 0 or cantidad > 10:  # Verifica que la cantidad sea válida
            raise ValueError("La cantidad debe estar entre 1 y 100.")
        
        self.elementos = random.sample(range(1, 101), cantidad)
        self.__nItems = cantidad
        
        
if __name__ == "__main__":
    pila = Cola()  # Crear una instancia de la clase Pila
    print("La pila ha sido creada.")
    pila.llenar_con_aleatorios(5)  # Llenar la pila con 5 elementos aleatorios
    print(f"Elementos en la pila: {pila.elementos}")
    print(f"Tamaño de la pila: {pila.tamano()}")
    print(f"Nuestra cola es: {pila.desencolar()} ")