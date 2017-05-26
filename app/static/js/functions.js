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

	function popularTabla() {

	    var options = {
	        url: "/visitas?",
	        method: 'get',
	        pageNumber: 1,
	        pageSize: parseInt($("#limit").val()),
	        queryParams: function(p) {
	            console.log(p);
	            return {
	                limit: p.limit,
	                offset: p.offset,

	            };
	        },

	        cache: false,
	        pagination: true,
	        paginationLoop: true,
	        nothing: true,
	        sidePagination: 'server'
	    }

	    $('#visitas_table').bootstrapTable(options);

	}