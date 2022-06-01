class Menu:
    __opciones={}
    def __init__(self):
        self.__opciones={
            1:self.opcion1,
            2:self.opcion2,
            3:self.opcion3,
            4:self.salir
        }
    def lanzarMenu(self,manejador):
        #Menu opciones
        i=len(self.__opciones)
        opcion=0
        while(i!=opcion):
            print('Menu:')
            print('-Ingrese 1: Mostrar el calefactor a gas natural de menor costo de consumo.')
            print('-Ingrese 2: Mostrar el calefactor electrico  de menor costo de consumo.')
            print('-Ingrese 3: Mostrar calefactores de menor costo de  consumo.')
            print('-Ingrese 4 para salir.')
            opcion=self.cargarNumeroEntero('Ingrese opcion:\n')
            ejecutar=self.__opciones.get(opcion,self.error)
            if opcion==1:
                ejecutar(manejador)
            elif opcion==2:
                ejecutar(manejador)
            elif opcion==3:
                ejecutar(manejador)
            else:
                ejecutar()
    def opcion1(self,manejador):
        print('Ingrese la cantidad que se estima consumir en m^3.')
        cantidad=self.cargarNumeroEntero()
        print('Ingrese el costo que se estima consumir en m^3.')
        costo=self.cargarNumeroFlotante()
        manejador.verificarMenorCalefactorGas(cantidad,costo)
    def opcion2(self,manejador):
        print('Ingrese la cantidad que se estima consumir.')
        cantidad=self.cargarNumeroEntero()
        print('Ingrese el costo que se estima consumir en kilowhatt.')
        costo=self.cargarNumeroFlotante()
        manejador.verificarMenorCalefactorElectrico(cantidad,costo)
    def opcion3(self,manejador):
        print('Ingrese la cantidad que se estima consumir en m^3.')
        cantidad=self.cargarNumeroEntero()
        print('Ingrese el costo que se estima consumir en m^3.')
        costo=self.cargarNumeroFlotante()
        manejador.verificarCalefactorGas(cantidad,costo)
        print('Ingrese la cantidad que se estima consumir.')
        cantidad=self.cargarNumeroEntero()
        print('Ingrese el costo que se estima consumir en kilowhatt.')
        costo=self.cargarNumeroFlotante()
        manejador.verificarCalefactorElectrico(cantidad,costo)
        manejador.menorConsumo()
       
    def cargarNumeroFlotante(self,mensaje='Ingrese valor:'):
        numero=None
        bandera=True
        while bandera:
            try:
                numero=float(input(mensaje))
            except ValueError:
                print('ERROR: Se debe ingresar un numero con punto (.), por ejemplo: 10.50')
            else:
                bandera=False
        return numero
    def cargarNumeroEntero(self,mensaje='Ingrese valor:'):
        numero=None
        bandera=True
        while bandera:
            try:
                numero=int(input(mensaje))
            except ValueError:
                print('ERROR: Se debe ingresar un numero entero.')
            else:
                bandera=False
        return numero
    def error(self):
        #Mensaje cuando ingresa opcion incorrecta
        print('Opción incorrecta')
    def salir(self):
        #Mensaje cuando decide salir
        print('Se cerro el menú')