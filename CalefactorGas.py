from Calefactor import Calefactor
class CalefactorGas(Calefactor):
    __matricula=''
    __calorias=0
    def __init__(self,marca='',modelo='',matricula='',calorias=0):
        super(). __init__(marca,modelo)
        self.__matricula=matricula
        self.__calorias=calorias
    def calcularCosto(self,cantidad,costo):
        self.setCosto((self.__calorias/1000)*cantidad*costo)
    def getMatricula(self):
        return self.__matricula
    def getCalorias(self):
        return self.__calorias
        
        