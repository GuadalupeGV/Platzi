class Automovil:
    #DEFINIR ATRIBUTOS    
    def __init__(self, modelo, marca, color):
        self.modelo=modelo
        self.marca=marca
        self.color=color
        self._estado='en reposo'
        self._motor=Motor(cilindros=4)
        self._rastreo='Ubicación GPS'

   #METODO  
    def acelerar(self, tipo='Despacio'):
        if tipo=='rápida':
           self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)
#CLASE MOTOR
class Motor:
    def __init__(self, cilindros,tipo='gasolina'):
        self.cilindros=cilindros
        self.tipo=tipo
        self._temperatura=0
    def inyecta_gasolina(self,cantidad):
        pass
