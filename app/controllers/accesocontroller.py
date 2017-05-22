from app import app
from flask import render_template, redirect, url_for, request, flash
from datetime import datetime
from services.annotateservice import *


@app.route('/', methods=['GET'])
#@app.route('/control')
def accessControl():
	fecha = datetime.now().date().strftime("%d/%m/%Y")
	hora = datetime.now().time().strftime("%I:%M:%S %p")
	return render_template('control_de_acceso.html', fecha=fecha, hora=hora)

@app.route('/registrar',  methods=['POST'])
def registerVisit():
	save_visita(request)
	return redirect(url_for('accessControl'))
	
#@app.route('/consultar')
#def consultVisits():
#	pass