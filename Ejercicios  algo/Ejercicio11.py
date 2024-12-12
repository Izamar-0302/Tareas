class cola(object):
    def __init__ (self,initialsize):
        self.__a = [None]*initialsize
        self.__nItems = 0
        
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
colita = cola(5)
colita.enqueue(1)
colita.enqueue(2)
colita.enqueue(3)
colita.enqueue(4)
colita.enqueue(5)

print(colita)
colita.peek()
colita.dequeue()
print(colita)