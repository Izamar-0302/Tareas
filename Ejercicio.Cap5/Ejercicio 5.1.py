class LinkedList(object):
    # Se asume que __init__, getFirst(), y demás métodos están definidos.

    def traverse(self, func=print):
        """Recorre la lista aplicando una función a cada elemento."""
        for data in self:  # Itera directamente usando el generador
            func(data)

    def __len__(self):
        """Devuelve la longitud de la lista."""
        return sum(1 for _ in self)  # Cuenta el número de elementos iterados

    def __str__(self):
        """Construye una representación en cadena de la lista."""
        return "[" + " > ".join(str(data) for data in self) + "]"
