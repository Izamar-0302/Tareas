# Crear una lista (array)
mi_array = [1, 2, 3, 4, 5]


# Acceder a un elemento
print(mi_array[0])  # Imprime: 1

# Modificar un elemento
mi_array[1] = 10
print(mi_array)  # Imprime: [1, 10, 3, 4, 5]

print("Dame un numero para buscarlo")
numer=int(input(""))

for i in range(len(mi_array)):
    if numer==mi_array[i]:
        print("Este numero si se encuentra en la cadena")
        break
    else:
        print("Este numero no se encuentra en la cadena")