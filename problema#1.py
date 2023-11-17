class persona:
    def iniciar(self,nom):
       self.nombre=nom

    def imprimir(self):
        print("nombre",self.nombre)

#bloque principal
persona1 = persona()
persona1.iniciar("sebastian")        
persona1.imprimir()