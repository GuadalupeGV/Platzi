#Superclase
class Rectangulo:

    def __init__(self, base, altura):
        self.base= base
        self.altura= altura

    def area(self):
        return self. base* self.altura

#Subclase
class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

 
if __name__== '__main__':

    Rectangulo=Rectangulo(base=3, altura= 4)
    print(f'.............................. ')
    print(f'El área del rectángulo es: ')
    print(Rectangulo.area())

    Cuadrado=Cuadrado(lado=5)
    print(f'.............................. ')
    print(f'El área del cuadrado es: ')
    print(Cuadrado.area())