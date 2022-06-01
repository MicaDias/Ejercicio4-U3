from Calefactor import Calefactor
class CalefactorElectrico(Calefactor):
    __potenciaMaxima=0
    
    def __init__(self,marca='',modelo='',potenciaMaxima=0):
        super(). __init__(marca,modelo)
        self.__potenciaMaxima=potenciaMaxima
    def calcularCosto(self,cantidad,costo):
        self.setCosto((self.__potenciaMaxima/1000)*cantidad*costo)
    def getPotencia(self):
        return self.__potenciaMaxima
