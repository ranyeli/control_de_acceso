from repository.visitacrud import *
from repository.destinocrud import *
#from repository.session import session


def check_visitas(params):
	visitas = get_all_visitas(params)
	return visitas


def check_destinos():
	return get_all_destinos()


def check_visita_reciente(tipo_id, identidad):
	return get_visita_reciente(tipo_id, identidad)

