class Pila(object):
    def __init__(self, initialSize):
        self.__a = [None] * initialSize
        self.__nItems = 0
    
    def push(self, item):
        if self.__nItems < len(self.__a):  # Verificar si hay espacio en la pila
            self.__a[self.__nItems] = item
            self.__nItems += 1
        else:
            print("Error: La pila está llena.")
    
    def __str__(self):
        return f"Pila: {self.__a[:self.__nItems]}"  # Mostrar solo los elementos válidos
    
    def peek(self):
        if self.__nItems > 0:
            return self.__a[self.__nItems - 1]
        else:
            return "Pila vacía"
    
    def pop(self):
        if self.__nItems > 0:
            x = self.__a[self.__nItems - 1]
            self.__nItems -= 1
            return x
        else:
            print("Error: No se puede hacer pop en una pila vacía.")
            return None
    
    def delete(self, item):
        for i in range(self.__nItems):
            if self.__a[i] == item:
                for j in range(i, self.__nItems - 1):
                    self.__a[j] = self.__a[j + 1]
                self.__nItems -= 1
                self.__a[self.__nItems] = None  # Limpiar el último elemento
                return True
        return False
    
    def operandi(self):
        Pil = Pila(self.__nItems)  # Crear una nueva pila auxiliar

        for i in range(self.__nItems):
            elemento = self.__a[i]

            if isinstance(elemento, int) or isinstance(elemento, float):
                Pil.push(elemento)  # Empujar operandos
            else:
                try:
                    operador2 = Pil.pop()  # Desempilar operandos
                    operador1 = Pil.pop()
                    
                    # Realizar la operación según el operador
                    if elemento == '+':
                        Pil.push(operador1 + operador2)
                    elif elemento == '-':
                        Pil.push(operador1 - operador2)
                    elif elemento == '*':
                        Pil.push(operador1 * operador2)
                    elif elemento == '/':
                        if operador2 == 0:
                            print("Error: División por cero.")
                            return None
                        Pil.push(operador1 / operador2)
                    else:
                        print(f"Operador desconocido: {elemento}")
                        return None
                except TypeError:
                    print("Error: Operandos insuficientes para realizar la operación.")
                    return None

        if Pil.__nItems == 1:
            return Pil.pop()  # Retornar el resultado final
        else:
            print("Error: Expresión mal formada.")
            return None

# Crear una pila con una expresión postfija
mipila = Pila(5)
mipila.push(3)
mipila.push(4)
mipila.push('+')
mipila.push(2)
mipila.push('*')

# Evaluar la expresión
resultado = mipila.operandi()
print(mipila)
# Imprimir el resultado
if resultado is not None:
    print(f"Resultado de la operación: {resultado}")
else:
    print("No se pudo calcular el resultado.")
