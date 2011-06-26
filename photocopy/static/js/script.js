$(function(){
        $("input").keyup(function(){
                var value = $(this).val();
                $.ajax({
                        type:"GET",
                        url:"/api/search?value="+value,
                        success:function(data){
                            console.log(arguments[0]);
                        }
                    });
            });
    });
