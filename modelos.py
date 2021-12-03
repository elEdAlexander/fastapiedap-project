from typing import List
from pydantic import BaseModel

class cliente(BaseModel):
    id:int
    correo:str
    nombre:str
    apellido:str
    rnc:str
    telefono:int

class facturadetalle(BaseModel):
    factura_id:int
    codigo:str
    nombre:str
    precio:float
    cantidad:float
    total:float

class factura(BaseModel):
    id:int
    fecha:str
    cliente_id:int
    descripcion:str
    subtotal:float
    itbis:float
    total:float
    detalle: List[facturadetalle] = []

class articulo(BaseModel):
    id:int
    codigo:str
    nombre:str
    tipo:str
    precio:int
    cantidad:int
    comentario:str
    
"""""
class usuario(BaseModel):
    id:int
    correo:str
    nombre:str
    password:str """