from app import app
from flask import jsonify, request
from services.checkoutservice import *
from services.excelservice import get_excel
from io import BytesIO
from xlsxwriter.workbook import Workbook


@app.route('/visitas/', methods=['GET'])
def getVisitas():
	visitas = check_visitas(request)
	return jsonify({"total":visitas["total"], "rows":[visita.serialize for visita in visitas["rows"]]})


@app.route('/destinos/', methods=['GET'])
def getDestinos():
	destinos = check_destinos()
	json = jsonify([destino.serialize for destino in destinos]) if destinos else jsonify({})
	return json


@app.route('/visita/tipo_id/<string:tipo_id>/identidad/<string:identidad>', methods=['GET'])
def getVisita(tipo_id, identidad):
	visita = check_visita_reciente(tipo_id, identidad)
	json = jsonify(visita.serialize) if visita else jsonify({})
	return json


@app.route('/visitas/excel', methods=['GET'])
def getVisitasToExcel():
	send = get_excel(request)
	return send