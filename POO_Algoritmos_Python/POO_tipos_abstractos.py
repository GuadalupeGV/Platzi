#Nombre de la clase

class Coordenada:

#Definimos variables
    def __init__(self, x, y):
#Inicialización de variables
       self.x=x
       self.y=y

#Metodo
    def distancia(self, otra_coordenada):
        x_diff =(self.x - otra_coordenada.x)**2
        y_diff=(self.y-otra_coordenada.y)**2

        return (x_diff + y_diff)**0.5

#Inicializar programa
if __name__ ==  '__main__':
    coord_1 = Coordenada(3,30)
    coord_2 = Coordenada(4,8)

    print('.........................')
    print(coord_1.distancia(coord_2))
    print('.........................')

#Determinar si una coordena es intancia de Coordenada 
    print(isinstance(coord_1,Coordenada))       