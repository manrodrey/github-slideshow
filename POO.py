# Clase -> características comunes de un grupo de objetos
# Clases tienen Estado, Propiedades y Comportamiento
# Instancia, Objeto, Ejemplar -> ejemplar que pertenece a una clase (dos coches)
# Modularizacion -> Varias clases dentro de un programa
# Encapsulacion -> Las clases no saben del funcionamiento de las otras pero estan de alguna forma conectadas para poder funcionar como equipo

# Ya hay cambios en este, asi que a ver como se hace en github
class Coche():# Propiedades
    #Vamos a crear un constructor de la clase (lo que da un estado inicial a los objetos de la clase)
    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4 # Asi encapsulo esta propiedad y no es accesible desde fuera de la clase
        self.__en_marcha = False

    # Comportamiento -> determinado por Metodos(funciones que pertenecen a una clase)
    def arrancar(self,arrancamos): # El self actua como mi ejemplo de clase, en este caso miCoche
        self.__en_marcha=arrancamos
        if(self.__en_marcha):
            chequeo=self.__chequeo_interno()

        if (self.__en_marcha and chequeo):
            return 'El coche esta en marcha'

        elif(self.__en_marcha and chequeo==False):
            return 'Algo ha ido mal en el chequeo, no podemos arrancar'

        else:
            return 'El coche esta parado'

    def estado(self):
        print('El coche tiene',self.__ruedas,'ruedas. Un ancho de',self.__anchoChasis,'y un largo de',self.__largoChasis)

    def __chequeo_interno(self): # Hemos encapsulado el metodo
        print('Realizando chequeo interno')
        self.gasolina = 'ok'
        self.aceite = 'ok'
        self.puertas = 'cerradas'

        if(self.gasolina=='ok' and self.aceite=='ok' and self.puertas=='cerradas'):
            return True
        else:
            return False


miCoche = Coche() # Instanciar o ejemplarizar una clase (crearla)
miCoche.estado()
print(miCoche.arrancar(True))

miCoche2 = Coche()
miCoche2.estado()
print(miCoche2.arrancar(False))