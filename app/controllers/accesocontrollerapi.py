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