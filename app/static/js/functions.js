	function updateTime() {
	    var currentTime = new Date();
	    var hours = currentTime.getHours();
	    var hours12 = hours == 12 || hours == 0 ? 12 : hours % 12;
	    var minutes = currentTime.getMinutes();
	    if (minutes < 10) {
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
	    if (hours > 11) {
	        t_str += "PM";
	    } else {
	        t_str += "AM";
	    }
	    $('#visita_hora').value = t_str;
	}

	function visitasCallback(mydata) {
	    $('#visitas_table').bootstrapTable({
	        data: mydata.visitas
	    });
	}

	function agregarPagina(e, n, limit) {

	    var isNext = isNaN(e.parent().next().text());
	    var isPrev = isNaN(e.parent().prev().text());
	    if (n > limit && isNext) {

	    }

	}

	function getVisitas(params) {
	    var args = params.p;
	    var limit = parseint($("#limit").val());
	    $.ajax({
	        method: "GET",
	        url: "/visitas?" + args.join("&"),
	        dataType: "json"
	    }).done(function(mydata) {
	        visitasCallback(mydata);
	        agregarPagina(params.e, mydata.total, limit);
	        console.log(mydata);
	    }).fail(function() {
	        alert("fallo");
	    });
	}