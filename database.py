from re import template
from peewee import *
from modelos import *

db = SqliteDatabase('tarea8.db')


class cliente(Model):
    correo = CharField()
    nombre = CharField()
    apellido = CharField()
    rnc = CharField()
    telefono = CharField()

    class Meta:
        database = db

class factura(Model):
    fecha = TextField()
    cliente_id = IntegerField()
    descripcion = TextField()
    subtotal = DoubleField()
    itbis = DoubleField()
    total = DoubleField()
    detalle: List[facturadetalle] = []

    class Meta:
        database = db

class facturadetalle(Model):
    factura_id = ForeignKeyField(factura, backref='detalle')
    codigo = TextField()
    nombre = TextField()
    precio = FloatField()
    cantidad = FloatField()
    total = FloatField()

    class Meta:
        database = db

class articulo(Model):
    codigo = CharField()
    nombre = CharField()
    tipo = CharField()
    precio = CharField()
    cantidad = CharField()
    comentario = CharField()

    class Meta:
        database = db
"""
class usuario(Model):
    correo = CharField()
    nombre = CharField()
    password = CharField()

    class Meta:
        database = db
"""
db.connect()

db.create_tables([cliente, factura, articulo, facturadetalle])

##cliente-----------------------------------------
def guardarcliente(obj:cliente):
    cli = cliente()
    cli.correo = obj.correo
    cli.nombre = obj.nombre
    cli.apellido = obj.apellido
    cli.rnc = obj.rnc
    cli.telefono = obj.telefono
    cli.save()

def cargarclientes():
    clientes = []
    for cli in cliente.select().dicts():
        clientes.append(cli)
    return clientes

def actualizarcliente(obj:cliente):
    cli = cliente.get(cliente.id == obj.id)
    cli.correo = obj.correo
    cli.nombre = obj.nombre
    cli.apellido = obj.apellido
    cli.rnc = obj.rnc
    cli.telefono = obj.telefono
    cli.save()

def eliminarcliente(cli):
    user = cliente.get(cliente.id == cli)
    user.delete_instance() 
        
##cliente-----------------------------------------

##factura-----------------------------------------
def guardarfactura(obj:factura):
    fac = factura()
    fac.fecha = obj.fecha
    fac.cliente_id = obj.cliente_id
    fac.descripcion = obj.descripcion
    fac.subtotal = obj.subtotal
    fac.itbis = obj.itbis
    fac.total = obj.total
    fac.save()

    for dett in obj.detalle:
        det = facturadetalle()
        det.factura_id = fac
        det.codigo = dett.codigo
        det.nombre = dett.nombre
        det.precio = dett.precio
        det.cantidad = dett.cantidad
        det.total = dett.total
        det.save()

def cargarfacturas():
    facturas = []
    for fac in factura.select().dicts():
        facturas.append(fac)
    return facturas

def cargarfacturasdetalles():
    facturas = []
    for facd in facturadetalle.select().dicts():
        facturas.append(facd) 
    return facturas

def actualizarfactura(obj:factura):
    fac = factura.get(factura.id == obj.id)
    fac.fecha = obj.fecha
    fac.cliente_id = obj.cliente_id
    fac.descripcion = obj.descripcion
    fac.subtotal = obj.subtotal
    fac.itbis = obj.itbis
    fac.total = obj.total
    fac.usuario = obj.usuario
    fac.save()

    for fact in obj.detalle:
        det = facturadetalle.get(facturadetalle.id == obj.id)
        det.codigo = fact.codigo
        det.nombre = fact.nombre
        det.precio = fact.precio
        det.cantidad = fact.cantidad
        det.total = fact.total
        det.save()

def eliminarfactura(fac):  
    user =  factura.get(factura.id == fac)
    user.delete_instance() 

def eliminarfacturadetalle(fac):
    qry=facturadetalle.delete().where (facturadetalle.factura_id==fac)
    qry.execute()



##factura-----------------------------------------

##articulo-----------------------------------------
def guardararticulo(obj:articulo):
    art = articulo()
    art.codigo = obj.codigo
    art.nombre = obj.nombre
    art.tipo = obj.tipo
    art.precio = obj.precio
    art.cantidad = obj.cantidad
    art.comentario = obj.comentario
    art.save()


def cargararticulo():
    articulos = []
    for art in articulo.select().dicts():
        articulos.append(art)
    return articulos

def actualizararticulo(obj:articulo):
    art = articulo.get(articulo.id == obj.id)
    art.codigo = obj.codigo
    art.nombre = obj.nombre
    art.tipo = obj.tipo
    art.precio = obj.precio
    art.cantidad = obj.cantidad
    art.comentario = obj.comentario
    art.save()

def eliminararticulo(art):
    user = articulo.get(articulo.id == art)
    user.delete_instance()
##articulo-----------------------------------------
"""
##usuario-----------------------------------------
def guardarusuario(obj:usuario):
    usu = usuario()
    usu.correo = obj.correo
    usu.nombre = obj.nombre
    usu.password = obj.password
    usu.save()

def cargarusuario():
    usuarios = []
    for usu in usuario.select().dicts():
        usuarios.append(usu)
    return usuarios

def actualizarusuario(obj:usuario):
    usu = usuario.get(usuario.id == obj.id)
    usu.correo = obj.correo
    usu.nombre = obj.nombre
    usu.password = obj.password
    usu.save()

def eliminarusuario(num:usuario):
    user = usuario.get(usuario.id == usuario.id)
    user.delete_instance()
##usuario-----------------------------------------
"""
