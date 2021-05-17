from peewee import *

database = MySQLDatabase(
    'Aqui va el nombre de la base de datos a la que me conecto',
    user='root', password='escribir la contraseña',
    host='localhost', port=3306
)

class User(Model):
    username = CharField(max_length=50, unique=True)
    email = CharField(max_length=50)

    def __str__(self):
        return self.username

    class Meta:
        database = database
        table_name = 'users' # Esto es para sobreescribir lo creado por defecto que lo hace en singular
