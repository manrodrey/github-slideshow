from fastapi import FastAPI
from fastapi import HTTPException

from database import User
from database import database as connection

from schemas import UserRequestModel
from  schemas import UserResponseModel

app = FastAPI(title='Primera vez',
              description='Prueba de una API',
              version='1.0.1')
# Por defecto, se crea un apartado de documentacion(/docs)

# Eventos:
@app.on_event('startup')
def startup():
    if connection.is_closed():
        connection.connect()
    # Antes de comenzar el servidor:
    connection.create_tables([User]) #Crea todas las tablas de nuestro proyecto

@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():
        connection.close()

@app.get('/') # Con esto hacemos que cuando un cliente realice una peticion a / utilizando get sera la funcion index la que respondera
async def index(): # se le pone async recomendado por fastAPI porque se ejecuta de manera asincrona
    return 'Que pasa mi gente'

@app.post('/users') # Para crear usuarios utilizamos el metodo post
async def create_user(user_request: UserRequestModel): # Asi indicamos que si un cliente quiere realizar una peticion a esta url tiene que enviar obligatoriamente los valores para crear un objeto de userRequestModel
    user = User.create(
        username=user_request.username,
        email=user_request.email
    )
    return user_request

@app.get('/users/{user_id}')
async def get_user(user_id):
    user = User.select().where(User.id == user_id).first()

    if user:
        return UserResponseModel(id=user.id,
                                 username=user.username,
                                 email=user.email)
    else:
        return HTTPException(404, 'User not found')

@app.delete('/users/{user_id}')
async def get_user(user_id):
    user = User.select().where(User.id == user_id).first()

    if user:
        user.delete_instance()
        return True
    else:
        return HTTPException(404, 'User not found')