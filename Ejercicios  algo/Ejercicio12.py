class cola(object):
    def __init__ (self,initialsize):
        
        self.__nItems = 0
        self.caja = [None]*initialsize
        self.tickets = [None]*initialsize
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
            if self.caja[i] == item:
                self.__nItems-=1
                for j in range(i,self.__nItems):
                 self.caja[j]=self.caja[j+1]
                return True
        return False
    
    def __str__(self):
        elementos = [self.caja[i] for i in range(self.__nItems)]
        return f"Cola : {elementos}"
    
    def entrada(self,item):
        
        if self.__nItems == len(self.caja):
          x=self.caja[0]
          print(f"Cliente numero {x} ha salido")
          self.delete(x)
          
        
        self.caja[self.__nItems]=item
        
        self.__nItems +=1
        print(f"Cliente numero {item} a caja")
        
    def ultin(self):
        print(f"Cliente numero {self.caja[self.__nItems-1]} ha salido")
        
 
        
        
print("BIENVENIDO A BANCO ATLANTIDA")  
print("............................")  
print("Estado del dia")  
    
Ticket = cola(3)
print("............................") 
Ticket.entrada(1)
print("............................") 
Ticket.entrada(2)
print("............................") 
Ticket.entrada(3)
print("............................") 
Ticket.entrada(4)
print("............................") 
Ticket.entrada(5)
print("............................") 
Ticket.ultin()


