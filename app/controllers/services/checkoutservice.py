from repository.visitacrud import *
#from models.menuitem import MenuItem


def check_visitas(params):
	return get_all_visitas(params)
	#tables = ", ".join(params['tables'])
	#conditions = " and ".params['conditions']
	#return filter_visita(tables, conditions)


