from stack import Stack

def test_stack():
    # Crear una pila con capacidad para 3 elementos
    stack = Stack(3)
    print("Pila creada con tamaño máximo de 3.\n")

    # Intentar agregar 3 elementos y mostrar la pila
    try:
        stack.push(1)
        stack.push(2)
        stack.push(3)
        print("Estado de la pila después de agregar 3 elementos:", stack)
    except OverflowError as e:
        print(e)

    # Intentar agregar un cuarto elemento para generar una excepción
    try:
        print("\nIntentando agregar un cuarto elemento...")
        stack.push(4)
    except OverflowError as e:
        print("Excepción capturada:", e)

    # Quitar todos los elementos y mostrar la pila en cada paso
    try:
        print("\nEliminando elementos de la pila:")
        print("Elemento eliminado:", stack.pop())
        print("Elemento eliminado:", stack.pop())
        print("Elemento eliminado:", stack.pop())
        print("Estado de la pila después de eliminar todos los elementos:", stack)
    except IndexError as e:
        print(e)

    # Intentar quitar un elemento de una pila vacía para generar una excepción
    try:
        print("\nIntentando quitar un elemento de una pila vacía...")
        stack.pop()
    except IndexError as e:
        print("Excepción capturada:", e)

# Ejecutar la prueba
test_stack()