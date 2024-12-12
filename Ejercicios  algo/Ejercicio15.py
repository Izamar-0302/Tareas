class cola(object):
    def __init__ (self,initialsize):
        self.__a = [None]*initialsize
        self.__nItems = 0
        self.mayores=[None]*initialsize
        self.menores=[None]*initialsize
        
    def enqueue(self,item):
        self.__a[self.__nItems]=item
        self.__nItems += 1
        
    def peek(self):
        if self.__nItems  > 0:
            return self.__a[0]
     
    def dequeue(self):
        if  self.__nItems >0:
            x = self.__a[0]
            self.delete(x)
            print( f"Elemento borrado: {x}")
                
    def delete(self,item):
        for i in range(self.__nItems):
            if self.__a[i] == item:
                self.__nItems-=1
                for j in range(i,self.__nItems):
                 self.__a[j]=self.__a[j+1]
                return True
        return False
    
    def __str__(self):
        elementos = [self.__a[i] for i in range(self.__nItems)]
        return f"Cola : {elementos}"
    
    def is_empty(self):
        """Verificar si la cola está vacía."""
        return len(self.__a) == 0
    
    def ordenarcola(self):
        
         
       """Ordenar la cola en orden decreciente utilizando solo enqueue y dequeue."""
       temp_cola = cola(len(self.__a))

       while not self.is_empty():
         item = self.dequeue()  # Sacamos un elemento de la cola original

        # Mover todos los elementos de la cola auxiliar hasta que el elemento sea menor
         while not temp_cola.is_empty() and temp_cola.peek() is not None and temp_cola.peek() > item:
               self.enqueue(temp_cola.dequeue())  # Volvemos a meter en la cola original

         # Insertamos el elemento en la cola auxiliar
         temp_cola.enqueue(item)

       # Copiar los elementos ordenados de la cola auxiliar de vuelta a la cola original
       while not temp_cola.is_empty():
          self.enqueue(temp_cola.dequeue())

       return cola
        
        

colita = cola(5)
colita.enqueue(1)
colita.enqueue(2)
colita.enqueue(3)
colita.enqueue(4)
colita.enqueue(5)
print(f"Nuestra cola: {colita}")
colita.ordenarcola()