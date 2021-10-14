$(document).ready(function(){
    send_to_server();
    $(".pp").click(function(){
        send_to_server();
    });
    $(".bt-ok").click(function(){
        var cep = document.getElementById("cep");
        var frete = document.getElementsByClassName("frete-result");
        var total = document.getElementsByClassName("total-carrinho");
        cep = cep.value;
        if (cep < 88000000 || cep > 89999999){
            var valor_frete = 40;
        }else{
            var valor_frete = 15;
        }
        var somatotal = valor_frete + Number(total[0].innerText);
        frete[0].innerText = valor_frete;
        total[0].innerText = somatotal;
        send_to_server();
    });
});

function devolve_json(){
    var elementspp = document.getElementsByClassName("pp");
    var elementsmult = document.getElementsByClassName("mult");
    var elementsunit = document.getElementsByClassName("unit");
    var elementsid = document.getElementsByClassName("carrinho-descricao-produto");
    var total = document.getElementsByClassName("total-carrinho");
    var frete = document.getElementsByClassName("frete-result");

    var objects = [];
    var somatotal = 0;
    for (var i = 0; i < elementspp.length; i++){
        qtd = elementspp[i].value;
        textmult = elementsmult[i].innerText;
        textunit = elementsunit[i].innerText;
        id = elementsid[i].id;
        var valor_final = qtd * Number(textunit);
        var object = {id: Number(id), qtd: Number(qtd), unit: Number(textunit), total: valor_final};
        objects.push(object);
        elementsmult[i].innerText = valor_final;
        somatotal += valor_final;
    }
    var valor_frete = Number(frete[0].innerText);
    total[0].innerText = somatotal + valor_frete;
    objects.push(valor_frete);
    console.log(objects);
    return objects;
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function send_to_server(){
    var json = devolve_json();
    var csrftoken = getCookie('csrftoken');
    $.ajax({
        method: "POST",
        url: "/pedidos/inicia-pedido/",
        data: {dados: json, csrfmiddlewaretoken: csrftoken},    
    });

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
    beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
}
