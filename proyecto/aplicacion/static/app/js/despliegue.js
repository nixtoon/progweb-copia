//function desplegar_credito() {
//    document.getElementById('credit_panel').style.display = 'block';
//}
//function ocultar_credit() {
//    document.getElementById('credit_panel').style.display = 'none';
//}

$(document).ready(function(){
    $("#credit").click(function(){
        $("#credit_panel").slideDown("slow");
    });
});

$(document).ready(function(){
    $("#desplegar_debito").click(function(){
        $("#debit_panel").slideDown("slow");
    });
});