class PriorityQueue:
    def _init_(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def insert(self, item):
        # Insertar el nuevo elemento al final, lo cual es O(1)
        self.queue.append(item)
        print(f"Insertado {item}")

    def remove(self):
        if self.is_empty():
            print("La cola de prioridad está vacía")
            return None
        
        # Buscar el índice del elemento con la mayor prioridad
        # (aquí, se considera el menor valor como de mayor prioridad)
        max_index = 0
        for i in range(1, len(self.queue)):
            if self.queue[i] < self.queue[max_index]:
                max_index = i
        
        # Remover el elemento de mayor prioridad
        item = self.queue.pop(max_index)
        print(f"Removido {item} con mayor prioridad")
        return item

    def peek(self):
        if self.is_empty():
            print("La cola de prioridad está vacía")
            return None
        
        # Encontrar el elemento de mayor prioridad sin removerlo
        max_index = 0
        for i in range(1, len(self.queue)):
            if self.queue[i] < self.queue[max_index]:
                max_index = i
        print(f"Elemento de mayor prioridad: {self.queue[max_index]}")
        return self.queue[max_index]

    def display(self):
        # Mostrar la cola como una cadena
        print("Contenido de la cola de prioridad:", ' '.join(map(str, self.queue)))