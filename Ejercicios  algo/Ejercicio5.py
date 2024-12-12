def delete(lista, elemento):
   
    try:
        lista.remove(elemento)  # Elimina el elemento de la lista
        print(f"Elemento '{elemento}' eliminado correctamente.")
    except ValueError:
        print(f"El elemento '{elemento}' no se encuentra en la lista.")
    return lista
        
# Crear una lista (array)
mi_array = [1, 3, 3, 4, 5]


# Acceder a un elemento
print(mi_array[0])  # Imprime: 1

# Modificar un elemento

print(mi_array)  # Imprime: [1, 10, 3, 4, 5]

i=0
while i < len(mi_array):
    
    if mi_array.count(mi_array[i])>1:
            mi_array = delete(mi_array, mi_array[i])
    else:
        i+=1
    
print(mi_array)           

        


        