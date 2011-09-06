var ajaxSearchTimer;
var ajaxSearchWait = 1000; //Wait timer defined in milliseconds
var currentQuery;

function ajaxSearch(query) {
        if(query.length > 3 && currentQuery != query) {
                                $.ajax({
                                        type:"GET",
                                        url:"/api/search/"+query,
                                        success:function(data){
                                            $("#bookmarks").html("");
                                            for(var i = 0, len = data.length;i<len;i++){
                                                var photocopy = data[i].fields;
                                                $("#bookmarks").append("<li><a href='"+photocopy.url+"'>"+photocopy.title+"</a>");
                                            }
                                            currentQuery = query;
                                        }
                                });
        }
}

$(function(){
        $("input").keyup(function(){            
                clearTimeout(ajaxSearchTimer);
                var value = $(this).val();
                if(value.length > 3) {
                    ajaxSearchTimer = setTimeout("ajaxSearch(\'"+value+"\')", ajaxSearchWait);
                }
            });
    });

