from app import app
from flask import jsonify, request
from services.checkoutservice import *

@app.route('/visitas/', methods=['GET'])
def getVisitas():
	visitas = check_visitas(request)
	return jsonify({"total":len(visitas), "visitas": [visita.serialize for visita in visitas]})