from repository.visitacrud import get_all_visitas
from io import BytesIO
from xlsxwriter.workbook import Workbook
from datetime import datetime
from flask import send_file


def get_excel(params):
    visitas = get_all_visitas(params)
    
    output = BytesIO()

    workbook = Workbook(output, {'in_memory': True, 'default_date_format': 'dd/mm/yyyy'})
    # workbook = Workbook("reporte.xlsx")
    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({'bold': True})

    worksheet.set_column(0, 7, 18)
    worksheet.set_column(8, 10, 14)

    worksheet.write(0, 0, 'VISITANTE', bold)
    worksheet.write(0,1, 'TIPO ID', bold)
    worksheet.write(0,2, 'VISITANTE ID', bold)
    worksheet.write(0,3, 'ORIGEN', bold)
    worksheet.write(0,4, 'DESTINO', bold)
    worksheet.write(0,5, 'VEHICULO', bold)
    worksheet.write(0,6, 'AUTORIZADO POR', bold)
    worksheet.write(0,7, 'SEGURIDAD EN TURNO', bold)
    worksheet.write(0,8, 'FECHA', bold)
    worksheet.write(0,9, 'HORA ENTRADA', bold)
    worksheet.write(0,10, 'HORA SALIDA', bold)

    time_format = workbook.add_format({'num_format': 'hh:mm:ss AM/PM'})

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
        worksheet.write_datetime(r, 8, rval.fecha)
        worksheet.write(r, 9, rval.hora_entrada, time_format)
        worksheet.write(r, 10, rval.hora_salida, time_format)

    workbook.close()
    output.seek(0)
    nombre_archivo ="reporte" + str(datetime.now().strftime("%Y%m%d_%I%M%S%p")) + ".xlsx"

    return send_file(output, attachment_filename=nombre_archivo, as_attachment=True)