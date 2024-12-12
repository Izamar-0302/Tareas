class ColaCircular:
    def __init__(self, tamaño):
        """Inicializa la cola circular."""
        self.tamaño = tamaño
        self.cola = [None] * tamaño  
        self.front = -1  
        self.rear = -1   

    def encolar(self, elemento):
        """Agrega un elemento a la cola."""
        
        if (self.rear + 1) % self.tamaño == self.front:
            print("Cola llena. No se puede insertar.")
            return
       
        if self.front == -1:
            self.front = 0
       
        self.rear = (self.rear + 1) % self.tamaño
        self.cola[self.rear] = elemento

    def desencolar(self):
        """Elimina un elemento de la cola."""
        
        if self.front == -1:
            print("Cola vacía. No se puede eliminar.")
            return None
       
        elemento = self.cola[self.front]
        self.cola[self.front] = None  
       
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            
            self.front = (self.front + 1) % self.tamaño
        return elemento

    def mostrar(self):
        """Muestra el estado actual de la cola."""
        print("Cola:", self.cola)


cola = ColaCircular(5)

cola.encolar(10)
cola.encolar(20)
cola.encolar(30)
cola.mostrar()  

cola.desencolar()  
cola.mostrar()  

cola.encolar(40)
cola.encolar(50)
cola.encolar(60)  
cola.mostrar()  
