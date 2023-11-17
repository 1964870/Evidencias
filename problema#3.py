class Mayor_edad:
    def inicializar(self,nom,edad):
        self.nom = nom
        self.edad = edad

    def imprimir(self):
        print("nombre: ",self.nom)
        print("edad: ",self.edad)

    def M_edad(self):
        if self.edad >=18:
            print("eres mayor de edad")
        else:
            print("eres menor de edad")
#bloque principal
persona1 = Mayor_edad()
persona1.inicializar("sebastian",19)
persona1.imprimir()
persona1.M_edad()