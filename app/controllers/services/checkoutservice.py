from repository.visitacrud import *
from repository.destinocrud import *


def check_visitas(params):
	return get_all_visitas(params)


def check_destinos():
	return get_all_destinos()


def check_visita_reciente(tipo_id, identidad):
	return get_visita_reciente(tipo_id, identidad)

