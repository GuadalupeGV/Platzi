class Lavadora:

    def __init__(self):
        pass

    def lavar(self,temperatura='Templada'):
        self._llenar_tanque_de_agua(temperatura)
        self._anadir_jabon()
        self._lavar()
        self._centrifugar()

    def _llenar_tanque_de_agua(self,temperatura):
        print (f'.......................................................')
        print(f'El tanque se esta llenando, temperatura: {temperatura}')

    def _anadir_jabon(self):
        print (f'.......................')
        print (f'Añadiendo jabón')

    def _lavar(self):
        print (f'.......................')
        print(f'Lavado iniciado')
    
    def _centrifugar(self):
        print (f'.......................')
        print(f'Centrifugado iniciado')

if __name__ == '__main__':
    Lavadora=Lavadora()
    Lavadora.lavar()


