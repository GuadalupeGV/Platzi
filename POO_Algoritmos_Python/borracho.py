import random, math
from bokeh.plotting import figure, show

class Borracho:
    def __init__(self,nombre):
        self.nombre=nombre

#Subclase, extención de la clase borracho

class BorrachoTradicional (Borracho):
    def __init__(self,nombre):
        super().__init__(nombre)

#Posibles formas de movimiento
    def camina(self):
        return random.choice([(0,1),(0,-1), (1,0),(-1,0)])        