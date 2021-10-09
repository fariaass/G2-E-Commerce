$(document).ready(function(){
    $(".pp").click(function(){
        var json = devolve_json();
        $.ajax({
            method: "GET",
            url: "/pedidos/teste/",
            data: {dados: json},
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
        var object = {id: id, qtd: Number(qtd), unit: Number(textunit), total: valor_final};
        objects.push(object);
        elementsmult[i].innerText = valor_final;
        somatotal += valor_final;
    }
    total[0].innerText = somatotal;
    console.log(objects)
    return objects;
}