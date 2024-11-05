from stack import Stack

stack = Stack(100)  # Crear una pila para almacenar letras
word = input("Palabra a invertir: ")

# Recorrer las letras en la palabra
for letter in word:
    if not stack.isFull():  # Apilar letras si la pila no está llena
        stack.push(letter)

reverse = ''  # Construir la versión invertida de la palabra

# Desapilar la pila hasta que esté vacía
while not stack.isEmpty():
    reverse += stack.pop()
    
print('La palabra', word, 'invertida es', reverse)
    
if word == reverse :
    print('La palabra si es palindromo')
else:
    print('La palabra no es palindromo')
    

