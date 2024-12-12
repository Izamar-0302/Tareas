class HistorialNavegador:
    def __init__(self):
        self.historial = []       # Pila principal
        self.pilaAdelante = []    # Pila auxiliar para ir hacia adelante

    def visitar(self, pagina):
        """Visita una nueva página."""
        self.historial.append(pagina)
        self.pilaAdelante.clear()  # Limpiar la pila de adelante
        print(f"Visitando: {pagina}")

    def ir_atras(self):
        """Ir a la página anterior."""
        if len(self.historial) > 1:
            pagina_actual = self.historial.pop()
            self.pilaAdelante.append(pagina_actual)
            print(f"Regresando a: {self.historial[-1]}")
        else:
            print("No puedes regresar más atrás.")

    def ir_adelante(self):
        """Ir a la página siguiente."""
        if self.pilaAdelante:
            pagina = self.pilaAdelante.pop()
            self.historial.append(pagina)
            print(f"Avanzando a: {pagina}")
        else:
            print("No hay páginas hacia adelante.")

    def mostrar_pagina_actual(self):
        """Muestra la página actual."""
        if self.historial:
            print(f"Página actual: {self.historial[-1]}")
        else:
            print("No hay páginas en el historial.")

    def mostrar_historial(self):
        """Muestra todo el historial."""
        print("Historial de navegación:")
        for pagina in self.historial:
            print(pagina)

# Ejemplo de uso
navegador = HistorialNavegador()
navegador.visitar("www.google.com")
navegador.visitar("www.youtube.com")
navegador.visitar("www.github.com")
navegador.mostrar_pagina_actual()

navegador.ir_atras()
navegador.mostrar_pagina_actual()

navegador.ir_adelante()
navegador.mostrar_pagina_actual()

navegador.mostrar_historial()
