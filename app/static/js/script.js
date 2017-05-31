/**
 * Created by Robert Ranyeli Lopez Ferreira
 */

$(() => {
    $.fn.datepicker.dates['es'] = {
        days: ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"],
        daysShort: ["Dom", "Lun", "Mar", "Mié", "Jue", "Vie", "Sáb"],
        daysMin: ["Do", "Lu", "Ma", "Mi", "Ju", "Vi", "Sá"],
        months: ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"],
        monthsShort: ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"],
        today: "Hoy",
        clear: "Limpiar",
        format: "dd/mm/yyyy",
        titleFormat: "MM yyyy",
        /* Leverages same syntax as 'format' */
        weekStart: 0
    };
    $(".datepicker").datepicker({
        language: 'es',
        enableOnReadonly: false,
        clearBtn: true
    });
    $.mask.definitions['h'] = "[APap]";
    $.mask.definitions['z'] = "[Mm]";
    $("#visitante_cedula").mask("999-9999999-9");
    $(".v_hora").mask("99:99:99 hz");
    $(".datepicker").mask("99/99/9999");

    var updatingTime = setInterval(updateTime, 1000);

    $("#reg_hora > a").on("click", () => {
        clearInterval(updatingTime);
        $("#visita_hora").removeAttr("readonly");
    });

    $("#reg_fecha > a").on("click", () => $("#visita_fecha").removeAttr("readonly"));

    popularTabla();

    $("#limit").change(function(e) {
        var $e = $(e.target);
        $('#visitas_table').bootstrapTable('refreshOptions', {
            //pagination: true,
            //search: true,
            pageSize: parseInt($e.val())
        });
    });

    $("#filtros .datepicker").on("change", (e) => {
        $e = $(e.target);
        var isDate = /[0-9]{2}\/[0-9]{2}\/[0-9]{4}/.test($e.val());
        var isBlur = $e.val() == $e.data("prevBlur");
        console.log(isBlur);

        if ((isDate || $.trim($e.val()).length == 0) && !isBlur) {
            //alert($e.attr('id'));
            // my match regex /[0-9]{2}\/[0-9]{2}\/[0-9]{4}/
            $('#visitas_table').bootstrapTable('refreshOptions', {
                queryParams: queryParams
            });

            $e.data("prevBlur", $e.val());
        }
    });

    $("#filtros .v_hora").on("keyup", (e) => {
        $e = $(e.target);
        var isHour = /[0-9]{2}:[0-9]{2}:[0-9]{2}\s[AaPp][Mm]/.test($e.val());

        if ($.trim($e.val()).length == 0 || isHour) {
            $('#visitas_table').bootstrapTable('refreshOptions', {
                queryParams: queryParams
            });
        }
    });

    $("#buscar_visita").on("keyup", (e) => {
        $e = $(e.target);

        $('#visitas_table').bootstrapTable('refreshOptions', {
            queryParams: queryParams
        });

    });

    $("#a_buscar a").on("click", (e) => {
        $e = $(e.target);
        $("#buscar_por strong").text($e.text());
        $("#a_buscar .hidden").toggleClass("hidden show");
        $e.parent().toggleClass("show hidden");

    });

    $("#visitante_tipo_id").val($("#visitante_id_tipo strong").text());

    $("#tipo_doc a").on("click", (e) => {
        $e = $(e.target);
        $("#visitante_id_tipo strong").text($e.text());
        $("#visitante_tipo_id").val($e.text());
        $("#tipo_doc .hidden").toggleClass("hidden show");
        $e.parent().toggleClass("show hidden");

    });

    $("#visita_destino").editableSelect();

    popularDestinos();

    $("#a_destino").on("click", () => registrarDestino());

    $('#entra_sale').on("change", (e) => {
        var $e = $(e.target);

        var $form = $("#form_registrar");
        var url = $form.attr("action").split("/");
        url[url.length - 1] = $e.find(":selected").text().toLowerCase();
        $form.attr("action", url.join("/"));

        var $inputs = $("#visita_razon, #form_registrar input[type=text]:not(#visita_hora):not(#visitante_identidad):not(#visitante_tipo_id)");

        if ($e.val() == 2) {

            for (var input of $inputs) {
                var $input = $(input);
                $input.attr("disabled", "disabled");
            }

        } else {

            for (var input of $inputs) {
                var $input = $(input);
                $input.removeAttr("disabled");
            }

        }
    });

    $('#form_registrar').submit(function(event) {

        event.preventDefault(); //this will prevent the default submit

        $("#destino_id").val($("#visita_destino ~ .es-list").find(".es-visible").attr("value"));

        $(this).unbind('submit').submit(); // continue the submit unbind preventDefault
    })

    $("#b_visita button").on("click", () => {
        $.get('/visita/tipo_id/' +
            $("#visitante_tipo_id").val() +
            '/identidad/' + $("#visitante_identidad").val(),
            (data, status) => {
                console.log(data);
                popularRegistro(data);
            });
    });

});