class historianavegacion:
     def __init__(self):
         self.historial = []
         self.paginaadelan =[]
         
     def visitado(self,pagina):
         self.historial.append(pagina)
         self.paginaadelan.clear()
         print(f'Visitando: {pagina}')
     
     def pagina_actual(self):
         if self.historial:
             print(f"Pagina actual : {self.historial[-1]}")
         else:
             print("No  hay paginas actuales")
             
     def mostraerhistorial(self):
           print("Historial  de navegacion")
           for pagina in self.historial :
              print(pagina)
             
     def ir_atras(self):
         if len(self.historial)>1:
             paginaactual = self.historial.pop()
             self.paginaadelan.append(paginaactual)
             print(f"Pagina anterior : {self.historial[-1]}")
         else:
             print(f"No puedes retroceder mas")
             
     def ir_adelan(self):
         if self.paginaadelan:
             paginaactual = self.paginaadelan.pop()
             self.historial.append(paginaactual)
             print (f"Avanzando a : {paginaactual}")
         else: 
             print ("No hay paginas adelante")
             
             
navegador = historianavegacion()
navegador.visitado("www.google.com")
navegador.visitado("www.youtube.com")
navegador.visitado("www.github.com")
navegador.pagina_actual()

navegador.ir_atras()
navegador.pagina_actual()
navegador.ir_atras()
navegador.pagina_actual()
navegador.ir_adelan()
navegador.pagina_actual()
navegador.ir_adelan()
navegador.pagina_actual()

navegador.mostraerhistorial()