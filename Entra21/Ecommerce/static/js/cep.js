function limpa_formulario(){
    document.getElementById("id_rua").value="";
    document.getElementById("id_bairro").value="";
    document.getElementById("id_cidade").value="";
    document.getElementById("id_estado").value="";
}

function meu_callback(conteudo){
    if (!("erro" in conteudo)){
        document.getElementById("id_rua").value=conteudo.logradouro;
        document.getElementById("id_bairro").value=conteudo.bairro;
        document.getElementById("id_cidade").value=conteudo.localidade;
        document.getElementById("id_estado").value=conteudo.uf;
    }
    else{
        limpa_formulario();
        alert("CEP não encontrado.")
    }
}

function pesquisacep(valor){
    var cep = valor.replace(/\D/g, '');
    if (cep != ""){
        var validacep = /^[0-9]{8}$/;
        if (validacep.test(cep)){
            document.getElementById("id_rua").value="...";
            document.getElementById("id_bairro").value="...";
            document.getElementById("id_cidade").value="...";
            document.getElementById("id_estado").value="...";
            var script = document.createElement('script')
            script.src = "https://viacep.com.br/ws/"+ cep + "/json/?callback=meu_callback";

            document.body.appendChild(script);
        }
    }
    else{
        limpa_formulario();
        alert("Formato de CEP inválido.");
    }
}

$(document).ready(function(){
    $("#id_cep").blur(function(){
        pesquisacep($(this).val());
    })
    })