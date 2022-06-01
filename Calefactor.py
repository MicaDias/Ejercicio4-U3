import abc
from abc import ABC
class Calefactor(ABC):
    __marca=''
    __modelo=''
    __costo=0
    def __init__(self,marca='',modelo=''):
        self.__marca=marca
        self.__modelo=modelo
        self.__costo=0
    @abc.abstractclassmethod
    def calcularCosto(self,cantidad,costo):
        pass
    def setCosto(self,costo):
        self.__costo=costo
    def getCosto(self):
        return self.__costo
    def __lt__(self,otro):
        resultado=False
        if isinstance(otro,Calefactor):
            resultado=self.__costo<otro.getCosto()
        return resultado
    def getMarca(self):
        return self.__marca
    def getModelo(self):
        return self.__modelo

        
    