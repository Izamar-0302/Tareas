# Crear una lista (array)
mi_array = [1, 2, 3, 4, 5]


# Acceder a un elemento
print(mi_array[0])  # Imprime: 1

# Modificar un elemento
mi_array[1] = 10
print(mi_array)  # Imprime: [1, 10, 3, 4, 5]




candinver = [""] * len(mi_array)
f=0
for j in range(len(mi_array)-1,-1,-1):

   candinver[f]=mi_array[j]
   f+=1
print(f"Cadena invertida {candinver}")
print(candinver)



   