class BinaryTree:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def combine(self, operator, left_tree, right_tree):
        """Crea un árbol combinando un operador con dos árboles existentes."""
        self.value = operator
        self.left = left_tree
        self.right = right_tree

    def inorder(self):
        """Devuelve la representación en orden con paréntesis para operadores."""
        if self.left is None and self.right is None:  # Nodo hoja
            return str(self.value)
        return f"({self.left.inorder()} {self.value} {self.right.inorder()})"

    def preorder(self):
        """Devuelve la representación en preorden."""
        if self.left is None and self.right is None:  # Nodo hoja
            return str(self.value)
        return f"{self.value} {self.left.preorder()} {self.right.preorder()}"

    def postorder(self):
        """Devuelve la representación en postorden."""
        if self.left is None and self.right is None:  # Nodo hoja
            return str(self.value)
        return f"{self.left.postorder()} {self.right.postorder()} {self.value}"
    
    def build_expression_tree(postfix_expression):
     stack = []
     operators = {'+', '-', '*', '/'}
    
     for token in postfix_expression.split():
        if token.isnumeric() or token.isalpha():  # Operando
            stack.append(BinaryTree(token))
        elif token in operators:  # Operador
            if len(stack) < 2:
                raise ValueError(f"Expresión inválida: falta operandos para '{token}'")
            right_tree = stack.pop()
            left_tree = stack.pop()
            new_tree = BinaryTree()
            new_tree.combine(token, left_tree, right_tree)
            stack.append(new_tree)
        else:
            raise ValueError(f"Expresión inválida: token no reconocido '{token}'")

     if len(stack) != 1:
         raise ValueError("Expresión inválida: más de un árbol resultante")
    
     return stack.pop()
 
def test_expressions():
    expressions = {
        "a": "91 95 + 15 + 19 + 4 *",
        "b": "B B * A C 4 * * -",
        "c": "42",
        "d": "A 57",  # Esto debería lanzar una excepción
        "e": "+ /",  # Esto debería lanzar una excepción
    }

    for key, expr in expressions.items():
        print(f"\nExpresión {key}: {expr}")
        try:
            tree =BinaryTree.build_expression_tree(expr)
            print(f"Inorden: {tree.inorder()}")
            print(f"Preorden: {tree.preorder()}")
            print(f"Postorden: {tree.postorder()}")
        except ValueError as e:
            print(f"Error: {e}")
            
test_expressions()