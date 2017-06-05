from app import app
from flask import jsonify, request, send_file
from services.checkoutservice import *
# from services.excelservice import get_excel
from io import BytesIO
from xlsxwriter.workbook import Workbook


@app.route('/visitas/', methods=['GET'])
def getVisitas():
	visitas = check_visitas(request)
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


@app.route('/visitas/excel', methods=['GET'])
def getVisitasToExcel():
	# output = get_excel(request)
	
	visitas = check_visitas(request)
    
    # # strIO = cStringIO.StringIO()
	output = BytesIO()

	workbook = Workbook(output, {'in_memory': True})
    # # workbook = Workbook("reporte.xlsx")
	worksheet = workbook.add_worksheet()

	worksheet.write(0, 0, 'VISITANTE')
	worksheet.write(0,1, 'TIPO ID')
	worksheet.write(0,2, 'VISITANTE ID')
	worksheet.write(0,3, 'ORIGEN')
	worksheet.write(0,4, 'DESTINO')
	worksheet.write(0,5, 'VEHICULO')
	worksheet.write(0,6, 'AUTORIZADO POR')
	worksheet.write(0,7, 'SEGURIDAD EN TRUNO')
	worksheet.write(0,8, 'FECHA')
	worksheet.write(0,9, 'HORA ENTRADA')
	worksheet.write(0,10, 'HORA SALIDA')

	for num_r, rval in enumerate(visitas['rows']):
		r = int(num_r) + 1
		worksheet.write(r, 0, rval.visitante.nombre)
		worksheet.write(r, 1, rval.visitante.tipo_id)
		worksheet.write(r, 2, rval.visitante.identidad)
		worksheet.write(r, 3, rval.origen)
		worksheet.write(r, 4, rval.destino.empresa)
		worksheet.write(r, 5, rval.vehiculo.marca)
		worksheet.write(r, 6, rval.autorizada_por)
		worksheet.write(r, 7, rval.seguridad.nombre)
		worksheet.write(r, 8, str(rval.fecha.strftime("%d/%m/%Y")))
		worksheet.write(r, 9, str(rval.hora_entrada.strftime("%I:%M:%S %p")))
		worksheet.write(r, 10, str(rval.hora_salida.strftime("%I:%M:%S %p")))

	workbook.close()
	output.seek(0)
	nombre_archivo ="reporte" + str(datetime.now().strftime("%Y%m%d_%I%M%S%p")) + ".xlsx"

	return send_file(output, attachment_filename=nombre_archivo, as_attachment=True)