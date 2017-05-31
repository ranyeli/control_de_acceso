import sys
import os
import json
sys.path.append('../')
from sqlalchemy import create_engine
from models.base import Base
from models.visitante import Visitante
from models.visita import Visita
from models.seguridad import Seguridad
from models.vehiculo import Vehiculo
from models.destino import Destino
from datetime import datetime


with open('../config.json') as json_data_file:
    data = json_data_file.read()

os.environ['settings'] = data;
settings = json.loads(os.environ['settings'])

from controllers.services.repository.session import session
from controllers.services.repository.generalcrud import *
from sqlalchemy import text, func, or_, cast, Date, and_


ids = ["CEDULA", "LIC. DE CONDUCIR", "PASAPORTE"]
colores = ["rojo", "azul", "verde", "blanco", "negro", "amarillo", "naranja", "plateado", "rosado"]
marcas = ["toyota", "honda", "mitsubishi", "chevrolet", "cadilac", "mustan", "personalida"]
tipos = ["camion", "carro", "motor", "pasola", "fourwheel", "guagua"]
ellos = ["robinson sosa", "alex mendez", "gisela", "popeye el marino"]


destino = Destino()
destino.empresa = "aurora"
insertdb(destino)

destino = Destino()
destino.empresa = "comedor"
insertdb(destino)

destino = Destino()
destino.empresa = "hospital"
insertdb(destino)


for i in range(50):
    visitante = Visitante()
    visitante.nombre = "persona_nombre" + str(i)
    visitante.apellido = "persona_apellido" + str(i)
    visitante.identidad = "".join([str(2 + i), str((3*i)%50), str(abs(8-i)), 
                                str(i), str((i**2)%50), str(i-1), str(i+3), str(i+i)]);
    visitante.tipo_id = ids[i%3]
    insertdb(visitante)


    vehiculo = Vehiculo()
    vehiculo.color = colores[i%9]
    vehiculo.marca = marcas[i%7]
    vehiculo.tipo = tipos[i%6]
    vehiculo.placa = str(i) + str(i+3) + str(datetime.now().time().second)
    insertdb(vehiculo)

    seguridad = Seguridad()
    seguridad.nombre = "seguridad_" + str(i)
    insertdb(seguridad)

    visita = Visita()
    visita.destino_id = (i%3) + 1
    visita.seguridad_id = seguridad.id
    visita.vehiculo_id = vehiculo.id
    visita.visitante_id = visitante.id
    visita.razon = "razon_" + str(i)
    visita.origen = "sitio_" + str(i)
    visita.fecha = datetime(2017 - (i%3), (i%12)+1, (i%28) + 1).date()
    visita.hora_entrada = datetime(2017 - (i%3), (i%12)+1, (i%28) + 1, i%24, i%60, i%60).time()
    visita.hora_salida = datetime(2017 - (i%3), (i%12)+1, (i%28) + 1, (i+3)%24, i%60, i%60).time()
    visita.autorizada_por = ellos[i%4]
    insertdb(visita)



