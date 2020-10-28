#Superclase
class Persona:
    def __init__(self, nombre):
        self.nombre=nombre
    def avanza(self):
        print(f'..................................')
        print(f'Ando caminado')
        print(f' ')

#Clase hija
class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)

#Aplicacion de polimorfimo
    def avanza(self):
        print(f'..................................')
        print(f'Ando moviendome en mi bicicleta')
        print(f' ')

#Instancia de clases    
def main():
    persona=Persona('David')
    persona.avanza()

    ciclista=Ciclista('Daniel')
    ciclista.avanza()

if __name__=='__main__':
    main()