$(document).ready(function(){
    $(".change_cart").click(function(){
        $.ajax({
            url: $(".change_cart").attr("value"),
            type: 'get',
            success: function(data){
                location.reload(true);
            },
            failure: function(data){
                alert("Algo deu errado... Recarregue a página.");
            }
        })
    })
})
