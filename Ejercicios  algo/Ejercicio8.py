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
       return x
       
    def delete(self,item):
        for i in range(self.__nItems-1):
           if self.__a[i]==item:
               self.__nItems-=1
               for j in range(i,self.__nItems):
                   self.__a[j]=self.__a[j+1]
                   return True 
        return False       
        
    def revercadena(self):
        Pil2 = Pila(self.__nItems)
        
        for i in range(self.__nItems):
          y = self.pop()
          self.__nItems-=1
          Pil2.push(y)
        return  f"Pila reversa: {Pil2}"
          
miPila1 = Pila(5)   

miPila1.push(1)
miPila1.push(2)
miPila1.push(3)
miPila1.push(4)
miPila1.push(5)

print(f"Pila 1: {miPila1}")

      
print(f"{miPila1.revercadena()}")
