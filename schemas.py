# Aqui vamos a incluir las validaciones

from typing import Optional
from pydantic import BaseModel

class UserRequestModel(BaseModel): # Por defecto son requeridos pero podemos hacerlos opcionales
    username: str
    email: Optional[str] = None # Con esto solo no valdria, en la base de datos tiene que admitir nulos

class UserResponseModel(UserRequestModel): # Esto nos permitira responder al cliente a traves de un usuario
    id: int

