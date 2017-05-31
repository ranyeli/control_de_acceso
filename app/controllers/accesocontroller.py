from app import app
from flask import render_template, redirect, url_for, request, flash, Response
from datetime import datetime
from services.annotateservice import *


@app.route('/', methods=['GET'])
#@app.route('/control')
def accessControl():
	fecha = datetime.now().date().strftime("%d/%m/%Y")
	hora = datetime.now().time().strftime("%I:%M:%S %p")
	return render_template('control_de_acceso.html', fecha=fecha, hora=hora)


@app.route('/registrar/<string:accion>',  methods=['POST'])
def registerVisit(accion):
	if accion.lower().strip() == 'entrada':
		save_visita(request)
	elif accion.lower().strip() == 'salida':
		update_salida(request)
	return redirect(url_for('accessControl'))
	

@app.route('/registrar/destino/<string:destino>', methods=['POST'])
def registroDestino(destino):
	save_destino(destino)
	return Response(response=None, status=None, headers=None, mimetype=None, content_type=None, direct_passthrough=False)