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
	    $('#visita_hora').val(t_str);
	}

	function queryParams(p) {
	    return {
	        limit: p.limit,
	        offset: p.offset,
	        desde_fecha: $('#desde_fecha').val(),
	        hasta_fecha: $('#hasta_fecha').val(),
	        desde_hora: $('#desde_hora').val(),
	        hasta_hora: $('#hasta_hora').val(),
	        buscar: $("#buscar_visita").val(),
	        buscarPor: $("#buscar_por strong").text()
	    };
	}

	function popularTabla() {

	    var options = {
	        url: "/visitas?",
	        method: 'get',
	        pageNumber: 1,
	        pageSize: parseInt($("#limit").val()),
	        queryParams: queryParams,
	        //search: true,
	        cache: false,
	        pagination: true,
	        paginationLoop: true,
	        nothing: true,
	        sidePagination: 'server'
	    }

	    $('#visitas_table').bootstrapTable(options);

	}

	function popularDestinos() {
	    var $destino = $('#visita_destino ~ .es-list');
	    $.get('/destinos/', function(json, status) {
	        $destino.empty();
	        $.each(json, function(i, value) {
	            //console.log('i = ' + value.destino_id + ', ' + 'value = ' + value.destino);
	            $destino.append($('<li>')
	                .text(value.destino)
	                .attr('value', value.destino_id).addClass('es-visible'));
	        });

	        var selected = $('#visita_destino ~ .es-list li:contains("' + $('#visita_destino').val() + '")');
	        selected.addClass('selected');
	    });

	    // $("#visita_destino").click();
	}

	function registrarDestino() {
	    $.post('registrar/destino/' + $('#visita_destino').val(), function(data, status) {
	        popularDestinos();
	        var mensase = $('#mensaje_destino').toggleClass("hidden show");
	        mensase.fadeOut(6000, function() {
	            mensase.toggleClass("show hidden");
	        });
	    });
	}

	function popularRegistro(data) {
	    var $nombre = $("#visitante_nombre");
	    //var $apellido = $("#visitante_apellido");
	    var $v_marca = $("#vehiculo_marca");
	    var $v_tipo = $("#vehiculo_tipo");
	    var $v_color = $("#vehiculo_color");
	    var $v_placa = $("#vehiculo_placa");
	    var $razon = $("#visita_razon");
	    var $origen = $("#visita_origen");
	    var $destino = $("#visita_destino");
	    var $autoriza = $("#visita_autorizada");
	    var $seguridad = $("#seguridad_turno");

	    var isEntrando = $("#entra_sale").val() == 1;
	    $nombre.val(data.visitante_nombre);
	    //$apellido.val(data.visitante_apellido)
	    if (!isEntrando) {
	        $v_color.val(data.vehiculo_color);
	        $v_marca.val(data.vehiculo_marca);
	        $v_placa.val(data.vehiculo_placa);
	        $v_tipo.val(data.vehiculo_tipo);
	        $razon.val(data.razon);
	        $origen.val(data.origen);
	        $destino.val(data.destino);
	        $autoriza.val(data.autorizada_por);
	        $seguridad.val(data.seguridad_de_turno);
	    }
	}