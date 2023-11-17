class alumno:

    def inicializar(self,nom,nota):
        self.nom = nom
        self.nota = nota

    def imprimir(self):
        print("nombre: ",self.nom)
        print("nota: ",self.nota)

    def regular(self):
        if self.nota>=4:
            print("tu nota es regular")
        else:
            print("tu nota no es regular") 

alumno1= alumno()
alumno1.inicializar("Sebastian", 5)
alumno1.imprimir()
alumno1.regular()