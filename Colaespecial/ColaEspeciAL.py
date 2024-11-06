class ColaEspecial:
    
    def __init__(self):
        self.elementos = []  # Lista que almacena los elementos
        self.__nItems = 0 # Número de elementos en la cola

    def apilar(self, elemento):
        self.elementos.append(elemento)
        self.__nItems += 1  # Aumentar el número de elementos
        
    def apilarr(self, elemento):
        if self.__nItems < 10:
         self.elementos.append(elemento)
         self.__nItems += 1  # Aumentar el número de elementos
        elif  self.__nItems > 9: # Si la cola no está vacía
          for j in range(self.__nItems):
            elemento = self.elementos.pop( self.__nItems-1)  # Sacar el primer elemento
            self.__nItems -= 1  # Reducir el número de elementos
       
     
    def apilarespe(self, elemento):
        if self.__nItems < 10:
         for j in range(self.__nItems):
           self.elementos.append(elemento)
           self.__nItems += 1  # Aumentar el número de elementos
        else:
         for j in range(self.__nItems):
           self.elementos.append(elemento)
           self.__nItems -= 1  # decrecer el número de elementos
           
    def apilarespe(self, elemento):
        if self.__nItems < 10:
         for j in range(self.__nItems):
           self.elementos.append(elemento)
           self.__nItems += 1  # Aumentar el número de elementos
        else:
         for j in range(self.__nItems):
           self.elementos.append(elemento)
           self.__nItems -= 1  # decrecer el número de elementos
            
        
    # Método para obtener el valor en un índice n
    def get(self, n):  # Retornar el valor en el índice n
        if 0 <= n < self.__nItems:  # Verificar que el índice está dentro de los límites
            return self.elementos[n]  # Retornar el elemento en la posición n
       
            # Si el índice está fuera de los límites, devolver None
        
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
        if self.__nItems > 0:  # Si la cola no está vacía
            elemnt = self.elementos.pop(0)  # Sacar el primer elemento
            self.__nItems -= 1  # Reducir el número de elementos
            return elemnt
        else:
            print("La cola está vacía.")
            return None