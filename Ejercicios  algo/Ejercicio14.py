
class cola(object):
    def __init__ (self,initialsize):
        self.__a = [None]*initialsize
        self.__nItems = 0
        self.__Items = 0
        self.impar = [None]*initialsize
        
    def enqueue(self,item):
        self.__a[self.__nItems]=item
        self.__nItems += 1
        
    def peek(self):
        if self.__nItems  > 0:
            print (f"Nuestro elemento 1 es : {self.__a[0]}")
        else:
            print("Esta vacio")
            
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
    
    def pareimpar(self,item):
         if item % 2==0:
            self.enqueue(item)
         else:
            self.impar[self.__Items]=item
            self.__Items += 1
        
        
    def resultado(self):
        
        impares_validos = [x for x in self.impar if x is not None]
        
        resultado = self.__a[:self.__nItems] + impares_validos
        print( f"Nuestras cola dividida entre par e impares seria {resultado}") 
    
cola = cola (6)
cola.pareimpar(1)
cola.pareimpar(2)
cola.pareimpar(3)
cola.pareimpar(4)
cola.pareimpar(5)
cola.pareimpar(6)

cola.resultado()