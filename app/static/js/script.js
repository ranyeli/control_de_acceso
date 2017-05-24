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
        titleFormat: "MM yyyy",
        /* Leverages same syntax as 'format' */
        weekStart: 0
    };
    $(".datepicker").datepicker({
        language: 'es',
        enableOnReadonly: false
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


    //getVisitas();
    $(".pagination a").on("click", (evt) => {
        var $evt = $(evt.target);
        $(".pagination .active").removeClass("active");
        $evt.parent().addClass("active");
        //alert(evt.innerHTML);
        var limit = parseInt($("#limit").val(), 10);
        var offset = "offset=" + (limit * parseInt($evt.text()));
        var limitplus = "limit=" + (limit + 1);
        getVisitas({
            "e": $evt,
            "p": [offset, limitplus],
            "limit": limit
        });
    });


});