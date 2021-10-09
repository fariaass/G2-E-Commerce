$(document).ready(function(){
    $(".pp").click(function(){
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
    });
    $(".bt-ok").click(function(){
        var cep = document.getElementsByClassName("p");
        alert(cep.value);
        console.log(cep);
        $.ajax({
            method: "GET",
            url: `https://maps.googleapis.com/maps/api/distancematrix/json?origins=place_id:89110536&destinations=place_id:89110458&key=${'AIzaSyAYLU0UXZLiKI4TQbbFr76i9shto3fUvOU'}`,
            success: function(data){
                console.log(data);
                var element = document.getElementsByClassName("frete-result");
                element.innerText = data.rows.elements.distance.value;
                alert(data); 
            }
        });
    });
});

function devolve_json(){
    var elementspp = document.getElementsByClassName("pp");
    var elementsmult = document.getElementsByClassName("mult");
    var elementsunit = document.getElementsByClassName("unit");
    var elementsid = document.getElementsByClassName("carrinho-descricao-produto");
    var total = document.getElementsByClassName("total-carrinho");
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
    total[0].innerText = somatotal;
    console.log(objects)
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