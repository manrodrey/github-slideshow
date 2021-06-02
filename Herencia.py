class vehiculos():


    def __init__(self,marca,modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):

        self.enmarcha = True

    def acelera(self):
        self.acelera = True

    def frena(self):
        self.frena = True

    def estado(self):
        print('Marca: ', self.marca, '\nModelo: ', self.modelo, '\nEn Marcha: ', self.enmarcha, '\nAcelera: ', self.acelera, '\nFrena: ', self.frena)

class Furgoneta(vehiculos):

    def carga(self, carga):
        self.cargado = carga
        if(self.cargado):
            return 'La furgoneta esta cargada'
        else:
            return 'La furgoneta no esta cargada'

class Moto(vehiculos): # asi nuestra clase moto hereda de vehiculos
    hcaballito = ''
    def cabaliito(self):
        self.hcaballito = 'Voy haciendo el caballito'

    def estado(self):
        print('Marca: ', self.marca, '\nModelo: ', self.modelo, '\nEn Marcha: ', self.enmarcha, '\nAcelera: ', self.acelera, '\nFrena: ', self.frena, '\n', self.hcaballito)
        # Al poner un comportamiento dentro de la clase que tiene el mismo nombre que la clase de la que hereda, cuando lo llamamos, a cual va? Al hijo porque se sobreescribe el de la clase padre

class Velectrico():
    def __init__(self):
        self.autonomia = 100

    def cargarEnergia(self):
        self.cargando = True


miMoto = Moto('Honda','CBR')# Hay que pasar marca y modelo porque hereda de vehiculo y es necesario para que funcione
miMoto.cabaliito()
miMoto.estado()

miFurgoneta = Furgoneta('Mercedes','Viano')
miFurgoneta.estado()

class bicicletaElectrica(vehiculos,Velectrico): #Herencia multiple que hereda de vehiculos y de v electricos
# Se da preferencia a la primera clase que indique al heredar
    pass

miBici = bicicletaElectrica('Xiaomi','1000')





