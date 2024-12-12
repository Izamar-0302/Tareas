class Pila(object):
    def __init__(self,initialSize):
        
        self.__a = [None] * initialSize
        self.__nItems = 0
    
    def push(self,item):
     self.__a[self.__nItems]=item
     self.__nItems +=1
     
    def __str__(self):
        return f"Pila: {self.__a}"
    
    def peek(self):
        return f"Elemento tope: {self.__a[self.__nItems-1]}"
    
    def pop(self):
       x= self.__a[self.__nItems-1]
       self.delete(self.__a[self.__nItems-1])
       return f"Elemento borrado: {x}"
       
    def delete(self,item):
        for i in range(self.__nItems-1):
           if self.__a[i]==item:
               self.__nItems-=1
               for j in range(i,self._nItems):
                   self.__a[j]=self.__a[j+1]
                   return True 
        return False       
        
     
    
miPila = Pila (5)    
miPila.push(1)
miPila.push(2)
miPila.push(3)
miPila.push(4)
miPila.push(5)

print(miPila)
    
print(miPila.peek())
print(miPila.pop())