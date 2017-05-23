/**
 * Created by Robert Ranyeli Lopez Ferreira
 */

/*$('a[data-toggle="tab"]').on('shown.bs.tab', function (e) {
  var target = $(e.target).attr("href") // activated tab
  alert(target);
});*/

$(document).ready(() => {
	$.fn.datepicker.dates['es'] = {
    days: ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"],
    daysShort: ["Dom", "Lun", "Mar", "Mié", "Jue", "Vie", "Sáb"],
    daysMin: ["Do", "Lu", "Ma", "Mi", "Ju", "Vi", "Sá"],
    months: ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"],
    monthsShort: ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"],
    today: "Hoy",
    clear: "Limpiar",
    format: "dd/mm/yyyy",
    titleFormat: "MM yyyy", /* Leverages same syntax as 'format' */
    weekStart: 0
	};
	$(".datepicker").datepicker({language:'es', enableOnReadonly: false});
	$.mask.definitions['h'] = "[APap]";
	$.mask.definitions['z'] = "[Mm]";
	$("#visitante_cedula").mask("999-9999999-9");
	$(".v_hora").mask("99:99:99 hz");
	$(".datepicker").mask("99/99/9999");
	function updateTime(){
    	var currentTime = new Date();
    	var hours = currentTime.getHours();
    	var hours12 = hours == 12 || hours == 0 ? 12 : hours % 12;
    	var minutes = currentTime.getMinutes();
    	if (minutes < 10){
    	    minutes = "0" + minutes;
   	 }
   	 var seconds = currentTime.getSeconds();
   	 if (seconds < 10) {
   	 	seconds = "0" + seconds;
   	 }
   	 if (hours12 < 10) {
			hours12 = "0" + hours12;
   	 }
   	 var t_str = hours12 + ":" + minutes + ":" + seconds + " ";
   	 if(hours > 11){
   	     t_str += "PM";
   	 } else {
   	     t_str += "AM";
   	 }
   	 document.getElementById('visita_hora').value = t_str;
	}
	var updatingTime = setInterval(updateTime, 1000);
	
	$("#reg_hora > a").on("click", ()=>{
			clearInterval(updatingTime);
			$("#visita_hora").removeAttr("readonly");
		});
		
	$("#reg_fecha > a").on("click", ()=>$("#visita_fecha").removeAttr("readonly"));
	
	//var $table = $('#table');

	function visitasCallback(mydata) {	
		$('#visitas_table').bootstrapTable({
   		data: mydata
    	});
    }
    
    $.ajax({
    	method:"GET",
		url:"/visitas" + "",
		dataType:"json"    
    }).done(function (mydata) {
		visitasCallback(mydata);
		console.log(mydata);
    }).fail(function () {
		alert("fallo");    
    });

});

