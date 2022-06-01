import csv
import numpy as np
from Calefactor import Calefactor
from CalefactorElectrico import CalefactorElectrico
from CalefactorGas import CalefactorGas
class ManejaCalefactor:
    __cantidad=0
    __dimension=0
    __incremento=0
    __arregloCalefactores=None

    def __init__(self,dimension=0,incremento=5):
        self.__arregloCalefactores=np.empty(dimension,dtype=Calefactor)
        self.__cantidad=0
        self.__dimension=dimension
        self.__incremento=incremento
    def agregarCalefactor(self,calefactor):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.redimensionar()
        self.__arregloCalefactores[self.__cantidad]=calefactor
        self.__cantidad+=1
    def redimensionar(self):
        self.__arregloCalefactores.resize(self.__dimension)
    def cargarArchivo(self):
        archivo=open('calefactor-electrico.csv',encoding='utf-8')
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        for fila in reader:
            if bandera:
                bandera=not bandera
            else:
                self.agregarCalefactor(CalefactorElectrico(fila[0],fila[1],int(fila[2])))
        archivo.close()
        archivo=open('calefactor-a-gas.csv',encoding='utf-8')
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        for fila in reader:
            if bandera:
                bandera=not bandera
            else:
                self.agregarCalefactor(CalefactorGas(fila[0],fila[1],fila[2],int(fila[3])))
        archivo.close()
        self.verificarDimension()
    def verificarDimension(self):
        if self.__dimension!=self.__cantidad:
            self.__dimension=self.__cantidad
            self.redimensionar()
    def verificarCalefactorGas(self,cantidad,costo):
        for i in range(self.__cantidad):
            if type(self.__arregloCalefactores[i])==CalefactorGas:
                self.__arregloCalefactores[i].calcularCosto(cantidad,costo)
    def verificarMenorCalefactorGas(self,cantidad,costo):
        self.verificarCalefactorGas(cantidad,costo)
        menor=None
        bandera=True
        for i in range(self.__cantidad):
            if type(self.__arregloCalefactores[i])==CalefactorGas:
                if bandera:
                    menor=i
                    bandera=False
                else:
                    if self.__arregloCalefactores[i]<self.__arregloCalefactores[menor]:
                        menor=i
        if menor!=None:
            print('{},{}'.format(self.__arregloCalefactores[menor].getMarca(),self.__arregloCalefactores[menor].getModelo()))
    def verificarCalefactorElectrico(self,cantidad,costo):
        for i in range(self.__cantidad):
            if type(self.__arregloCalefactores[i])==CalefactorElectrico:
                self.__arregloCalefactores[i].calcularCosto(cantidad,costo)
    def verificarMenorCalefactorElectrico(self,cantidad,costo):
        self.verificarCalefactorElectrico(cantidad,costo)
        menor=None
        bandera=True
        for i in range(self.__cantidad):
            if type(self.__arregloCalefactores[i])==CalefactorElectrico:
                if bandera:
                    menor=i
                    bandera=False
                else:
                    if self.__arregloCalefactores[i]<self.__arregloCalefactores[menor]:
                        menor=i
        if menor!=None:
            print('{},{}'.format(self.__arregloCalefactores[menor].getMarca(),self.__arregloCalefactores[menor].getModelo()))
    def menorConsumo(self):
        menor=0
        for i in range(self.__cantidad):
            if self.__arregloCalefactores[i]<self.__arregloCalefactores[menor]:
                menor=i
        if type(self.__arregloCalefactores[menor])==CalefactorElectrico:
            print("{},{},{},{}".format('Calefactor electrico',self.__arregloCalefactores[menor].getMarca(),self.__arregloCalefactores[menor].getModelo(),self.__arregloCalefactores[menor].getPotencia()))
        else:
            print('{},{},{},{}'.format('Calefactor a gas',self.__arregloCalefactores[menor].getMarca(),self.__arregloCalefactores[menor].getModelo(),self.__arregloCalefactores[menor].getMatricula(),self.__arregloCalefactores[menor].getCalorias()))