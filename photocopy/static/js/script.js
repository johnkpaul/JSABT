$(function(){
        $("input").keyup(function(){
                var value = $(this).val();
                $.ajax({
                        type:"GET",
                        url:"/api/search/"+value,
                        success:function(data){
                            $("#bookmarks").html("");
                            for(var i = 0, len = data.length;i<len;i++){
                                var photocopy = data[i].fields;
                                $("#bookmarks").append("<li><a href='"+photocopy.url+"'>"+photocopy.title+"</a>");
                            }
                        }
                    });
            });
    });
