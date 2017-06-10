# -*- coding: utf-8 -*-


from datetime import datetime
from dateutil.parser import parse
from repository.generalcrud import *
from repository.visitacrud import *
from models.seguridad import Seguridad
from models.visita import Visita
from models.vehiculo import Vehiculo
from models.visitante import Visitante
from models.destino import Destino


def save_visita(request):
	f = request.form
	
	visitante = Visitante()
	visitante.nombre = f['visitanteNombre']
	visitante.apellido = f['visitanteApellido']
	visitante.identidad = f['visitanteIdentidad']
	visitante.tipo_id = f['visitanteIdTipo']
	insertdb(visitante)
	
	seguridad = Seguridad()
	seguridad.nombre = f['seguridadTurno']
	insertdb(seguridad)
	
	vehiculo = Vehiculo()
	vehiculo.marca = f['vehiculoMarca']
	vehiculo.color = f['vehiculoColor']
	vehiculo.tipo = f['vehiculoTipo']
	vehiculo.placa = f['vehiculoPlaca']
	insertdb(vehiculo)
	
	visita = Visita()
	visita.origen = f['visitaOrigen']
	visita.destino_id = f['destinoId']
	visita.razon = f['visitaRazon']
	visita.fecha = parse("-".join(f['visitaFecha'].split("/")[::-1])).date()
	visita.hora_entrada = parse(f['visitaHora']).time()
	visita.autorizada_por = f['visitaAutorizada']
	visita.seguridad_id = seguridad.id
	visita.vehiculo_id = vehiculo.id
	visita.visitante_id = visitante.id
	insertdb(visita)

def save_destino(destino):
	empresa = Destino(empresa=destino)
	insertdb(empresa)


def update_salida(params):
	actualizar_hora_salida(params)


