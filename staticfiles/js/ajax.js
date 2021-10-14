$(document).ready(function(){
    $(".ajax-class").click(function(){
        $.ajax({
            url: $(".ajax-class").attr("value"),
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
