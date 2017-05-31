from app import app
from flask import jsonify, request
from services.checkoutservice import *

@app.route('/visitas/', methods=['GET'])
def getVisitas():
	visitas = check_visitas(request)
	#for row in visitas:
    #		print str(row.hora_visita)
	#jsonify({"total":len(visitas), "visitas": [visita.serialize for visita in visitas]})
	#jsonify({"total":len(visitas), "rows":[visita.serialize for visita in visitas]})
	#jsonify([visita.serialize for visita in visitas])
	return jsonify({"total":visitas["total"], "rows":[visita.serialize for visita in visitas["rows"]]})


@app.route('/destinos/', methods=['GET'])
def getDestinos():
	destinos = check_destinos()
	return jsonify([destino.serialize for destino in destinos])


@app.route('/visita/tipo_id/<string:tipo_id>/identidad/<string:identidad>', methods=['GET'])
def getVisita(tipo_id, identidad):
	print tipo_id, identidad
	visita = check_visita_reciente(tipo_id, identidad)
	return jsonify(visita.serialize)