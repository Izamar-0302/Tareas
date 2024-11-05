import random
class Pila:
    def __init__(self):
        self.elementos = []

    def esta_vacia(self):
        return len(self.elementos) == 0

    def apilar(self, elemento):
        self.elementos.append(elemento)

    def desapilar(self):
        if self.esta_vacia():
            raise IndexError("Desapilar de una pila vacía")
        return self.elementos.pop()

    def ver_cima(self):
        if self.esta_vacia():
            raise IndexError("La pila está vacía")
        return self.elementos[-1]

    def tamano(self):
        return len(self.elementos)

    def llenar_con_aleatorios(self, cantidad):
        self.elementos = random.sample(range(1, 101), cantidad)