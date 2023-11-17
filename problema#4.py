class Triangulo:
    def iniciar(self,L1,L2,L3):
        self.lado1=L1
        self.lado2=L2
        self.lado3=L3

    def imprimir(self):
        print("lado1",self.lado1)
        print("lado2",self.lado2)
        print("lado3",self.lado3)

    def lm(self):
        if self.lado1 > self.lado2 and self.lado2 > self.lado3:
            print(self.lado1)
        else:
            if self.lado2 > self.lado3:
                print(self.lado2)
            else:
                print(self.lado3)

    def equilatero(self):
        if self.lado1 == self.lado2 and self.lado1 == self.lado3:
            print("tu triangulo es equilatero") 
        else:
            print("no es equilatero") 
#bloque principal
triangulo1 = Triangulo()
triangulo1.iniciar(12,12,11)
triangulo1.imprimir()
triangulo1.lm()
triangulo1.equilatero()
