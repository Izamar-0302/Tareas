# Crear una lista (array)
mi_array = [1, 2, 3, 4, 5]

# Acceder a un elemento
print(mi_array[0])  # Imprime: 1

# Modificar un elemento
mi_array[1] = 10
print(mi_array)  # Imprime: [1, 10, 3, 4, 5]

x=0
for i in range(len(mi_array)):
   x+= mi_array[i]    
print (x)

max=mi_array[0]
min=mi_array[0]

for i in range(len(mi_array)):
   
    if mi_array[i]>max:
      max = mi_array[i]
    
    if mi_array[i]<min:
      min = mi_array[i]
      
print("El valor máximo es:", max , "El valor minimo es:", min)

   
