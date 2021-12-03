from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from modelos import *
import database
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def inicio():
    return {"Mensaje":"tarea8"}

#Apartado de cliente-------------------------
@app.post("/clientes/agregar", tags=['Cliente'])
def agregar_clientes(cli:cliente):
    database.guardarcliente(cli)
    return {"masg":"Datos guardados"}

@app.put("/clientes/actualizar", tags=['Cliente'])
def actualizar_clientes(cli:cliente):
    database.actualizarcliente(cli)
    return {"masg":"Datos actualizados"}

@app.get("/clientes/lista", tags=['Cliente'])
def lista_clientes():
    tmp = database.cargarclientes()
    return tmp

@app.delete("/clientes/eliminar", tags=['Cliente'])
def eliminar_clientes(num:int):
    database.eliminarcliente(num)
    return {"masg":"Datos eliminados"}
#---------------------------------------------  


#Apartado de factura-------------------------
@app.post("/facturas/agregar", tags=['Factura'])
def agregar_facturas(fac:factura):
    database.guardarfactura(fac)
    return {"masg":"Datos guardados " }

@app.put("/facturas/actualizar", tags=['Factura'])
def actualizar_facturas(fac:factura):
    database.actualizarfactura(fac)
    return {"masg":"Datos actualizados"}

@app.get("/facturas/lista", tags=['Factura'])
def lista_facturas():
    tmp = database.cargarfacturas()
    return tmp

@app.get("/facturasdetalles/lista", tags=['Factura'])
def lista_facturas():
    tmp = database.cargarfacturasdetalles()
    return tmp

@app.delete("/facturas/eliminar", tags=['Factura'])
def eliminar_facturas(num:int):
    database.eliminarfactura(num)
    database.eliminarfacturadetalle(num)
    return {"masg":"Datos eliminados"}
#---------------------------------------------  


#Apartado de articulo-------------------------
@app.post("/articulos/agregar", tags=['Articulo'])
def agregar_articulos(art:articulo):
    database.guardararticulo(art)
    return {"masg":"Datos guardados"}

@app.put("/articulos/actualizar", tags=['Articulo'])
def actualizar_articulos(art:articulo):
    database.actualizararticulo(art)
    return {"masg":"Datos actualizados"}

@app.get("/articulos/lista", tags=['Articulo'])
def lista_articulos():
    tmpa = database.cargararticulo()
    return tmpa

@app.delete("/articulos/eliminar", tags=['Articulo'])
def eliminar_articulos(num:int):
    database.eliminararticulo(num)
    return {"masg":"Datos eliminados"}
#---------------------------------------------  
"""
#Apartado de usuario-------------------------
@app.post("/usuarios/agregar", tags=['Usuario'])
def agregar_usuarios(usu:usuario):
    database.guardarusuario(usu)
    return {"masg":"Datos guardados"}

@app.put("/usuarios/actualizar", tags=['Usuario'])
def actualizar_usuarios(usu:usuario):
    database.actualizarusuario(usu)
    return {"masg":"Datos actualizados"}

@app.get("/usuarios/lista", tags=['Usuario'])
def lista_usuarios():
    tmpa = database.cargarusuario()
    return tmpa
#---------------------------------------------  
"""