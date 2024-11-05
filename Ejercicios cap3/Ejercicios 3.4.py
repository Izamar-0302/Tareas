class Array(object):
    def __init__(self, initialSize):  # Constructor
        self.__a = [None] * initialSize  # El array almacenado como lista
        self.__nItems = 0  # Sin elementos en el array inicialmente

    # Otros métodos aquí...

    # Método oddEvenSort para ordenar la lista utilizando el método de ordenación impar-par
    def oddEvenSort(self):
        is_sorted = False  # Indicador de si la lista está ordenada
        pass_count = 0  # Contador de pases (pares impar y par) necesarios para ordenar

        while not is_sorted:
            is_sorted = True  # Asumimos que está ordenado hasta que encontremos un intercambio

            # Pasada impar (pares en posiciones impares: 1, 3, 5, ...)
            for i in range(1, self.__nItems - 1, 2):
                if self.__a[i] > self.__a[i + 1]:  # Si están fuera de orden, intercambiamos
                    self.swap(i, i + 1)
                    is_sorted = False

            # Pasada par (pares en posiciones pares: 0, 2, 4, ...)
            for i in range(0, self.__nItems - 1, 2):
                if self.__a[i] > self.__a[i + 1]:  # Si están fuera de orden, intercambiamos
                    self.swap(i, i + 1)
                    is_sorted = False

            pass_count += 1  # Incrementamos el número de pases

        print(f"Número de pases realizados: {pass_count}")

    # Métodos auxiliares como swap, insert, etc.

# Ejemplo de prueba
if __name__ == "__main__":
    array = Array(10)
    # Insertamos algunos datos no ordenados
    import random
    for _ in range(10):
        array.insert(random.randint(1, 100))

    print("Arreglo antes de ordenar:", array)
    array.oddEvenSort()
    print("Arreglo después de ordenar:", array)