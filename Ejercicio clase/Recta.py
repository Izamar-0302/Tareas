
class Rectangulo():
    def __init__(self, ancho, alto):
        self.__ancho = ancho
        self.__alto = alto
       
        

    def getArea(self):
        return self.__ancho * self.__alto
   
    def getPerimetro(self):
        return 2 * (self.__ancho + self.__alto)
    
    def setAncho(self, nuevo_ancho):
        self.__ancho = nuevo_ancho
    
    def compararCon(self, otro_rectangulo):
        if self.getArea() > otro_rectangulo.getArea():
            return " Este rectángulo es más grande."
        elif self.getArea() < otro_rectangulo.getArea():
            return "El otro rectángulo es más grande."
        else:
            return "Ambos rectángulos tienen el mismo tamaño."  
        
    def compararaltu(self, otro__rectangulo):
        if self.__alto > otro__rectangulo.__alto :
            return "Este rectangulo es mas alto"
        elif self.__alto < otro__rectangulo.__alto:
            return "El otro rectangulo es mas alto"
        else:
            return "Ambos rectángulos tienen el mismo tamaño."  
        
    def u(rectangulo, rectangulo1):
        if rectangulo.__alto > rectangulo1.__alto :
            return "Este rectangulo es mas alto"
        elif rectangulo.__alto < rectangulo1.__alto:
            return "El otro rectangulo es mas alto"
        else:
            return "Ambos rectángulos tienen el mismo alto."  
        
        
        