from Menu import Menu
from ManejadorCalefactor import ManejaCalefactor
if __name__=='__main__':
    bandera=True
    while bandera:
        try:
            cantidad=int(input('Ingrese la cantidad de calefactores:'))
        except ValueError:
            print('ERROR: Se debe ingresar un numero entero.')
        else:
            bandera=False
    manejadorCalefactor=ManejaCalefactor(cantidad)
    menu=Menu()
    manejadorCalefactor.cargarArchivo()
    menu.lanzarMenu(manejadorCalefactor)